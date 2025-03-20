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

This project implements and analyzes state-space search algorithms to solve **Problems 3.7 and 3.9** from *Artificial Intelligence: A Modern Approach (3rd Edition)*. The focus is on:  

- **Uninformed Search:** Implementations of **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Uniform Cost Search (UCS)**.  
- **Informed Search:** Implementation of **A\*** search using a Euclidean heuristic for optimal pathfinding.  
- **Graph Search vs. Tree Search:** Comparative analysis of search efficiency, memory usage, and optimality across different problem formulations.  
- **State-Space Representation & Complexity:** Exploration of state-space sizes, constraints, and practical optimizations for complex search problems.  

### **Problem 3.7 - Shortest Path with Convex Polygonal Obstacles**  
- Implements **custom state-space modeling** for **Figure 3.31**, using **polygonal environments** and **straight-line visibility graphs** to determine valid movement paths.  
- **Search Algorithms Applied:** BFS, DFS, UCS, and A* on a manually defined state space, ensuring feasibility and efficiency in navigation.  

### **Problem 3.9 - Missionaries and Cannibals Problem**  
- Models and solves the classic **Missionaries and Cannibals** problem using **state-space search** with BFS, DFS, and A*.  
- Ensures **valid state transitions** (preventing cannibals from outnumbering missionaries at any point) while **finding optimal solutions**.  
- Uses **graph visualization tools** to analyze the structure and complexity of the problem’s search space.  

### **Visualization & Experimentation**  
The project includes **advanced visualization tools** to generate and display:  
✔ **State transition graphs** for both problems.  
✔ **Search progress visualization**, allowing step-by-step inspection of explored nodes.  
✔ **Custom search problem visualizations** using **Matplotlib** and **NetworkX**.  


### **Jupyter Notebook** 
- Detailed experimental analysis, performance evaluations, and solution insights.  

---

## Project Presentation 🎥  

A detailed video presentation covering the **AI Search Algorithms** project, including its implementation, results, and key takeaways, is available here:

