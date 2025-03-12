import pandas as pd
import random
import matplotlib.pyplot as plt
from shapely.geometry import box

# Define furniture dimensions (Width, Height)
FURNITURE = {
    "Bed": (6, 7),
    "Sofa": (6, 3),
    "Table": (3, 3),
    "Chair": (2, 2),
    "Cupboard": (4, 2),
    "TV_Unit": (5, 1)  # Ensure 'TV_Unit' exists
}

# Room dimensions
ROOM_WIDTH = 30
ROOM_HEIGHT = 30

# Function to generate synthetic dataset
def generate_dataset(num_samples=100):
    data = []
    for _ in range(num_samples):
        sample = {}
        for item in FURNITURE.keys():
            sample[f"{item}_X"] = random.randint(0, ROOM_WIDTH - FURNITURE[item][0])
            sample[f"{item}_Y"] = random.randint(0, ROOM_HEIGHT - FURNITURE[item][1])
        data.append(sample)

    df = pd.DataFrame(data)
    df.to_csv("furniture_dataset.csv", index=False)
    print("Dataset generated and saved as 'furniture_dataset.csv'.")

# Fitness function to evaluate layouts
def fitness_function(layout):
    objects = []
    for key in layout.keys():
        if key.endswith("_X"):
            name = key.split("_X")[0]

            # Fix 'TV' key issue by renaming
            if name == "TV":
                name = "TV_Unit"

            if name in FURNITURE:
                x, y = layout[key], layout[f"{name}_Y"]
                w, h = FURNITURE[name]
                objects.append(box(x, y, x + w, y + h))

    # Calculate overlap penalty
    overlap_penalty = sum([a.intersection(b).area for i, a in enumerate(objects) for j, b in enumerate(objects) if i < j])
    return -overlap_penalty  # Lower overlap is better

# Generate dataset
generate_dataset()

# Load dataset
df = pd.read_csv("furniture_dataset.csv")

# Find best layout
best_layout = max(df.to_dict("records"), key=fitness_function)

# Visualization
def visualize_layout(layout):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, ROOM_WIDTH)
    ax.set_ylim(0, ROOM_HEIGHT)

    # Draw room boundary
    ax.plot([0, ROOM_WIDTH, ROOM_WIDTH, 0, 0], [0, 0, ROOM_HEIGHT, ROOM_HEIGHT, 0], 'k-')

    # Draw furniture
    for name, (w, h) in FURNITURE.items():
        x, y = layout.get(f"{name}_X", 0), layout.get(f"{name}_Y", 0)
        ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor='b', facecolor='c', alpha=0.5))
        ax.text(x + w / 2, y + h / 2, name, ha='center', va='center', fontsize=10, color='black')

    plt.title("Optimized Furniture Layout")
    plt.grid(True)
    plt.show()

# Show the best layout
visualize_layout(best_layout)
