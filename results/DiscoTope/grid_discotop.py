import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# =========================
# PATHS (WSL-safe)
# =========================
BASE_DIR = r"/mnt/c/Users/MHC V(D)J/EBV/DiscoTope"
OUT_DIR  = r"/mnt/c/Users/MHC V(D)J/EBV/DiscoTope/summary_figures"

os.makedirs(OUT_DIR, exist_ok=True)

# =========================
# SUBFOLDERS (16 total)
# =========================
subfolders = [
    "vaccine1", "vaccine2", "vaccine3", "vaccine4",
    "vaccine5", "vaccine6", "vaccine7", "vaccine8",
    "vaccine9", "vaccine10", "vaccine11", "vaccine12",
    "vaccine13", "vaccine14", "vaccine15", "vaccine16"
]

letters = list("ABCDEFGHIJKLMNOP")

# =========================
# HELPER FUNCTION
# =========================
def plot_grid(subset, fig_title, grid_shape, start_letter_idx, outfile):
    rows, cols = grid_shape
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 6, rows * 4))
    fig.suptitle(fig_title, fontsize=16)

    axes = axes.flatten()

    for i, folder in enumerate(subset):
        img_path = os.path.join(BASE_DIR, folder, "chart.png")

        if os.path.exists(img_path):
            img = mpimg.imread(img_path)
            axes[i].imshow(img)
            axes[i].axis("off")
            axes[i].set_title(
                f"{letters[start_letter_idx + i]} – {folder}",
                fontsize=11
            )
        else:
            axes[i].axis("off")

    # Turn off unused axes
    for j in range(len(subset), len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    fig.subplots_adjust(top=0.92)
    fig.savefig(outfile, dpi=300, bbox_inches="tight")
    plt.close(fig)


# =========================
# FIGURE 1: Proteins 1–6
# =========================
plot_grid(
    subset=subfolders[0:6],
    fig_title="Proteins 1–6",
    grid_shape=(3, 2),
    start_letter_idx=0,
    outfile=os.path.join(OUT_DIR, "Proteins_1_to_6.png")
)

# =========================
# FIGURE 2: Proteins 7–12
# =========================
plot_grid(
    subset=subfolders[6:12],
    fig_title="Proteins 7–12",
    grid_shape=(3, 2),
    start_letter_idx=6,
    outfile=os.path.join(OUT_DIR, "Proteins_7_to_12.png")
)

# =========================
# FIGURE 3: Proteins 13–16
# =========================
plot_grid(
    subset=subfolders[12:16],
    fig_title="Proteins 13–16",
    grid_shape=(2, 2),
    start_letter_idx=12,
    outfile=os.path.join(OUT_DIR, "Proteins_13_to_16.png")
)

print("✅ All grids generated and saved successfully.")

