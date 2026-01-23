import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Load data
# =========================
df = pd.read_csv("optimized_sequences/dna_analysis_summary.csv")

# =========================
# Helper function: add values on bars
# =========================
def add_bar_labels(ax, bars, fmt="{:.2f}"):
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            fmt.format(height),
            ha="center",
            va="bottom",
            fontsize=9,
            rotation=0
        )

# =========================
# ---- Individual Figures ----
# =========================

# A. GC Content
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(df["ID"], df["GC Content (%)"])
ax.set_title("A. GC Content of Codon-Optimized Vaccine Constructs", fontweight="bold")
ax.set_xlabel("Vaccine Construct")
ax.set_ylabel("GC Content (%)")
ax.set_xticklabels(df["ID"], rotation=45, ha="right")
ax.set_ylim(0, df["GC Content (%)"].max() * 1.15)
add_bar_labels(ax, bars, "{:.1f}")
plt.tight_layout()
plt.savefig("GC_content.png", dpi=300)
plt.close()

# B. Sequence Length
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(df["ID"], df["Length (nt)"])
ax.set_title("B. Sequence Length of Codon-Optimized Vaccine Constructs", fontweight="bold")
ax.set_xlabel("Vaccine Construct")
ax.set_ylabel("Length (nt)")
ax.set_xticklabels(df["ID"], rotation=45, ha="right")
ax.set_ylim(0, df["Length (nt)"].max() * 1.15)
add_bar_labels(ax, bars, "{:.0f}")
plt.tight_layout()
plt.savefig("Sequence_length.png", dpi=300)
plt.close()

# C. MFE
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(df["ID"], df["MFE (RNAfold)"])
ax.set_title("C. Predicted mRNA Stability (RNAfold MFE)", fontweight="bold")
ax.set_xlabel("Vaccine Construct")
ax.set_ylabel("Minimum Free Energy (kcal/mol)")
ax.set_xticklabels(df["ID"], rotation=45, ha="right")
add_bar_labels(ax, bars, "{:.1f}")
plt.tight_layout()
plt.savefig("MFE_plot.png", dpi=300)
plt.close()

# D. GC Content vs Length
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(df["Length (nt)"], df["GC Content (%)"])
ax.set_title("D. GC Content vs Sequence Length", fontweight="bold")
ax.set_xlabel("Length (nt)")
ax.set_ylabel("GC Content (%)")
plt.tight_layout()
plt.savefig("GC_vs_length.png", dpi=300)
plt.close()

# =========================
# ---- Combined 2×2 Grid ----
# =========================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# A
bars = axes[0, 0].bar(df["ID"], df["GC Content (%)"])
axes[0, 0].set_title("A. GC Content", fontweight="bold")
axes[0, 0].set_ylabel("GC Content (%)")
axes[0, 0].set_ylim(0, df["GC Content (%)"].max() * 1.15)
axes[0, 0].set_xticklabels(df["ID"], rotation=45, ha="right")
add_bar_labels(axes[0, 0], bars, "{:.1f}")

# B
bars = axes[0, 1].bar(df["ID"], df["Length (nt)"])
axes[0, 1].set_title("B. Sequence Length", fontweight="bold")
axes[0, 1].set_ylabel("Length (nt)")
axes[0, 1].set_ylim(0, df["Length (nt)"].max() * 1.15)
axes[0, 1].set_xticklabels(df["ID"], rotation=45, ha="right")
add_bar_labels(axes[0, 1], bars, "{:.0f}")

# C
bars = axes[1, 0].bar(df["ID"], df["MFE (RNAfold)"])
axes[1, 0].set_title("C. mRNA Stability (MFE)", fontweight="bold")
axes[1, 0].set_ylabel("MFE (kcal/mol)")
axes[1, 0].set_xticklabels(df["ID"], rotation=45, ha="right")
add_bar_labels(axes[1, 0], bars, "{:.1f}")

# D
axes[1, 1].scatter(df["Length (nt)"], df["GC Content (%)"])
axes[1, 1].set_title("D. GC Content vs Length", fontweight="bold")
axes[1, 1].set_xlabel("Length (nt)")
axes[1, 1].set_ylabel("GC Content (%)")

plt.tight_layout()
plt.savefig("Combined_Figure_2x2.png", dpi=300)
plt.close()

print("✅ All individual and combined figures generated successfully.")

