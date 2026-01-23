import os
import subprocess
import json

def remove_oxt(pdb_file):
    try:
        with open(pdb_file, "r") as f:
            lines = f.readlines()

        with open(pdb_file, "w") as f:
            for line in lines:
                if " OXT " not in line:
                    f.write(line)

        print(f"✅ Cleaned OXT atoms from {pdb_file}")
    except Exception as e:
        print(f"❌ ERROR cleaning {pdb_file}: {e}")

def update_setup_with_grid(setup_path, grid_path):
    try:
        with open(grid_path, "r") as grid_file:
            grid_data = json.load(grid_file)

        with open(setup_path, "r") as setup_file:
            setup_data = json.load(setup_file)

        setup_data["swarm_centers"] = grid_data.get("swarm_centers", setup_data.get("swarm_centers"))
        setup_data["swarm_sizes"] = grid_data.get("swarm_sizes", setup_data.get("swarm_sizes"))

        with open(setup_path, "w") as setup_file:
            json.dump(setup_data, setup_file, indent=4)

        print(f"✅ Updated setup.json with grid from {grid_path}")
    except Exception as e:
        print(f"❌ ERROR updating setup.json: {e}")

# Settings
receptors_dir = "receptors"
ligand_sets = {
    "adjuvants": "adjuvants",
    "nonadjuvants": "nonadjuvants"
}
results_base = "results"
num_iterations = 100
scoring_function = "dfire2"
basedir = os.getcwd()

print(f"🔍 Starting batch docking in: {basedir}")

for set_name, ligand_dir in ligand_sets.items():
    ligands_path = os.path.join(basedir, ligand_dir)
    result_path = os.path.join(basedir, f"results_{set_name}")
    os.makedirs(result_path, exist_ok=True)

    for receptor_file in os.listdir(receptors_dir):
        if not receptor_file.endswith(".pdb"):
            continue
        receptor_path = os.path.join(receptors_dir, receptor_file)
        receptor_name = os.path.splitext(receptor_file)[0]

        for ligand_file in os.listdir(ligands_path):
            if not ligand_file.endswith(".pdb"):
                continue
            ligand_path = os.path.join(ligands_path, ligand_file)
            ligand_name = os.path.splitext(ligand_file)[0]

            pair_name = f"{receptor_name}_{ligand_name}"
            work_dir = os.path.join(result_path, pair_name)
            if os.path.exists(work_dir):
                print(f"⏭️ Skipping {pair_name}, folder already exists.")
                continue
            os.makedirs(work_dir)

            rec_copy = os.path.join(work_dir, "receptor.pdb")
            lig_copy = os.path.join(work_dir, "ligand.pdb")

            # Copy and clean files
            with open(receptor_path, "r") as src, open(rec_copy, "w") as dst:
                dst.writelines(src.readlines())
            with open(ligand_path, "r") as src, open(lig_copy, "w") as dst:
                dst.writelines(src.readlines())
            remove_oxt(rec_copy)
            remove_oxt(lig_copy)

            os.chdir(work_dir)

            setup_command = f'lightdock3_setup.py receptor.pdb ligand.pdb --noh'
            print(f"\n🛠️ Running setup for {pair_name}...")
            setup_result = subprocess.run(setup_command, shell=True, capture_output=True, text=True)
            print(setup_result.stdout)
            if setup_result.returncode != 0:
                print(f"❌ Setup failed for {pair_name}: {setup_result.stderr}")
                os.chdir(basedir)
                continue

            grid_path = os.path.join(work_dir, "grid.json")
            setup_path = os.path.join(work_dir, "setup.json")
            if os.path.exists(grid_path) and os.path.exists(setup_path):
                update_setup_with_grid(setup_path, grid_path)

            docking_command = f'lightdock3.py setup.json {num_iterations} --scoring {scoring_function}'
            print(f"🚀 Running docking for {pair_name}...")
            docking_result = subprocess.run(docking_command, shell=True, capture_output=True, text=True)
            print(f"📄 Docking STDOUT for {pair_name}:")
            print(docking_result.stdout)
            print(f"📄 Docking STDERR for {pair_name}:")
            print(docking_result.stderr)
            if docking_result.returncode != 0:
                print(f"❌ Docking failed for {pair_name}")

            os.chdir(basedir)

print("\n✅ All docking completed.")
