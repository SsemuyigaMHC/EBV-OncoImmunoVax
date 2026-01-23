import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# Embedded data: Top 10 global B-cell epitopes
# --------------------------------------------------
epitopes = [
    "CVLVLIV\n(LMP2_2)",
    "LCVFCLV\n(gH)",
    "CVFCLVL\n(gH)",
    "LVVLLIC\n(LMP2_2)",
    "LLCVFCL\n(gH)",
    "VLSVVVL\n(gB)",
    "VCLPVIV\n(LMP2_2)",
    "VFCLVLL\n(gH)",
    "LACVLVL\n(LMP2_2)",
    "YCCYYCL\n(LMP2_2)"
]

mean_antigenicity_scores = [
    1.316, 1.312, 1.312, 1.297, 1.293,
    1.292, 1.290, 1.288, 1.285, 1.281
]

ranks = np.arange(1, len(epitopes) + 1)

# --------------------------------------------------
# Plot
# --------------------------------------------------
plt.figure(figsize=(12, 6))

bars = plt.bar(
    ranks,
    mean_antigenicity_scores,
    width=0.6
)

# --------------------------------------------------
# Formatting
# --------------------------------------------------
plt.xlabel("Ranked B-cell Epitopes (Sequence and Source Protein)", fontsize=12)
plt.ylabel("Mean Antigenicity Score", fontsize=12)
plt.title(
    "Top 10 Global Linear B-cell Epitopes Predicted Across EBV Proteins",
    fontsize=14
)

plt.xticks(ranks, epitopes, rotation=35, ha="right", fontsize=10)
plt.ylim(1.25, 1.33)

# Annotate bars with score values
for bar, score in zip(bars, mean_antigenicity_scores):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.002,
        f"{score:.3f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

# --------------------------------------------------
# Save figure (no display)
# --------------------------------------------------
output_file = "Top10_Global_Bcell_Epitopes.png"
plt.savefig(output_file, dpi=600)
plt.close()

print(f"Figure saved as: {output_file}")

