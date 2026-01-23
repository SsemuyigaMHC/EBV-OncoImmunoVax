import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the MHC I and MHC II epitope data (use your actual file paths)
mhc_i_file = "Unique_MHC_I_Epitopes.csv"
mhc_ii_file = "Unique_MHC_II_Epitopes.csv"

mhc_i_df = pd.read_csv(mhc_i_file)
mhc_ii_df = pd.read_csv(mhc_ii_file)

# Total epitopes predicted
total_mhc_i_epitopes = mhc_i_df['peptide'].nunique()
total_mhc_ii_epitopes = mhc_ii_df['peptide'].nunique()

# Create a 2x2 grid for the plots
plt.figure(figsize=(12, 12))

# A. MHC I Rank Distribution
plt.subplot(2, 2, 1)
plt.hist(mhc_i_df['rank'], bins=20, color='skyblue', edgecolor='black')
plt.title('A. MHC Class I Epitope Rank Distribution')
plt.xlabel('Rank')
plt.ylabel('Frequency')

# B. MHC II Rank Distribution
plt.subplot(2, 2, 2)
plt.hist(mhc_ii_df['rank'], bins=20, color='lightgreen', edgecolor='black')
plt.title('B. MHC Class II Epitope Rank Distribution')
plt.xlabel('Rank')
plt.ylabel('Frequency')

# C. MHC I Epitope Score vs Rank
plt.subplot(2, 2, 3)
sns.scatterplot(x=mhc_i_df['rank'], y=mhc_i_df['score'], color='skyblue')
plt.title('C. MHC Class I Epitope Score vs Rank')
plt.xlabel('Rank')
plt.ylabel('Score')

# D. MHC II Epitope Score vs Rank
plt.subplot(2, 2, 4)
sns.scatterplot(x=mhc_ii_df['rank'], y=mhc_ii_df['score'], color='lightgreen')
plt.title('D. MHC Class II Epitope Score vs Rank')
plt.xlabel('Rank')
plt.ylabel('Score')

plt.tight_layout()
plt.savefig("Epitope_Analysis_Grid.png", dpi=300)  # Save to file
plt.show()  # Show the plots

# Top 10 MHC I and II candidates based on the lowest rank
top_mhc_i_candidates = mhc_i_df.nsmallest(10, 'rank')
top_mhc_ii_candidates = mhc_ii_df.nsmallest(10, 'rank')

# Include the 'seq_num' column to identify protein sources
top_mhc_i_candidates = top_mhc_i_candidates[['peptide', 'rank', 'score', 'seq_num']]
top_mhc_ii_candidates = top_mhc_ii_candidates[['peptide', 'rank', 'score', 'seq_num']]

# Save these as CSV for further exploration
top_mhc_i_candidates.to_csv("Top_MHC_I_Candidates.csv", index=False)
top_mhc_ii_candidates.to_csv("Top_MHC_II_Candidates.csv", index=False)

# Display summary of results
print(f"Total MHC I Epitopes: {total_mhc_i_epitopes}")
print(f"Total MHC II Epitopes: {total_mhc_ii_epitopes}")
print("\nTop MHC I Candidates:")
print(top_mhc_i_candidates[['peptide', 'rank', 'score', 'seq_num']])
print("\nTop MHC II Candidates:")
print(top_mhc_ii_candidates[['peptide', 'rank', 'score', 'seq_num']])

