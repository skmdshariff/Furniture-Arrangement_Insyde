import matplotlib.pyplot as plt
import random

# Define room dimensions
ROOM_WIDTH = 30
ROOM_HEIGHT = 30

# Furniture dimensions (Width, Height)
FURNITURE = {
    "Sofa": (8, 5),
    "TV_Unit": (6, 2),
    "Cupboard": (5, 6),
    "Table": (4, 4),
    "Bed": (10, 8),
    "Chair": (3, 3)
}


def place_furniture(room_type):
    layout = []

    if room_type.lower() == "hall":
        # Place sofa at extreme edge or corner
        sofa_x = 0 if random.choice([True, False]) else ROOM_WIDTH - FURNITURE["Sofa"][0]
        sofa_y = 0 if random.choice([True, False]) else ROOM_HEIGHT - FURNITURE["Sofa"][1]
        layout.append(("Sofa", sofa_x, sofa_y))

        # Place TV aligned with sofa
        tv_x = sofa_x + (FURNITURE["Sofa"][0] // 2) - (FURNITURE["TV_Unit"][0] // 2)
        tv_y = sofa_y + FURNITURE["Sofa"][1] + 1
        layout.append(("TV_Unit", tv_x, tv_y))

        # Place cupboard at any corner or edge
        cupboard_x = random.choice([0, ROOM_WIDTH - FURNITURE["Cupboard"][0]])
        cupboard_y = random.choice([0, ROOM_HEIGHT - FURNITURE["Cupboard"][1]])
        layout.append(("Cupboard", cupboard_x, cupboard_y))

        # Place table randomly
        table_x = random.randint(0, ROOM_WIDTH - FURNITURE["Table"][0])
        table_y = random.randint(0, ROOM_HEIGHT - FURNITURE["Table"][1])
        layout.append(("Table", table_x, table_y))

    elif room_type.lower() == "bedroom":
        # Place bed at any corner or attached to a wall
        bed_x = random.choice([0, ROOM_WIDTH - FURNITURE["Bed"][0]])
        bed_y = random.choice([0, ROOM_HEIGHT - FURNITURE["Bed"][1]])
        layout.append(("Bed", bed_x, bed_y))

        # Place TV aligned with bed
        tv_x = bed_x + (FURNITURE["Bed"][0] // 2) - (FURNITURE["TV_Unit"][0] // 2)
        tv_y = bed_y + FURNITURE["Bed"][1] + 1
        layout.append(("TV_Unit", tv_x, tv_y))

        # Place cupboard at any corner or edge
        cupboard_x = random.choice([0, ROOM_WIDTH - FURNITURE["Cupboard"][0]])
        cupboard_y = random.choice([0, ROOM_HEIGHT - FURNITURE["Cupboard"][1]])
        layout.append(("Cupboard", cupboard_x, cupboard_y))

        # Place chair randomly
        chair_x = random.randint(0, ROOM_WIDTH - FURNITURE["Chair"][0])
        chair_y = random.randint(0, ROOM_HEIGHT - FURNITURE["Chair"][1])
        layout.append(("Chair", chair_x, chair_y))

        # Place table randomly
        table_x = random.randint(0, ROOM_WIDTH - FURNITURE["Table"][0])
        table_y = random.randint(0, ROOM_HEIGHT - FURNITURE["Table"][1])
        layout.append(("Table", table_x, table_y))

    return layout


# Ask user for room type
room_type = input("Enter room type (Hall/Bedroom): ").strip().lower()
layout = place_furniture(room_type)

# Plot the furniture layout
plt.figure(figsize=(6, 6))
plt.xlim(0, ROOM_WIDTH)
plt.ylim(0, ROOM_HEIGHT)
plt.title("Optimized Furniture Layout")

for item, x, y in layout:
    w, h = FURNITURE[item]
    plt.gca().add_patch(plt.Rectangle((x, y), w, h, color='cyan', alpha=0.5, edgecolor='blue'))
    plt.text(x + w / 2, y + h / 2, item, fontsize=10, ha='center', va='center', color='black')

plt.grid(True)
plt.show()
