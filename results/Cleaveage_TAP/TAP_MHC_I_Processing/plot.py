import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Embedded data (EXACT as given)
# -----------------------------

peptides = [
    "YLLEMLWRL",
    "FLDKGTYTL",
    "MLYPGIDEL",
    "LLVDLLWLL",
    "WLAKSFFEL",
    "LLVDLLWLL",
    "YLQQNWWTL",
    "YLQQNWWTL",
    "FLLMLLWTL",
    "FLLMLLWTL"
]

source_proteins = [
    "LMP1",
    "gB",
    "gB",
    "LMP1",
    "gH",
    "LMP1_2",
    "LMP1",
    "LMP1_2",
    "LMP2_2",
    "LMP2"
]

proteasome_scores = [1.49, 1.48, 1.60, 1.43, 1.41, 1.34, 1.40, 1.40, 1.59, 1.59]
tap_scores         = [0.43, 0.43, 0.47, 0.46, 0.48, 0.46, 0.42, 0.42, 0.41, 0.41]
total_scores       = [1.62, 1.51, 1.36, 1.27, 1.25, 1.18, 1.09, 1.09, 1.06, 1.06]

# -----------------------------
# Plot configuration
# -----------------------------

x = np.arange(len(peptides))
width = 0.25

plt.figure(figsize=(14, 6))

plt.bar(x - width, proteasome_scores, width, label="Proteasome Score")
plt.bar(x,          tap_scores,         width, label="TAP Score")
plt.bar(x + width,  total_scores,       width, label="Total Score")

plt.xlabel("Peptides (Source Protein)")
plt.ylabel("Prediction Scores")
plt.title("Top 10 MHC-I Processing Predicted Peptides")

plt.xticks(
    x,
    [f"{p}\n({s})" for p, s in zip(peptides, source_proteins)],
    rotation=45,
    ha="right"
)

plt.legend()
plt.tight_layout()

# -----------------------------
# Save figure (no display)
# -----------------------------
plt.savefig(
    "Top10_MHCI_Processing_Predicted_Peptides.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

