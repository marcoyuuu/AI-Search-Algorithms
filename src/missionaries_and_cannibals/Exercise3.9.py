"""
missionaries_cannibals.py

PEP 8 compliant implementation of the Missionaries and Cannibals problem using multiple search algorithms:
    - Breadth-First Search (BFS)
    - Depth-First Search (DFS)
    - A* Search

The problem:
    Three missionaries and three cannibals need to cross a river. A boat that can carry at most two people is available.
    At no point should the cannibals outnumber the missionaries on either side of the river (unless there are no missionaries).

Key Features:
    - Uses BFS, DFS, and A* to search from the initial state (3, 3, 1) to the goal state (0, 0, 0).
    - Ensures valid state transitions to avoid failure states.
    - Provides a visualization of the state-transition graph for each algorithm using NetworkX and Matplotlib.
    
States are represented as a tuple:
    (missionaries_left, cannibals_left, boat_position)
    where boat_position is 1 if on the left bank and 0 if on the right bank.
"""
  
from collections import deque
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class MissionariesAndCannibals:
    """
    Class representing the Missionaries and Cannibals problem.

    Attributes:
        initial_state (tuple): The starting state represented as (missionaries_left, cannibals_left, boat).
        goal_state (tuple): The target state where everyone has crossed to the right bank.
    """
    def __init__(self):
        # Initial state: 3 missionaries, 3 cannibals on the left bank; boat on left (1)
        self.initial_state = (3, 3, 1)
        # Goal state: All missionaries and cannibals on the right bank; boat on right (0)
        self.goal_state = (0, 0, 0)

    def is_valid(self, state):
        """
        Check whether a given state is valid.

        A state is valid if:
            - The numbers of missionaries and cannibals are within the range [0, 3].
            - On each bank, if missionaries are present then they are not outnumbered by cannibals.

        Args:
            state (tuple): A tuple (m, c, boat) representing the state.

        Returns:
            bool: True if the state is valid; False otherwise.
        """
        m, c, _ = state
        # Check numbers are within bounds
        if not (0 <= m <= 3 and 0 <= c <= 3):
            return False

        # Left bank: if there are missionaries, they must not be outnumbered by cannibals.
        if m > 0 and m < c:
            return False

        # Right bank: compute missionaries and cannibals on right bank
        m_right = 3 - m
        c_right = 3 - c
        if m_right > 0 and m_right < c_right:
            return False

        return True

    def get_successors(self, state):
        """
        Generate all valid successor states from the current state.

        Each move is represented by a tuple (m, c) indicating the number of missionaries and cannibals
        that move across the river. The boat's direction is determined by its current position.
        
        Args:
            state (tuple): The current state (missionaries_left, cannibals_left, boat).

        Returns:
            list: A list of tuples where each tuple is (new_state, action) and
                  action is a tuple (m, c) representing the move.
        """
        missionaries, cannibals, boat = state
        # Possible moves: (missionaries, cannibals)
        possible_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        successors = []

        # Boat direction: if boat == 1, it moves from left to right; if 0, right to left.
        for m_move, c_move in possible_moves:
            if boat == 1:
                new_state = (missionaries - m_move, cannibals - c_move, 0)
            else:
                new_state = (missionaries + m_move, cannibals + c_move, 1)
            if self.is_valid(new_state):
                successors.append((new_state, (m_move, c_move)))
        return successors

    def breadth_first_search(self):
        """
        Perform Breadth-First Search (BFS) to solve the problem.

        Returns:
            tuple: A tuple (solution_path, graph) where:
                   - solution_path is a list of actions (moves) leading from the initial state to the goal state.
                   - graph is a NetworkX directed graph representing the state transitions.
        """
        # Each element in the queue is a tuple: (current_state, path_taken)
        queue = deque([(self.initial_state, [])])
        visited = set()
        graph = nx.DiGraph()

        while queue:
            state, path = queue.popleft()
            if state == self.goal_state:
                return path, graph

            if state not in visited:
                visited.add(state)
                for successor, action in self.get_successors(state):
                    queue.append((successor, path + [action]))
                    graph.add_edge(state, successor, action=str(action))
        return None, graph

    def depth_first_search(self):
        """
        Perform Depth-First Search (DFS) to solve the problem.

        Returns:
            tuple: A tuple (solution_path, graph) where:
                   - solution_path is a list of actions (moves) leading from the initial state to the goal state.
                   - graph is a NetworkX directed graph representing the state transitions.
        """
        # Each element in the stack is a tuple: (current_state, path_taken)
        stack = [(self.initial_state, [])]
        visited = set()
        graph = nx.DiGraph()

        while stack:
            state, path = stack.pop()
            if state == self.goal_state:
                return path, graph

            if state not in visited:
                visited.add(state)
                for successor, action in self.get_successors(state):
                    stack.append((successor, path + [action]))
                    graph.add_edge(state, successor, action=str(action))
        return None, graph

    def a_star_search(self):
        """
        Perform A* Search to solve the problem using a simple heuristic.

        The heuristic function estimates the cost to reach the goal as the sum of
        missionaries and cannibals still on the left bank.

        Returns:
            tuple: A tuple (solution_path, graph) where:
                   - solution_path is a list of actions (moves) leading from the initial state to the goal state.
                   - graph is a NetworkX directed graph representing the state transitions.
        """
        def heuristic(state):
            # Simple heuristic: remaining number of people on the left bank
            m, c, _ = state
            return m + c

        # Priority queue elements: (priority, state, path_taken)
        priority_queue = [(heuristic(self.initial_state), self.initial_state, [])]
        visited = set()
        graph = nx.DiGraph()

        while priority_queue:
            _, state, path = heapq.heappop(priority_queue)
            if state == self.goal_state:
                return path, graph

            if state not in visited:
                visited.add(state)
                for successor, action in self.get_successors(state):
                    new_path = path + [action]
                    cost = len(new_path)  # Cost is path length (each move costs 1)
                    priority = cost + heuristic(successor)
                    heapq.heappush(priority_queue, (priority, successor, new_path))
                    graph.add_edge(state, successor, action=str(action))
        return None, graph

    def visualize_solution(self, graph, title):
        """
        Visualize the state transition graph using NetworkX and Matplotlib.

        Args:
            graph (nx.DiGraph): The state transition graph.
            title (str): The title for the plot.
        """
        plt.figure(figsize=(10, 6))
        # Generate positions using spring layout
        pos = nx.spring_layout(graph)
        # Create labels for nodes and edges
        node_labels = {node: str(node) for node in graph.nodes()}
        edge_labels = {(u, v): d['action'] for u, v, d in graph.edges(data=True)}

        nx.draw(graph, pos, with_labels=True, labels=node_labels,
                node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)
        plt.title(title)
        plt.show()


def main():
    """
    Main execution function:
        - Instantiates the MissionariesAndCannibals problem.
        - Solves it using BFS, DFS, and A*.
        - Prints the solution paths and visualizes the state transition graphs.
    """
    problem = MissionariesAndCannibals()

    # Breadth-First Search
    print("Breadth-First Search Solution:")
    bfs_solution, bfs_graph = problem.breadth_first_search()
    print("Solution Moves:", bfs_solution)
    problem.visualize_solution(bfs_graph, "BFS State Transition Graph")

    # Depth-First Search
    print("Depth-First Search Solution:")
    dfs_solution, dfs_graph = problem.depth_first_search()
    print("Solution Moves:", dfs_solution)
    problem.visualize_solution(dfs_graph, "DFS State Transition Graph")

    # A* Search
    print("A* Search Solution:")
    a_star_solution, a_star_graph = problem.a_star_search()
    print("Solution Moves:", a_star_solution)
    problem.visualize_solution(a_star_graph, "A* State Transition Graph")


if __name__ == "__main__":
    main()
