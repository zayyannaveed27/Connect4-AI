# Connect 4 AI with Minimax Algorithm

## Introduction

Welcome to the GitHub repository for an interactive tutorial on implementing a Connect 4 AI using the minimax algorithm. This tutorial is designed for learners beginning to explore game AI and minimax algorithms. By the end, you'll have a comprehensive understanding of the minimax algorithm, its application in game strategies, and how to implement it in Python. To run the tutorial open the file `tutorial.ipynb` 

## Contents

- [Algorithm Overview](#algorithm-overview)
- [The Minimax Algorithm](#the-minimax-algorithm)
- [Enhancing the Minimax Function](#enhancing-the-minimax-function)
- [Optimizing AI Performance](#optimizing-ai-performance)

## Algorithm Overview

The minimax algorithm is a recursive decision-making tool used in two-player games. It involves simulating the opponent's potential moves to identify the best move. The process creates a game state tree until a terminal point (win, loss, or draw) is reached. This tutorial also covers alpha-beta pruning, an optimization technique for minimax.

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

To start, open the file `tutorial.ipynb`and start learning!

```bash
git clone [repository-url]
```
