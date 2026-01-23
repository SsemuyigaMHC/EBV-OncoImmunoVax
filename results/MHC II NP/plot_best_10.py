import matplotlib.pyplot as plt
import numpy as np

# Data for the top 10 best peptides, including Protein Source
best_peptides = [
    ("SPCYSLRFDLTRDK", 1.23087, 0.01, "gH"),
    ("SPPVTTAQATVPVPP", 1.15594, 0.06, "GP350"),
    ("YPSASGSSGNTPTPP", 1.14287, 0, "LMP2_2"),
    ("GPHDPLPHSPSDSAG", 1.13632, 0.15, "LMP1"),
    ("LPPPPYSPRDDSSQH", 1.09016, 0.02, "LMP2_2"),
    ("SPVTTPTPNATSPTP", 1.05081, 0.11, "GP350"),
    ("DPNTTTGLPSSTHVP", 0.92808, 0.18, "GP350"),
    ("DQSLYLGLQHDGNDG", 0.85345, 0.17, "LMP2_2"),
    ("DPDNTDDNGPQDPDN", 0.833, 0.64, "LMP1_2"),
    ("IDELAQQHASGEGPG", 0.8144, 0.13, "gB")
]

# Update the peptide names with protein source included
best_names = [
    f"{name} ({protein})" if "LMP2_2" not in protein else f"{name} ({protein.replace(' ', '_')})" 
    for name, _, _, protein in best_peptides
]
best_scores = [score for _, score, _, _ in best_peptides]
best_percentile = [percentile for _, _, percentile, _ in best_peptides]

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(12, 6))

# Customize bar plot style and colors
bar_width = 0.35  # Adjust bar width for better spacing
bar_color_cleavage = 'royalblue'
bar_color_percentile = 'orange'

# Position the bars side by side by adjusting the x-position for the percentile bars
x_positions = np.arange(len(best_names))

# Plot the best 10 peptides with side-by-side bars
bars1 = ax.bar(x_positions - bar_width/2, best_scores, width=bar_width, color=bar_color_cleavage, label='Cleavage Probability Score')
bars2 = ax.bar(x_positions + bar_width/2, best_percentile, width=bar_width, color=bar_color_percentile, alpha=0.5, label='Percentile Rank')

# Display the values on the bars and add protein source text
for i, bar in enumerate(bars1):
    yval = bar.get_height()
    # Adjusting the label position for the first bar to avoid overlap with the boundary
    y_offset = 0.005 if i != 0 else 0.01  # Add more space for the first bar
    ax.text(bar.get_x() + bar.get_width()/2, yval + y_offset, round(yval, 2), ha='center', va='bottom', fontsize=10)

for i, bar in enumerate(bars2):
    yval = bar.get_height()
    # Same adjustment for percentile rank values
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.03, round(yval, 2), ha='center', va='bottom', fontsize=10)

# Customize the axis labels, title, and legend
ax.set_xlabel('Peptides')
ax.set_ylabel('Scores and Percentile Ranks')
ax.set_title('Top 10 Best MHCII-NP Predicted Peptides')
ax.legend()

# Display the peptide names with protein source at the x-axis, avoiding overlap
plt.xticks(x_positions, best_names, rotation=45, ha='right')

# Add tight layout to avoid overlapping elements
plt.tight_layout()

# Save the figure to a PNG file (local path for your system)
plt.savefig('MHCII_NP_Predictions_Bar_Plots_Updated_with_Protein_Sources.png')

# Show the plot
plt.show()

