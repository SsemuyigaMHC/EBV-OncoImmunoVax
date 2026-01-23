import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg

# Path to the TAP folder containing the subfolders (protein names) in WSL
base_dir = r"/mnt/c/Users/MHC V(D)J/EBV/TAP"  # Correct WSL path format

# List of subfolders (protein names)
subfolders = [
    "BZLF1", "EBNA1", "EBNA1_2", "gB", "gH", "gp42", "GP350", 
    "LMP1", "LMP1_2", "LMP2", "LMP2_2"
]

# Create two separate figures to display two grids of images

# First grid (3x2 grid for the first 6 images)
fig1, axes1 = plt.subplots(3, 2, figsize=(12, 12))  # 3x2 grid for first 6 proteins
fig1.suptitle('Proteins 1-6', fontsize=16)

# Second grid (3x2 grid for the remaining 5 images, last row contains 1)
fig2, axes2 = plt.subplots(3, 2, figsize=(12, 12))  # 3x2 grid for 5 proteins (last row has 1)
fig2.suptitle('Proteins 7-11', fontsize=16)

# Set up grid layout and letters (for the first 6)
grid_positions1 = [(i//2, i%2) for i in range(6)]
letters1 = ['A', 'B', 'C', 'D', 'E', 'F']

# Set up grid layout and letters (for the last 5)
letters2 = ['G', 'H', 'I', 'J', 'K']

# Display images for the first 6 proteins (on the first grid)
for i in range(6):
    subfolder = subfolders[i]
    image_path = os.path.join(base_dir, subfolder, 'chart.png')  # Image path

    if os.path.exists(image_path):
        img = mpimg.imread(image_path)
        row, col = grid_positions1[i]  # Get grid position for the first grid
        axes1[row, col].imshow(img)
        axes1[row, col].axis('off')
        axes1[row, col].set_title(f'{letters1[i]} - {subfolder}', fontsize=12)

# Display images for the remaining 5 proteins (on the second grid)
for i in range(6, 11):
    subfolder = subfolders[i]
    image_path = os.path.join(base_dir, subfolder, 'chart.png')  # Image path

    if os.path.exists(image_path):
        img = mpimg.imread(image_path)
        if i == 10:
            axes2[2, 1].imshow(img)  # Last protein goes into the last slot
            axes2[2, 1].axis('off')
            axes2[2, 1].set_title(f'{letters2[i-6]} - {subfolder}', fontsize=12)
        else:
            row, col = divmod(i - 6, 2)  # Get grid position for the second grid
            axes2[row, col].imshow(img)
            axes2[row, col].axis('off')
            axes2[row, col].set_title(f'{letters2[i-6]} - {subfolder}', fontsize=12)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Reduce space between subplots for both grids
fig1.subplots_adjust(hspace=0.3, wspace=0.2)  # Adjust spacing for the first grid
fig2.subplots_adjust(hspace=0.3, wspace=0.2)  # Adjust spacing for the second grid

# Save the generated grids as image files
fig1.savefig("/mnt/c/Users/MHC V(D)J/EBV/TAP/Proteins_1_to_6_closer_final.png")  # Save the first grid
fig2.savefig("/mnt/c/Users/MHC V(D)J/EBV/TAP/Proteins_7_to_11_closer_final.png")  # Save the second grid

# Inform the user
print("Grids saved as 'Proteins_1_to_6_closer_final.png' and 'Proteins_7_to_11_closer_final.png'.")

