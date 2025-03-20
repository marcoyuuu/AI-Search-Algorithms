"""
src package

This package serves as the root for multiple AI-related modules, including:
- `berkeley_ai` : Search algorithms adapted from the UC Berkeley AI Repository.
- `missionaries_and_cannibals` : Implementation of the classic AI problem.
- `shortest_path` : Custom search problems involving polygonal environments.

Modules:
--------
Each subpackage contains specialized implementations of AI-related problems and algorithms.

Usage:
------
Import specific submodules as needed:

    from src.berkeley_ai import breadth_first_graph_search
    from src.shortest_path.figure_3_31_env import build_figure_3_31_env
    from src.missionaries_and_cannibals.Exercise3_9 import solve_missionaries_and_cannibals

"""

# Ensure submodules are accessible
from . import berkeley_ai
from . import missionaries_and_cannibals
from . import shortest_path
from . import notebook
from . import visualizations
