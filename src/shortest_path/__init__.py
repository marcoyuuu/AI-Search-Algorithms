"""
shortest_path package

This package defines a custom state-space environment (based on Figure 3.31)
and provides modules for:
  - Building the environment (figure_3_31_env)
  - Geometry utilities (geometry)
  - Defining search problems (search_problem)
  - Representing the state space (state_space)
  - Running search algorithms with visualizations (main)

Usage Example:
    from shortest_path import build_figure_3_31_env, ConvexPolygonPathProblem, run_searches

    env = build_figure_3_31_env()
    problem = ConvexPolygonPathProblem("S", "G", env)
    results = run_searches(problem)
    # ... further processing ...
"""

from .figure_3_31_env import build_figure_3_31_env
from .geometry import segments_intersect, point_in_polygon, sample_line, line_clear
from .search_problem import ConvexPolygonPathProblem, run_searches
from .state_space import StateSpace, Vertex
