# University of Puerto Rico at Mayagüez  
### Department of Electrical and Computer Engineering  
#### ICOM5015 - Artificial Intelligence

**Project Title:** AI Search Algorithms & Negative Step Costs  
**Assignment:** Programming Homework – Chapter 3 (Problems 3.7 & 3.9)  

**Team:** Group M  
- **Marco Yu** (Undergraduate, Computer Science)  
- **Samir Rivera** (Undergraduate, Software Engineering)  
- **Lex Feliciano** (Undergraduate, Electrical and Computer Engineering)  
- **Shadiel López** (Undergraduate, Computer Engineering)  

**Professor:** J. Fernando Vega Riveros  
**Date:** March 19, 2025  

<p align="center">
  <img src="https://www.uprm.edu/wdt/resources/seal-rum-uprm-1280x1280px.png" alt="UPRM Logo" width="250" height="250">
</p>

---

## Overview & Purpose

This project implements and analyzes state-space search algorithms to solve Problems 3.7 and 3.9 from *Artificial Intelligence: A Modern Approach (3rd Edition)*. The focus is on:

- **Uninformed Search:** Implementations of Breadth-First Search (BFS), Depth-First Search (DFS), and Uniform Cost Search (UCS).
- **Informed Search:** The A* search algorithm using a Euclidean heuristic.
- **Graph Search vs. Tree Search:** Evaluating efficiency and optimality when exploring different problem instances.
- **Handling Negative Step Costs:** Addressing challenges posed by negative weights using the Bellman-Ford and Johnson’s algorithms (adapted from the UC Berkeley AI Repository).

Additionally, the project features a custom environment that replicates Figure 3.31 using a manually defined state space based on polygons. Advanced visualization routines are included to both display and save figures (with descriptive filenames) to a designated folder.

For further analysis, the project also includes a Jupyter Notebook and written reports that cover detailed experimental results and problem analyses.

---

## Repository Structure

```
AI-Search-Algorithms/
│
├── codebase.txt                 # Overview of the project’s file structure
├── llmify_config.yaml           # Configuration to ignore specific files and directories (e.g., docs, .git, __pycache__, etc.)
├── README.md                    # This file: project overview and documentation (updated)
├── requirements.txt             # Required Python packages (numpy, matplotlib, networkx, shapely)
│
├── notebooks/                   # Jupyter Notebooks for analysis and reporting
│   └── AI_Search_Report.ipynb   # Detailed report on search algorithms and experiments
│
├── presentations/               # Presentation materials for the assignment
│   ├── slides.pptx              # PowerPoint slides
│   └── video_link.txt           # Link to the video submission
│
├── reports/                     # Written reports and analysis documents
│   ├── experiment_results.md    # Performance evaluation of search methods
│   └── problem_analysis.md      # Detailed breakdown of Problems 3.7 & 3.9
│
├── src/                         # Source code
│   ├── berkeley_ai/             # UC Berkeley search code (unaltered)
│   │   ├── search.py            # Search algorithms (BFS, DFS, UCS, A*, etc.)
│   │   └── utils.py             # Utility functions for search algorithms
│   │
│   ├── missionaries_and_cannibals/   # Missionaries and Cannibals problem implementation (Problem 3.9 example)
│   │   └── Exercise3.9.py
│   │
│   └── shortest_path/           # Custom environment and search problem modules
│       ├── geometry.py          # Geometry utilities (intersection, point-in-polygon, etc.)
│       ├── state_space.py       # StateSpace and Vertex classes (environment definition, polygon connections, and drawing with labels)
│       ├── figure_3_31_env.py   # Builds the Figure 3.31 environment with manual connectivity
│       ├── search_problem.py    # Definition of ConvexPolygonPathProblem and search wrapper functions (BFS, DFS, UCS, A*)
│       └── main.py              # Main execution script; builds the environment, runs searches, and visualizes results
│
└── tests/                       # Unit tests for verifying search algorithm correctness
    └── test_search.py
```

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher  
- Jupyter Notebook  
- Required Libraries: `numpy`, `matplotlib`, `networkx`, `shapely`, `heapq`

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/YOUR_USERNAME/AI-Search-Algorithms.git
    cd AI-Search-Algorithms
    ```
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## Running the Code

### Running Individual Algorithms

- **Shortest Path (Exercise 3.7):**  
  Navigate to the shortest_path directory and run:
  ```bash
  cd src/shortest_path
  python main.py
  ```

- **Missionaries and Cannibals (Exercise 3.9):**  
  Navigate to the missionaries and cannibals directory and run:
  ```bash
  cd src/missionaries_and_cannibals
  python Exercise3.9.py
  ```

### Running the Main Environment & Visualizations

The main script builds the custom Figure 3.31 environment, runs BFS, DFS, UCS, and A* searches, and displays & saves visualizations.

To run the main script from the `src/shortest_path` directory:
```bash
python main.py
```
This will:
- Display the initial state space (with polygon labels).
- Execute all search algorithms.
- Show each solution path on screen.
- Save each visualization in the `visualizations/` folder with descriptive filenames (e.g., `bfs_solution.png`, `dfs_solution.png`, etc.).

---

## Performance Evaluation & Analysis

Each algorithm is evaluated based on:
- **Time Complexity:** Number of node expansions.
- **Space Complexity:** Memory usage for frontiers/explored sets.
- **Optimality:** Whether the algorithm finds the shortest path.

In our experiments:
- **BFS and DFS** may return longer, suboptimal paths.
- **UCS and A\*** (using the Euclidean heuristic) typically return the optimal path.

Detailed performance and experiment analyses can be found in the `notebooks/` and `reports/` folders.

---

## Challenges, Lessons Learned & Future Work

### Challenges Encountered
- Efficiently handling cycles and negative weights.
- Balancing manual versus automated connectivity in the state space.

### Lessons Learned
- A clear and robust state-space representation is crucial for effective search.
- Graph search techniques significantly improve efficiency over tree search.
- Negative costs require specialized algorithms like Bellman-Ford and Johnson’s for proper handling.

### Future Work
- Improve A* algorithm heuristics to further optimize performance.
- Implement bidirectional search to accelerate convergence.
- Explore hybrid methods combining multiple search strategies for more complex problems.

---

## References & Citations

- **Textbook:**  
  Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3rd Edition).
- **Code Base:**  
  UC Berkeley AI Repository – [https://github.com/aimacode/aima-python](https://github.com/aimacode/aima-python)
- **Algorithms:**  
  - Bellman-Ford: [Wikipedia](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm)  
  - Johnson’s Algorithm: [Wikipedia](https://en.wikipedia.org/wiki/Johnson%27s_algorithm)

---

## Conclusion

This project successfully implements and compares various search algorithms for AI. The custom state space (Figure 3.31) with polygon labels has been rigorously constructed and visualized. Experiments show that while BFS and DFS are straightforward, UCS and A* provide more optimal solutions by effectively incorporating cost and heuristic information. The inclusion of the Missionaries and Cannibals problem further demonstrates practical problem solving using these search strategies.