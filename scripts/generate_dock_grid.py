import json
import os

# Define docking folders
docking_folders = ["docking_adjuvants", "docking_nonadjuvants"]

# Define custom grid centers and radii
grid_data = {
    "1KCG": {"center": [18.0, 19.0, 40.0], "radius": 16},
    "3BIK": {"center": [0.0, -15.0, -16.0], "radius": 16},
    "7M8S": {"center": [-9.0, 20.0, 19.0], "radius": 16},
    "8WTA": {"center": [150, 179.9, 180.0], "radius": 16}
}

# Debugging output
print("Starting JSON file creation...")

# Process each docking folder
for folder in docking_folders:
    print(f"Checking folder: {folder}")

    for receptor in grid_data.keys():
        docking_path = os.path.join(folder, receptor)
        
        # Debug: Check if folder exists
        if not os.path.exists(docking_path):
            print(f"⚠️ Folder missing: {docking_path} - Creating it now...")
            os.makedirs(docking_path, exist_ok=True)
        
        # Define JSON data
        setup_data = {"binding_box": grid_data[receptor]}
        json_path = os.path.join(docking_path, "grid.json")

        # Write JSON file
        try:
            with open(json_path, "w") as json_file:
                json.dump(setup_data, json_file, indent=4)
            print(f"✅ Created setup.json in {docking_path}")
        except Exception as e:
            print(f"❌ Error writing JSON in {docking_path}: {e}")

print("🔄 JSON file creation process completed.")
