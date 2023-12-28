# Connect 4 AI with Minimax Algorithm

## Introduction

Welcome to the GitHub repository for an interactive tutorial on implementing a Connect 4 AI using the minimax algorithm. This tutorial is designed for learners beginning to explore game AI and minimax algorithms. By the end, you'll have a comprehensive understanding of the minimax algorithm, its application in game strategies, and how to implement it in Python.

## Contents

- [Algorithm Overview](#algorithm-overview)
- [Connect 4 Game Rules](#connect-4-game-rules)
- [Environment Setup](#environment-setup)
- [Connect 4 Implementation](#connect-4-implementation)
- [Connect 4 Game Simulation](#connect-4-game-simulation)
- [The Minimax Algorithm](#the-minimax-algorithm)
- [Enhancing the Minimax Function](#enhancing-the-minimax-function)
- [Optimizing AI Performance](#optimizing-ai-performance)
- [Conclusion](#conclusion)

## Algorithm Overview

The minimax algorithm is a recursive decision-making tool used in two-player games. It involves simulating the opponent's potential moves to identify the best move. The process creates a game state tree until a terminal point (win, loss, or draw) is reached. This tutorial also covers alpha-beta pruning, an optimization technique for minimax.

## Connect 4 Game Rules

Connect Four is a two-player game with a 7x6 board. Players take turns dropping colored discs into columns. The first to align four discs vertically, horizontally, or diagonally wins. A full board without alignment results in a draw.

![Connect 4 Game Board](image-2.png)

## Environment Setup

- **Python Version**: The tutorial uses Python 3. Check your Python version with `!python --version`.
- **Importing Game Code**: Our game logic is in `connect_four.py`. Ensure this file is in the same directory as your Jupyter Notebook.

```python
from connect_four import *

## Connect 4 Implementation
- **Board Representation**: The board is a 6x7 grid, initialized with empty spaces.
- **Making Moves**: Functions for placing pieces and checking move validity.
- **Winning Condition**: `has_won` function checks for four consecutive discs.
- **Utility Functions**: Includes functions for generating moves, listing possible moves, and checking game status.
- **Gameplay Functions**: `play_random_game` allows playing against a random AI or watching two AI players.

## Connect 4 Game Simulation
You can play against a random AI or watch an AI vs. AI match. The simulations provide insights into strategies and game dynamics.

## The Minimax Algorithm
- **Explanation**: Minimax simulates all possible moves, evaluating and choosing the best one.
- **Building Minimax**: Step-by-step guide on implementing the minimax function, including handling base cases and developing recursive logic.
- **Enhancing with Move Return**: Modified to return the best move and its score.
- **Testing with Game Scenarios**: Setting up scenarios to test the algorithm.

## Enhancing the Minimax Function
- **Depth Limitation**: Introducing a depth parameter to limit recursion, improving execution time.
- **Evaluation Function**: Implementing `horizontal_evaluation` to assess non-terminal states based on streaks.
- **New Evaluation Strategy**: Considering horizontal, vertical, and diagonal streaks for a more comprehensive evaluation.

## Optimizing AI Performance
- **Alpha-Beta Pruning**: Integrating alpha-beta pruning to improve efficiency.
- **Simulation Tests**: Comparing the new evaluation function against the previous version in AI vs. AI matches.
- **Challenge Yourself**: Play against the optimized AI.

## Conclusion
This tutorial offers a deep dive into developing a Connect 4 AI with the minimax algorithm. From basic implementation to advanced optimizations and strategic evaluations, you'll gain valuable insights into AI development in gaming.

To start, clone this repository, set up your environment as described above, and dive into the tutorial!

```bash
git clone [repository-url]

