"""
main.py

PEP 8–compliant main execution script:
 1. Builds the figure_3_31_env environment.
 2. Creates a ConvexPolygonPathProblem.
 3. Runs BFS, DFS, UCS, A* searches.
 4. Displays and saves visualizations for:
    - Initial state space
    - BFS solution
    - DFS solution
    - UCS solution
    - A* solution

Usage:
    python main.py
"""

import os
import matplotlib.pyplot as plt

from .figure_3_31_env import build_figure_3_31_env
from .search_problem import ConvexPolygonPathProblem, run_searches


def ensure_visualizations_folder():
    """Ensure that a 'visualizations' folder exists in the project root."""
    folder = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
        "visualizations"
    )
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


def visualize_solution(env, solution_path, title="Solution Path",
                       filename="solution_path.png", show=True):
    """
    Overlays the solution path on the state space and both displays and saves the figure.

    Args:
        env: The state space environment.
        solution_path: List of vertex names representing the solution.
        title: Plot title.
        filename: Descriptive filename for saving the figure.
        show: Boolean; if True, displays the figure on screen.
    """
    fig, ax = plt.subplots()

    # Draw polygon edges in black
    for edge in env.polygon_edges:
        x_vals, y_vals = edge
        ax.plot([x_vals[0], x_vals[1]], [y_vals[0], y_vals[1]],
                color="black", linewidth=2)

    # Draw auto edges in dashed gray
    for edge in env.auto_edges:
        x_vals, y_vals = edge
        ax.plot([x_vals[0], x_vals[1]], [y_vals[0], y_vals[1]],
                color="gray", linestyle="--", linewidth=1)

    # Draw minimal labels for polygons
    for poly_info in env.polygons:
        verts = poly_info['vertices']
        label = poly_info['label']
        if not verts or not label:
            continue
        xs = [env.vertices[v].location[0] for v in verts]
        ys = [env.vertices[v].location[1] for v in verts]
        cx = sum(xs) / len(xs)
        cy = sum(ys) / len(ys)
        ax.text(cx, cy, label, fontsize=10, color="black", fontweight="bold",
                horizontalalignment='center', verticalalignment='center')

    # Draw vertices as blue dots
    for v in env.vertices.values():
        ax.plot(v.location[0], v.location[1], "bo", markersize=4)

    # Mark start and goal
    if env.start:
        ax.plot(env.start.location[0], env.start.location[1],
                "go", markersize=8, label="Start")
    if env.goal:
        ax.plot(env.goal.location[0], env.goal.location[1],
                "ro", markersize=8, label="Goal")

    # Draw the solution path in red
    if solution_path:
        coords = [env.vertices[n].location for n in solution_path]
        xs = [pt[0] for pt in coords]
        ys = [pt[1] for pt in coords]
        ax.plot(xs, ys, "r-", linewidth=3, label="Solution")

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.legend()

    # Save figure
    folder = ensure_visualizations_folder()
    filepath = os.path.join(folder, filename)
    plt.savefig(filepath, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close()
    print(f"Visualization saved as: {filepath}")


def draw_environment(env, filename="figure_3_31_state_space.png", show=True):
    """
    Draws the state space environment and both displays and saves the figure.

    Args:
        env: The state space environment.
        filename: Descriptive filename for the saved figure.
        show: Boolean; if True, displays the figure on screen.
    """
    fig, ax = plt.subplots()

    # Draw polygon edges in black
    for edge in env.polygon_edges:
        x_vals, y_vals = edge
        ax.plot([x_vals[0], x_vals[1]], [y_vals[0], y_vals[1]],
                color="black", linewidth=2)

    # Draw auto edges in dashed gray
    for edge in env.auto_edges:
        x_vals, y_vals = edge
        ax.plot([x_vals[0], x_vals[1]], [y_vals[0], y_vals[1]],
                color="gray", linestyle="--", linewidth=1)

    # Draw vertices as blue dots
    for v in env.vertices.values():
        ax.plot(v.location[0], v.location[1], "bo", markersize=4)

    # Mark start and goal
    if env.start:
        ax.plot(env.start.location[0], env.start.location[1],
                "go", markersize=8, label="Start")
    if env.goal:
        ax.plot(env.goal.location[0], env.goal.location[1],
                "ro", markersize=8, label="Goal")

    ax.set_title("State Space Environment")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.legend()

    folder = ensure_visualizations_folder()
    filepath = os.path.join(folder, filename)
    plt.savefig(filepath, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close()
    print(f"State space visualization saved as: {filepath}")


def main():
    # 1) Build the environment from figure_3_31
    env = build_figure_3_31_env()

    # 2) Create the search problem
    problem = ConvexPolygonPathProblem("S", "G", env)

    # 3) Draw and save the initial state space
    draw_environment(env, filename="figure_3_31_state_space.png", show=True)

    # 4) Run BFS, DFS, UCS, A*
    results = run_searches(problem)

    # 5) For each algorithm, print and visualize the solution
    for algo in ["BFS", "DFS", "UCS", "A*"]:
        path, cost = results[algo]
        print(f"=== {algo} ===")
        if path:
            print("Solution Path:", path)
            print("Path Cost:", cost)

            # Replace invalid filename chars, e.g., '*' -> 'star'
            safe_algo_name = algo.replace('*', 'star').lower()
            filename = f"{safe_algo_name}_solution.png"

            visualize_solution(
                env, path,
                title=f"{algo} Search Solution",
                filename=filename,
                show=True
            )
        else:
            print("No solution found.")
        print("-" * 40)


if __name__ == "__main__":
    main()
