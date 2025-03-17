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

- **Uninformed Search:** BFS, DFS, Uniform Cost Search (UCS)
- **Informed Search:** A* (using a Euclidean heuristic)
- **Graph Search vs. Tree Search:** Evaluating efficiency and optimality
- **Handling Negative Step Costs:** Implementing Bellman-Ford and Johnson’s Algorithms for problems with negative weights (code provided from UC Berkeley’s repository)

Additionally, the project features a custom environment that replicates Figure 3.31 using a manually defined state space with polygons. Enhanced visualization routines both display and save figures (with descriptive filenames) in a designated folder.

---

## Repository Structure

```
AI-Search-Algorithms/
│
├── codebase.txt                 # Overview of the project’s file structure
├── llmify_config.yaml           # LLMify configuration to ignore specific files/directories
├── README.md                    # This file: project overview and documentation
├── requirements.txt             # Required Python packages (numpy, matplotlib, heapq)
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
- Required Libraries: `numpy`, `matplotlib`, `heapq`

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

- **BFS & DFS:**  
  ```bash
  python src/bfs_dfs.py
  ```
- **UCS & A\*:**  
  ```bash
  python src/ucs_astar.py
  ```
- **Bellman-Ford & Johnson’s Algorithm:**  
  ```bash
  python src/bellman_ford.py
  python src/johnson.py
  ```

### Running the Main Environment & Visualizations

The main script builds the custom Figure 3.31 environment, runs BFS, DFS, UCS, and A* searches, and displays & saves visualizations.

To run the main script:
```bash
# Ensure you run from the project root or set PYTHONPATH appropriately.
python -m shortest_path.main
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
- **UCS and A\*** (with the Euclidean heuristic) typically return the optimal path.

The project also contains detailed performance and experiment analyses in the `notebooks/` and `reports/` folders.

---

## Grading Criteria & Alignment

| **Criterion**                 | **How Addressed**                                                                      |
|-------------------------------|----------------------------------------------------------------------------------------|
| Problem Understanding         | Clear definitions and problem breakdowns for Problems 3.7 & 3.9                         |
| Implementation Accuracy       | Correct implementations of BFS, DFS, UCS, A*, Bellman-Ford, and Johnson’s Algorithm     |
| Experimentation               | Multiple search algorithms tested on a manually defined, realistic state space          |
| Analysis & Reporting          | Detailed performance analysis provided in notebooks and reports                         |
| Presentation Quality          | Professional code structure, comprehensive README, and clear, polished visualizations    |

---

## Challenges, Lessons Learned & Future Work

### Challenges Encountered
- Efficient handling of negative weight cycles.
- Balancing manual vs. automated connectivity in the state space.

### Lessons Learned
- A clear state-space representation is vital for robust search.
- Graph search techniques significantly improve efficiency over tree search.
- Negative costs require specialized handling (Bellman-Ford, Johnson’s Algorithm).

### Future Work
- Improve heuristics for A* to further optimize performance.
- Implement bidirectional search for faster convergence.
- Explore hybrid methods combining multiple search strategies.

---

## References & Citations

- **Textbook:**  
  Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3rd Edition).
- **Code Base:**  
  [UC Berkeley AI Repository](https://github.com/aimacode/aima-python)
- **Algorithms:**  
  - Bellman-Ford: [Wikipedia](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm)  
  - Johnson’s Algorithm: [Wikipedia](https://en.wikipedia.org/wiki/Johnson%27s_algorithm)

---

## Conclusion

This project successfully implements and compares various search algorithms for AI. The custom state space replicates Figure 3.31 and includes professional-grade visualizations that are both displayed on screen and saved for documentation. The code is modular, well-documented, and adheres to PEP 8 standards.
