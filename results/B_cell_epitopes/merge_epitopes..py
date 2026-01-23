import os
import pandas as pd

# ---------------------------------------------
# Use current directory (B_cell_epitopes)
# ---------------------------------------------
base_dir = os.getcwd()

merged_data = []

for protein_folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, protein_folder)

    if os.path.isdir(folder_path):
        csv_path = os.path.join(folder_path, "result.csv")

        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            df["Protein_Source"] = protein_folder
            merged_data.append(df)

if merged_data:
    master_df = pd.concat(merged_data, ignore_index=True)
    master_df.to_csv("Bcell_Epitope_Master_Results.csv", index=False)
    print("Merged file created: Bcell_Epitope_Master_Results.csv")
else:
    print("No result.csv files found.")

