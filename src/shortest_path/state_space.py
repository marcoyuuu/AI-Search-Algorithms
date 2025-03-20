"""
state_space.py

Defines the Vertex and StateSpace classes for representing the environment
(replicating Figure 3.31). The StateSpace class includes methods for adding
vertices, connecting polygons, manually asserting reachability, and an enhanced
draw() method that displays the environment with polygon labels (one per shape).

PEP 8–compliant and documented.
"""

import itertools
import math
import os
import matplotlib.pyplot as plt

from .geometry import segments_intersect, line_clear, point_in_polygon


class Vertex:
    """
    Represents a vertex in the environment.

    Attributes:
        location (tuple): Coordinates (x, y) of the vertex.
        name (str): Unique identifier for the vertex.
        reachable (dict): Maps move vectors (dx, dy) to neighbor vertex names.
        edges (list): List of neighbor vertex names connected by polygon edges.
    """

    def __init__(self, x, y, name):
        self.location = (x, y)
        self.name = name
        self.reachable = {}  # {(dx, dy): neighbor_name}
        self.edges = []      # list of neighbor names (manually connected)


class StateSpace:
    """
    Represents the overall environment (state space) for the problem.

    Attributes:
        vertices (dict): Mapping of vertex names to Vertex objects.
        polygon_edges (list): List of edges (tuples) representing polygon boundaries.
        auto_edges (list): List of automatically generated edges (optional).
        polygons (list): List of polygon definitions; each is a dictionary with keys:
            'label' - a shape label, and 'vertices' - a list of vertex names.
        start (Vertex): The start vertex.
        goal (Vertex): The goal vertex.
    """

    def __init__(self):
        self.vertices = {}
        self.polygon_edges = []  # For drawing polygon edges (thick lines)
        self.auto_edges = []     # For drawing auto-discovered edges (optional)
        self.polygons = []       # List of polygons; each: {'label': str or None, 'vertices': [names]}
        self.start = None
        self.goal = None

    def add_vertex(self, x, y, name):
        """Add a vertex with coordinates (x, y) and unique name."""
        self.vertices[name] = Vertex(x, y, name)

    def set_start(self, x, y, name="S"):
        """Define the start vertex."""
        v = Vertex(x, y, name)
        self.vertices[name] = v
        self.start = v

    def set_goal(self, x, y, name="G"):
        """Define the goal vertex."""
        v = Vertex(x, y, name)
        self.vertices[name] = v
        self.goal = v

    def add_edge(self, a, b):
        """
        Connect two vertices a and b as part of a polygon.
        Records the edge for drawing and asserts mutual reachability.
        """
        self.vertices[a].edges.append(b)
        self.vertices[b].edges.append(a)

        x1, y1 = self.vertices[a].location
        x2, y2 = self.vertices[b].location
        self.polygon_edges.append(((x1, x2), (y1, y2)))
        self.assert_reachable(a, b)

    def connect_polygon(self, v_names, shape_label=None):
        """
        Connect a list of vertices in order to form a closed polygon.
        Optionally assign a shape_label to the polygon (only one label per shape).
        """
        for i in range(len(v_names) - 1):
            self.add_edge(v_names[i], v_names[i + 1])
        self.add_edge(v_names[0], v_names[-1])

        self.polygons.append({
            'label': shape_label,
            'vertices': v_names
        })

    def assert_reachable(self, a, b):
        """
        Manually assert that vertices a and b are reachable from each other.
        Updates the 'reachable' dictionaries in both vertices.
        """
        if isinstance(b, str):
            b = [b]
        for v in b:
            x1, y1 = self.vertices[a].location
            x2, y2 = self.vertices[v].location
            dx = x2 - x1
            dy = y2 - y1
            self.vertices[a].reachable[(dx, dy)] = v
            self.vertices[v].reachable[(-dx, -dy)] = a

    def build_automated_connections(self, polygons, samples=5, max_len=6.0):
        """
        Automatically build edges for any vertex pairs that are not manually connected,
        using geometry checks (line_clear).
        
        Args:
            polygons (list): List of polygons, each given as a list of vertex names.
            samples (int): Number of sample points for line clearance.
            max_len (float): Maximum allowed length for auto-added edges.
        """
        names = list(self.vertices.keys())
        # Convert each polygon into a list of coordinate tuples.
        poly_coords = []
        for poly in polygons:
            coords = [self.vertices[name].location for name in poly]
            poly_coords.append(coords)

        for a, b in itertools.combinations(names, 2):
            if any(b == nb for nb in self.vertices[a].reachable.values()):
                continue  # Skip if already manually connected.
            va = self.vertices[a].location
            vb = self.vertices[b].location
            dist = math.hypot(vb[0] - va[0], vb[1] - va[1])
            if dist > max_len:
                continue  # Skip overly long edges.
            if line_clear(va, vb, poly_coords, samples):
                self.auto_edges.append(((va[0], vb[0]), (va[1], vb[1])))
                self.assert_reachable(a, b)

    def draw(self):
        """
        Draws the state space, including:
          - Polygon edges (thick black lines)
          - Auto-discovered edges (dashed gray)
          - Vertices (blue dots)
          - Start and Goal (green and red)
          - Polygon labels: one label per polygon at its centroid.
        """
        fig, ax = plt.subplots()

        # Draw polygon edges.
        for edge in self.polygon_edges:
            x_vals, y_vals = edge
            ax.plot([x_vals[0], x_vals[1]], [y_vals[0], y_vals[1]],
                    color="black", linewidth=2)

        # Draw auto edges.
        for edge in self.auto_edges:
            x_vals, y_vals = edge
            ax.plot([x_vals[0], x_vals[1]], [y_vals[0], y_vals[1]],
                    color="gray", linestyle="--", linewidth=1)

        # Draw polygon labels (one label per polygon).
        for poly_info in self.polygons:
            verts = poly_info['vertices']
            label = poly_info['label']
            if not verts or not label:
                continue
            xs = [self.vertices[v].location[0] for v in verts]
            ys = [self.vertices[v].location[1] for v in verts]
            cx = sum(xs) / len(xs)
            cy = sum(ys) / len(ys)
            ax.text(cx, cy, label, fontsize=10, color="black", fontweight="bold",
                    horizontalalignment='center', verticalalignment='center')

        # Draw vertices (blue dots).
        for v in self.vertices.values():
            ax.plot(v.location[0], v.location[1], "bo", markersize=4)

        # Mark start and goal.
        if self.start:
            ax.plot(self.start.location[0], self.start.location[1],
                    "go", markersize=8, label="Start")
        if self.goal:
            ax.plot(self.goal.location[0], self.goal.location[1],
                    "ro", markersize=8, label="Goal")

        ax.set_title("Figure 3.31 State Space")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.grid(True)
        ax.legend()
        plt.show()


# For testing purposes, you might include a simple __main__ block.
if __name__ == "__main__":
    # (This block can be removed in production; it's here for quick testing.)
    from shortest_path.figure_3_31_env import build_figure_3_31_env
    env = build_figure_3_31_env()
    env.draw()
