import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
result_file_path = 'result.csv'  # Update this path to the correct location on your local machine
result_df = pd.read_csv(result_file_path)

# Basic statistics
total_peptides = result_df['peptide'].nunique()
average_score = result_df['score'].mean()
max_score = result_df['score'].max()
min_score = result_df['score'].min()

# Display basic statistics
print(f"Total unique peptides: {total_peptides}")
print(f"Average Immunogenicity Score: {average_score:.4f}")
print(f"Max Immunogenicity Score: {max_score:.4f}")
print(f"Min Immunogenicity Score: {min_score:.4f}")

# Generate a histogram for Immunogenicity Scores
plt.figure(figsize=(8, 6))
sns.histplot(result_df['score'], kde=True, color='skyblue', bins=20)
plt.title('Distribution of Immunogenicity Scores for MHC Class I Peptides')
plt.xlabel('Immunogenicity Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("Immunogenicity_Score_Distribution.png", dpi=300)  # Save the plot
plt.show()

# Top 10 peptides based on immunogenicity score
top_10_peptides = result_df.nlargest(10, 'score')[['peptide', 'score']]

# Display the top 10 peptides with highest immunogenicity scores
print("\nTop 10 Peptides Based on Immunogenicity Scores:")
print(top_10_peptides)

# Save the top 10 peptides to a CSV file for reference
top_10_peptides.to_csv("Top_10_Peptides_Immunogenicity.csv", index=False)

