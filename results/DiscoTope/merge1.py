import os
import pandas as pd

# ============================================
# Run from:
# C:\Users\MHC V(D)J\EBV\DiscoTope
# ============================================
base_dir = os.getcwd()

merged = []

for folder in sorted(os.listdir(base_dir)):
    folder_path = os.path.join(base_dir, folder)

    if not os.path.isdir(folder_path):
        continue

    csv_file = os.path.join(folder_path, "result.csv")

    if not os.path.exists(csv_file):
        print(f"⚠ Skipped (no result.csv): {folder}")
        continue

    try:
        # IMPORTANT: skip descriptive first row, no headers
        df = pd.read_csv(csv_file, skiprows=1, header=None)

        # Add metadata only
        df["Protein_Source"] = folder
        df["Prediction_Method"] = "DiscoTope"

        merged.append(df)
        print(f"✔ Merged: {folder}")

    except Exception as e:
        print(f"✖ Error reading {folder}: {e}")

# ============================================
# SAVE MASTER FILE
# ============================================
if merged:
    master_df = pd.concat(merged, ignore_index=True)

    output_name = "DiscoTope_Bcell_Epitope_Master_Results.csv"
    master_df.to_csv(output_name, index=False)

    print("\n✅ Master DiscoTope file created")
    print(f"   File: {output_name}")
    print(f"   Rows: {len(master_df)}")
    print(f"   Columns: {len(master_df.columns)}")

else:
    print("\n❌ No valid result.csv files found")