🔗 **Direct Link:** [https://youtu.be/UsZU4QsXNiE?feature=shared](https://youtu.be/UsZU4QsXNiE?feature=shared)

---

## Repository Structure

```
AI-Search-Algorithms/
│
├── README.md                      # Project overview, setup instructions, and documentation
├── LICENSE                         # License information
├── requirements.txt                # List of required Python packages
│
├── problem/                        # Describes problems 3.7 and 3.9 from the textbook
│
├── images/                         # Image assets used in reports and presentations
│
├── presentations/                  # Presentation materials for the project
│   └── video_link.txt              # Link to the recorded presentation or demonstration
│
├── src/                            # Source code implementation
│   ├── __init__.py                 # Makes `src` a Python package
│   │
│   ├── berkeley_ai/                # UC Berkeley AI search algorithms (reference implementation)
│   │   ├── __init__.py             
│   │   ├── search.py               # Implementation of BFS, DFS, UCS, A*, etc.
│   │   └── utils.py                # Helper functions for search algorithms
│   │
│   ├── missionaries_and_cannibals/  # Implementation of the Missionaries and Cannibals problem
│   │   ├── __init__.py             
│   │   └── main.py                  # Main execution script for Problem 3.9
│   │
│   ├── notebook/                    # Jupyter Notebook containing analysis and results
│   │   └── AI_Search_Report.ipynb   # Report on search algorithms and experimental findings
│   │
│   ├── shortest_path/               # Custom shortest path search implementation (Problem 3.7)
│   │   ├── __init__.py             
│   │   ├── figure_3_31_env.py       # Defines environment for Figure 3.31
│   │   ├── geometry.py              # Geometric utilities for intersection and path validation
│   │   ├── main.py                  # Main execution script; runs search algorithms and visualizations
│   │   ├── search_problem.py        # ConvexPolygonPathProblem class and search wrappers
│   │   └── state_space.py           # Defines state space and polygon connectivity
│   │
│   └── visualizations/              # Folder containing generated search visualizations
│
└── tests/                           # Unit tests for search algorithm correctness
    ├── __init__.py                 
    └── test_search.py               # Unit tests for BFS, DFS, UCS, and A*
```

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher  
- Jupyter Notebook  
- Required Libraries: `numpy`, `matplotlib`, `networkx`, `shapely`

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

### Running in Jupyter Notebook  

The project includes a **Jupyter Notebook** (`AI_Search_Report.ipynb`) for interactive execution, analysis, and visualization. This notebook:  
✔ Loads and runs search algorithms directly in an interactive environment.  
✔ Visualizes state-space graphs without saving them as image files.  
✔ Allows step-by-step debugging and modification of search parameters.  

To open the notebook:  
```bash
cd src/notebook
jupyter notebook AI_Search_Report.ipynb
```
Ensure that all modules are correctly imported by verifying that the **`src`** directory is recognized as a package.

---

### Running from the Command Line  

#### **Running Search Problems as Modules**  
To execute the **Shortest Path (Exercise 3.7)** and **Missionaries and Cannibals (Exercise 3.9)** problems directly from the command line, use Python’s `-m` flag to treat the directories as modules:  

- **Shortest Path (Exercise 3.7):**  
  ```bash
  cd src
  python -m shortest_path.main
  ```  
  This runs the search algorithms on the **polygonal environment** (Figure 3.31), displaying the results in the terminal and **visualizing state transitions interactively**.

- **Missionaries and Cannibals (Exercise 3.9):**  
  ```bash
  cd src
  python -m missionaries_and_cannibals.main
  ```  
  This runs the **Missionaries and Cannibals** problem using BFS, DFS, and A* algorithms, ensuring valid state transitions and solving the problem optimally.

---

### Expected Output  

Each script will:  
- **Display search progress and results** in the console.  
- **Generate interactive visualizations** of the state-space search process (Jupyter Notebook only).  
- **Provide insights into algorithm efficiency** (e.g., number of expanded nodes, path cost, and optimality).  

These execution methods ensure **cross-compatibility** between Jupyter Notebook and standalone Python scripts.

---

## **Performance Evaluation & Analysis**  

Each algorithm was evaluated based on fundamental search performance metrics:  

- **Time Complexity:** The number of nodes expanded before reaching the goal.  
- **Space Complexity:** The amount of memory required to store explored states and frontiers.  
- **Optimality:** Whether the algorithm finds the shortest possible path to the goal.  

### **Analysis of Shortest Path Problem (Exercise 3.7)**  

#### **1. BFS (Breadth-First Search)**  
- **Path Found:** `['S', 'rec1', 'rec4', 'hex1', 'hex6', 'G']`  
- **Path Cost:** ~13.59  

📌 **Key Observations:**  
- BFS explores level-by-level and guarantees the shortest path in terms of the number of steps.  
- However, BFS does **not** consider **actual travel distance**, leading to a **suboptimal path**.  

#### **2. DFS (Depth-First Search)**  
- **Path Found:** `['S', 'pent3', 'pent4', 'quad3', 'quad_2_3', 'G']`  
- **Path Cost:** ~12.69  

📌 **Key Observations:**  
- DFS searches deeply before backtracking, which may lead to a long, inefficient solution.  
- While DFS found a lower-cost path than BFS in this case, it **does not guarantee optimality**.  

#### **3. UCS (Uniform Cost Search)**  
- **Path Found:** `['S', 'rec2', 'pent1', 'tri2', 'quad2', 'quad3', 'quad_2_3', 'G']`  
- **Path Cost:** ~11.14  

📌 **Key Observations:**  
- UCS expands nodes **based on cumulative cost**, ensuring it finds the optimal path.  
- It found a **shorter** and **more efficient** solution than BFS and DFS.  

#### **4. A* Search**  
- **Path Found:** `['S', 'rec2', 'pent1', 'tri2', 'quad2', 'quad3', 'quad_2_3', 'G']`  
- **Path Cost:** ~11.14  

📌 **Key Observations:**  
- A* combines **cost-so-far (like UCS)** and an **informed heuristic** to guide exploration.  
- Under a **consistent and admissible heuristic**, A* finds the **same optimal path as UCS** but explores fewer nodes.  

### **Comparative Analysis of Search Algorithms (Exercise 3.7)**  

| Algorithm | Path Cost | Optimal? | Comments |
|-----------|----------|----------|----------|
| **BFS**   | 13.59    | ❌ No   | Finds the shortest step-based path but not the most cost-efficient. |
| **DFS**   | 12.69    | ❌ No   | Prone to deep exploration, may stumble upon a better path by chance but does not guarantee optimality. |
| **UCS**   | 11.14    | ✅ Yes  | Expands paths based on true cost, ensuring the shortest possible travel distance. |
| **A\***    | 11.14    | ✅ Yes  | Uses heuristics to focus on optimal paths, often outperforming UCS in efficiency. |

🔹 **Conclusion:** UCS and A* successfully found the **optimal** path, while BFS and DFS produced longer, **suboptimal** routes.  

---

### **Analysis of Missionaries and Cannibals Problem (Exercise 3.9)**  

#### **Problem Summary:**  
- There are **3 missionaries** and **3 cannibals** on the left bank of a river.  
- A **boat** (capacity: 2) must transport them to the right bank.  
- The number of **cannibals can never exceed missionaries** on either bank.  
- The **goal state** is `(0,0,0)`, where everyone has safely crossed.  

#### **1. BFS (Breadth-First Search)**  
- **Solution Length:** **11 moves**  
- **Characteristics:**  
  - BFS guarantees the shortest number of moves.  
  - It explores all possible actions level-by-level.  
  - It efficiently finds the **minimal** number of crossings needed.  

#### **2. DFS (Depth-First Search)**  
- **Solution Length:** **11 moves**  
- **Characteristics:**  
  - DFS follows a depth-first strategy and may take suboptimal routes.  
  - In this case, it found a valid 11-move solution, but its exact route differs from BFS.  

#### **3. A* Search**  
- **Solution Length:** **11 moves**  
- **Heuristic:** Sum of remaining people on the left bank (`m + c`).  
- **Characteristics:**  
  - A* uses a heuristic to **prioritize better crossings**.  
  - It finds an **optimal solution matching BFS**, confirming the heuristic guides the search efficiently.  

### **Comparative Analysis of Search Algorithms (Exercise 3.9)**  

| Algorithm | Solution Length | Optimal? | Comments |
|-----------|----------------|----------|----------|
| **BFS**   | 11 moves       | ✅ Yes  | Guarantees the fewest steps needed to reach the goal. |
| **DFS**   | 11 moves       | ❌ No   | Not guaranteed to be optimal; found a valid solution but may take unnecessary detours. |
| **A\***    | 11 moves       | ✅ Yes  | Uses a heuristic to guide the search efficiently, leading to an optimal solution. |

🔹 **Conclusion:**  
- **BFS and A\*** find the **same optimal solution** in this case.  
- **DFS also finds a valid solution but does not guarantee minimal crossings.**  
- **A\*** demonstrates that **a well-designed heuristic** effectively guides search toward an optimal solution.  

---

## **Challenges, Lessons Learned & Future Work**  

### **Challenges Encountered**  
- Efficient handling of **cyclic paths and negative weights** was crucial for shortest-path problems.  
- Balancing **manual vs. automated** connectivity in state-space graphs required careful design.  
- The **state explosion problem** made BFS/DFS inefficient in large search spaces.  

### **Lessons Learned**  
- **State-space representation** significantly impacts search efficiency.  
- **Graph search** is vastly superior to naive tree search.  
- **Heuristics in A\*** dramatically improve efficiency when properly designed.  

### **Future Work**  
- **Enhancing heuristics** for A* to optimize performance in more complex environments.  
- **Implementing bidirectional search** to accelerate convergence.  
- **Hybrid search methods** that combine BFS/UCS/A* for more advanced problem-solving.  
- **Handling dynamic environments** where obstacles and path costs change over time.  

🔹 **Real-World Applications:** These insights apply to AI-driven **path planning, robotics, and optimization** problems.  

---

## **Final Takeaways**  
✅ **BFS and A\*** performed best in structured state spaces.  
❌ **DFS** lacked guaranteed optimality and could lead to inefficient solutions.  
⭐ **UCS and A\*** consistently found the best solutions in path-planning problems.  
🎯 **Well-designed heuristics** dramatically **reduce computational effort** while maintaining optimality.

## References & Citations

- **Textbook:**  
  Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3rd Edition).
- **Code Base:**  
  UC Berkeley AI Repository – [https://github.com/aimacode/aima-python](https://github.com/aimacode/aima-python)