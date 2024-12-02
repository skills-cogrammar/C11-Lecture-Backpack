# Re-import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Redefine the maze
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

# Corrected solution path and facing directions with swapped left/right
solution_path_fixed = [
    (1, 1), (1, 2), (1, 3), (1, 3), 
    (2, 3), (3, 3), (3, 3), 
    (3, 4), (3, 5), (3, 5), 
    (4, 5), (5, 5), (5, 5),
    (4, 5), (3, 5), (2, 5), (1, 5)
]

facing_directions_fixed = [
    (0, 1), (0, 1), (0, 1), (1, 0), 
    (1, 0), (1, 0), (0, 1), 
    (0, 1), (0, 1), (1, 0), 
    (1, 0), (1, 0), (-1, 0)
]

# Helper function to calculate swapped direction offsets
def get_direction_offsets(facing_direction):
    return {
        "Forward": facing_direction,
        "Right": (facing_direction[1], -facing_direction[0]),  # Original Left swapped to Right
        "Left": (-facing_direction[1], facing_direction[0])   # Original Right swapped to Left
    }

# Initialize figure
maze_size = len(maze)
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, maze_size)
ax.set_ylim(0, maze_size)
ax.set_xticks(range(maze_size + 1))
ax.set_yticks(range(maze_size + 1))
ax.grid(color="gray", linestyle="--", linewidth=0.5)
ax.set_aspect('equal')
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

# Draw maze walls and path
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == 1:
            ax.add_patch(plt.Rectangle((col, maze_size - row - 1), 1, 1, color="black"))
        else:
            ax.add_patch(plt.Rectangle((col, maze_size - row - 1), 1, 1, color="white"))
ax.add_patch(plt.Rectangle((1, 5), 1, 1, color="green", label="Start"))
ax.add_patch(plt.Rectangle((5, 5), 1, 1, color="red", label="Exit"))

# Add legend
ax.legend(loc="upper right")

# Initialize agent
agent_circle = plt.Circle((solution_path_fixed[0][1] + 0.5, maze_size - solution_path_fixed[0][0] - 0.5), 0.3, color="blue")
ax.add_patch(agent_circle)

# Add text annotations for directions
text_annotations = {
    "Left": ax.text(0, 0, "", color="orange", fontsize=15, ha="center"),
    "Forward": ax.text(0, 0, "", color="orange", fontsize=15, ha="center"),
    "Right": ax.text(0, 0, "", color="orange", fontsize=15, ha="center"),
}

# Update function for animation
def update_fixed(step):
    # Update agent position
    row, col = solution_path_fixed[step]
    agent_circle.center = (col + 0.5, maze_size - row - 0.5)

    # Update direction annotations
    facing_direction = facing_directions_fixed[min(step, len(facing_directions_fixed) - 1)]
    direction_offsets = get_direction_offsets(facing_direction)

    for direction, (row_offset, col_offset) in direction_offsets.items():
        text_annotations[direction].set_position((col + 0.5 + col_offset * 0.7, maze_size - row - 0.5 - row_offset * 0.7))
        text_annotations[direction].set_text(direction)

# Create animation
ani_fixed = animation.FuncAnimation(
    fig, update_fixed, frames=len(solution_path_fixed), interval=1000, repeat=False
)

# Adjust layout and margins
plt.tight_layout(pad=0)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Save the animation as a GIF without padding
animation_filename_swap = "maze_agent_swapped_directions_output.gif"
writer = PillowWriter(fps=1)
ani_fixed.save(animation_filename_swap, writer=writer, dpi=100, savefig_kwargs={'bbox_inches': 'tight', 'pad_inches': 0})
