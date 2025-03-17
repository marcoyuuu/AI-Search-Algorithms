"""
search_problem.py

PEP 8–compliant module defining the ConvexPolygonPathProblem,
which extends the Berkeley 'Problem' class to handle:
 - BFS
 - DFS
 - UCS
 - A*

We import BFS, DFS, UCS, A* from the local berkeley_ai.search module.
"""

import math
from berkeley_ai.search import Problem, breadth_first_graph_search, depth_first_graph_search
from berkeley_ai.search import uniform_cost_search, astar_search

class ConvexPolygonPathProblem(Problem):
    """
    A search problem for the figure_3_31_env-based environment.
    States are vertex names (strings).
    Actions are the neighbor vertex names from 'reachable'.
    """

    def __init__(self, initial, goal, state_space):
        super().__init__(initial, goal)
        self.state_space = state_space

    def actions(self, state):
        """
        Return list of reachable vertex names from the given 'state'.
        """
        return list(self.state_space.vertices[state].reachable.values())

    def result(self, state, action):
        """
        The new state is simply the action, which is a neighbor's name.
        """
        return action

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """
        Euclidean distance between state1 and state2, plus current cost.
        """
        (x1, y1) = self.state_space.vertices[state1].location
        (x2, y2) = self.state_space.vertices[state2].location
        return c + math.hypot(x2 - x1, y2 - y1)

    def h(self, node):
        """
        Straight-line distance to the goal, for A*.
        """
        if hasattr(node, 'state'):
            s = node.state
        else:
            s = node
        (x1, y1) = self.state_space.vertices[s].location
        (xg, yg) = self.state_space.goal.location
        return math.hypot(xg - x1, yg - y1)


def run_searches(problem):
    """
    Execute BFS, DFS, UCS, and A* on the given problem.
    Return a dictionary of results: { 'BFS': (solution, cost), ... }
    """
    results = {}

    # BFS
    bfs_node = breadth_first_graph_search(problem)
    if bfs_node:
        path_bfs = [n.state for n in bfs_node.path()]
        results['BFS'] = (path_bfs, bfs_node.path_cost)
    else:
        results['BFS'] = (None, None)

    # DFS
    dfs_node = depth_first_graph_search(problem)
    if dfs_node:
        path_dfs = [n.state for n in dfs_node.path()]
        results['DFS'] = (path_dfs, dfs_node.path_cost)
    else:
        results['DFS'] = (None, None)

    # UCS
    ucs_node = uniform_cost_search(problem)
    if ucs_node:
        path_ucs = [n.state for n in ucs_node.path()]
        results['UCS'] = (path_ucs, ucs_node.path_cost)
    else:
        results['UCS'] = (None, None)

    # A*
    astar_node = astar_search(problem, problem.h)
    if astar_node:
        path_astar = [n.state for n in astar_node.path()]
        results['A*'] = (path_astar, astar_node.path_cost)
    else:
        results['A*'] = (None, None)

    return results
