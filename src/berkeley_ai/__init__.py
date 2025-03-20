"""
berkeley_ai package

This package contains implementations of fundamental AI search algorithms and 
utility functions adapted from the UC Berkeley AI Repository.

Modules:
--------
- `search.py` : Implements BFS, DFS, UCS, A*, and other search algorithms.
- `utils.py`  : Utility functions for handling search problems efficiently.

Usage:
------
Import specific algorithms or utilities as needed:

    from berkeley_ai.search import breadth_first_graph_search, astar_search
    from berkeley_ai.utils import some_utility_function

Author:
-------
UC Berkeley AI Repository (Unmodified for this project)

"""

# Import core search algorithms
from .search import (
    breadth_first_graph_search,
    depth_first_graph_search,
    uniform_cost_search,
    astar_search
)

# Import utilities
from .utils import *
