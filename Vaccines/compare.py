from Bio import SeqIO
from Bio.PDB import PDBParser, PPBuilder
import os

def extract_seq_from_pdb(pdb_file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("vaccine", pdb_file)
    ppb = PPBuilder()
    sequence = ""
    for pp in ppb.build_peptides(structure):
        sequence += str(pp.get_sequence())
    return sequence

def load_fasta_sequences(fasta_file):
    return list(SeqIO.parse(fasta_file, "fasta"))

def compare_sequences(seq1, seq2):
    diffs = []
    for i, (a, b) in enumerate(zip(seq1, seq2), start=1):
        if a != b:
            diffs.append((i, a, b))
    return diffs

# === INPUT PATHS ===
pdb_folder = "pdbs"  # Folder with vaccine1.pdb to vaccine16.pdb
fasta_main = "vaccines_with_tpa_adjuvant.fasta"
fasta_compare = "vaccines_with_adjuvants.fasta"

# === PART 1: Match PDB to FASTA ===
fasta_seqs = load_fasta_sequences(fasta_main)

print("=== Verifying PDB files against FASTA ===")
for i, fasta_record in enumerate(fasta_seqs, start=1):
    pdb_file = os.path.join(pdb_folder, f"vaccine{i}.pdb")
    if not os.path.exists(pdb_file):
        print(f"[!] Missing: {pdb_file}")
        continue
    pdb_seq = extract_seq_from_pdb(pdb_file)
    fasta_seq = str(fasta_record.seq)

    if pdb_seq == fasta_seq:
        print(f"[✓] vaccine{i} - MATCHED")
    else:
        print(f"[✗] vaccine{i} - MISMATCH (Length {len(pdb_seq)} vs {len(fasta_seq)})")
        diffs = compare_sequences(pdb_seq, fasta_seq)
        print(f"    → {len(diffs)} differences")
        if diffs:
            print(f"    First few: {diffs[:5]}")

# === PART 2: Compare Two FASTA Files ===
print("\n=== Comparing FASTA: vaccines_with_adjuvants vs vaccines_with_tpa_adjuvant ===")
fasta_tpa = load_fasta_sequences(fasta_main)
fasta_plain = load_fasta_sequences(fasta_compare)

for i, (rec1, rec2) in enumerate(zip(fasta_plain, fasta_tpa), start=1):
    diffs = compare_sequences(str(rec1.seq), str(rec2.seq))
    if diffs:
        print(f"[✗] Vaccine {i}: {len(diffs)} difference(s)")
        for pos, a, b in diffs[:5]:
            print(f"    Pos {pos}: {a} → {b}")
    else:
        print(f"[✓] Vaccine {i}: Identical")


