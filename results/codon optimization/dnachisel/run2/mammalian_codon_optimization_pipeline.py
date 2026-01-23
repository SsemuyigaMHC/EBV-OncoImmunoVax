from dnachisel import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction
import pandas as pd
import random
import os
import subprocess

# === USER SETTINGS ===
input_fasta = "best5_tagged.fasta"
codon_usage_csv = "cricetulus_codon_usage.csv"
restriction_sites_to_avoid = ["GAATTC", "GGATCC", "AAGCTT", "CTGCAG"]  # EcoRI, BamHI, HindIII, PstI
rnafold_path = "/usr/bin/RNAfold"  # Ensure RNAfold is installed in WSL

# === Step 1: Load codon usage table ===
codon_usage_df = pd.read_csv(codon_usage_csv)
custom_codon_table = {}
for aa, group in codon_usage_df.groupby("AminoAcid"):
    codons = group["Codon"].tolist()
    freqs = group["Frequency"].tolist()
    weights = [f / sum(freqs) for f in freqs]
    custom_codon_table[aa] = (codons, weights)

# === Step 2: Custom reverse translate function ===
def custom_reverse_translate(protein_seq, stop_codon="TAA"):
    dna_seq = ""
    for aa in protein_seq:
        if aa == "*":
            dna_seq += stop_codon
        else:
            codons, weights = custom_codon_table.get(aa, ([], []))
            if not codons:
                raise ValueError(f"No codons found for amino acid: {aa}")
            dna_seq += random.choices(codons, weights=weights)[0]
    return dna_seq

# === Step 3: Predict RNA secondary structure with RNAfold ===
def predict_rna_structure(seq):
    rna_input = f"{seq}\n"
    result = subprocess.run([rnafold_path], input=rna_input, capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")
    structure_info = lines[1] if len(lines) > 1 else "NA"
    mfe = structure_info.split(" (")[-1].rstrip(")") if "(" in structure_info else "NA"
    return mfe, result.stdout

# === Step 4: Prepare output folders ===
os.makedirs("optimized_sequences", exist_ok=True)
os.makedirs("rnafold_structures", exist_ok=True)

# === Step 5: Load protein sequences ===
protein_records = list(SeqIO.parse(input_fasta, "fasta"))
optimized_records = []
summary_data = []

# === Step 6: Optimize each sequence ===
for record in protein_records:
    print(f"\n🔬 Optimizing: {record.id}")
    try:
        # Step 6a: Reverse translate
        dna_seq = custom_reverse_translate(str(record.seq))

        # Step 6b: Define optimization problem
        problem = DnaOptimizationProblem(
            sequence=dna_seq,
            constraints=[
                EnforceGCContent(mini=0.45, maxi=0.65, window=100),
                *[AvoidPattern(site) for site in restriction_sites_to_avoid],
                AvoidStopCodons()
            ],
            objectives=[]  # No CodonOptimize — you're using your own codon table
        )

        # Step 6c: Optimize
        problem.optimize()
        optimized_seq = problem.sequence

        # Step 6d: Translate and verify match
        translated = Seq(optimized_seq).translate(to_stop=True)
        match = str(translated) == str(record.seq).rstrip("*")
        gc = gc_fraction(optimized_seq)

        # Step 6e: Predict RNA structure
        mfe, rna_output = predict_rna_structure(optimized_seq)
        with open(f"rnafold_structures/{record.id}_structure.txt", "w") as f:
            f.write(rna_output)

        # Step 6f: Save optimized sequence
        optimized_record = SeqRecord(
            Seq(optimized_seq),
            id=record.id,
            description="Codon optimized, GC controlled, motif-avoided"
        )
        optimized_records.append(optimized_record)

        # Step 6g: Store summary
        summary_data.append({
            "ID": record.id,
            "Length (nt)": len(optimized_seq),
            "GC Content (%)": round(gc * 100, 2),
            "Back-Translation Match": match,
            "MFE (RNAfold)": mfe
        })

    except Exception as e:
        print(f"❌ Error with {record.id}: {e}")
        summary_data.append({
            "ID": record.id,
            "Length (nt)": "NA",
            "GC Content (%)": "NA",
            "Back-Translation Match": False,
            "MFE (RNAfold)": "NA",
            "Error": str(e)
        })

# === Step 7: Save optimized FASTA and summary ===
SeqIO.write(optimized_records, "optimized_sequences/optimized_dna.fasta", "fasta")
df = pd.DataFrame(summary_data)
df.to_csv("optimized_sequences/dna_analysis_summary.csv", index=False)

# === Step 8: Save vector cloning version (ATG...TAA) ===
with open("optimized_sequences/for_vector_cloning.txt", "w") as f:
    for rec in optimized_records:
        f.write(f">{rec.id}_vector_ready\n")
        f.write(f"ATG{str(rec.seq)}TAA\n")

print("\n✅ Optimization complete. Summary saved.")

