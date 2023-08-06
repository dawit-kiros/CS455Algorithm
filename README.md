# Maze Solver - Depth-First Traversal

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
1. [Introduction](#introduction)
2. [Design](#design)
   - 2.1 [Why Depth-First Traversal?](#why-depth-first-traversal)
   - 2.2 [Identifying the Problem](#identifying-the-problem)
   - 2.3 [Investigating Solutions](#investigating-solutions)
   - 2.4 [Selecting the Approach](#selecting-the-approach)
3. [Implementation](#implementation)
4. [Test](#test)
5. [Enhancement Ideas](#enhancement-ideas)
6. [Conclusion](#conclusion)
7. [Usage](#usage)
8. [License](#license)

## Introduction
The 'Maze Solver' is a Python solution to the '490. The Maze' problem on LeetCode. The goal is to find if there exists a path from a given start cell to a destination cell in a maze represented as a 2D matrix. This repository provides a Depth-First Traversal (DFS) approach to solve the problem.

## Design
### 2.1 Why Depth-First Traversal?
Depth-First Traversal is chosen due to its effectiveness in exploring all possible paths in the maze until the destination is reached or all options are exhausted. It is suitable for maze-solving problems where backtracking is required to explore alternative directions.

### 2.2 Identifying the Problem
The maze is represented as a 2D matrix, where cells are either empty (0) or walls (1). The task is to find a path from the start cell to the destination cell while traversing only through consecutive empty cells horizontally or vertically.

### 2.3 Investigating Solutions
Other possible approaches like Breadth-First Traversal and Dijkstra's algorithm were considered. While Breadth-First Traversal guarantees the shortest path, it may explore a large number of nodes before finding the destination. Dijkstra's algorithm is not required as there are no edge weights associated with the maze.

### 2.4 Selecting the Approach
DFS was selected for its simplicity and efficiency in terms of space complexity compared to BFS. It provides a solution if it exists, which is sufficient for this problem.

## Implementation
The Python implementation includes a recursive `dfs` function to explore the maze, marking visited cells as '2' to avoid revisiting them. The algorithm backtracks when it reaches a dead-end and explores alternative directions.

## Test
The provided test data is used to validate the correctness of the implemented solution. The test data includes a sample maze, start cell, and destination cell with the expected output.

## Enhancement Ideas
Potential enhancements include implementing a non-recursive version of DFS to avoid stack overflow for large mazes and optimizing the algorithm using memoization or dynamic programming techniques to avoid redundant computations.

## Conclusion
The Depth-First Traversal approach, implemented in Python, successfully solves the '490. The Maze' problem on LeetCode for the provided test data. The solution provides a straightforward and efficient way to tackle maze-solving problems, making it a suitable choice for similar scenarios. Potential enhancements can be considered to further optimize the algorithm's performance for more extensive mazes.

## Usage
To use the 'Maze Solver' Python code, simply copy the `hasPath` function from the `maze_solver.py` file to your project and call it with the appropriate maze, start, and destination arguments.

```python
from maze_solver import hasPath

# Example usage
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

print(hasPath(maze, start, destination))  # Output: True
