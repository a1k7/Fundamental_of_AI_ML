# 🧠 Smart Study Planner (AI Powered)

## 📌 Overview
Smart Study Planner is an AI-based project that helps students decide the optimal order of studying tasks using classical search algorithms. The system analyzes multiple factors such as difficulty, priority, and deadlines to generate an efficient study plan.

This project demonstrates how Artificial Intelligence techniques can be applied to solve real-world decision-making problems.

---

## 🚨 Problem Statement
Students often struggle to decide what to study next. This leads to:
- Poor time management
- Increased stress
- Inefficient study patterns

Most students randomly pick subjects instead of following a structured approach.

---

## 💡 Solution
This project models the problem as a **state-space search problem**, where:
- Each state represents a sequence of tasks
- The goal is to find the optimal sequence with minimum cost

We use multiple AI search algorithms to generate study plans:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Hill Climbing
- A* Search

---

## 🧠 Algorithms Used

### 🔹 BFS (Breadth-First Search)
- Explores all possible solutions level by level
- Guarantees finding the optimal solution
- Computationally expensive

### 🔹 DFS (Depth-First Search)
- Explores one path deeply before backtracking
- Faster but not always optimal

### 🔹 Hill Climbing
- Starts with a random solution
- Improves solution step-by-step
- May get stuck in local optimum

### 🔹 A* Search
- Uses heuristic to guide search
- More efficient than BFS
- Combines cost + estimated future cost

---

## ⚙️ Cost Function

The system evaluates each study plan using the following formula:

Cost = (difficulty × 3) + (10 − priority) + (deadline × 2)

### Factors:
- **Difficulty** → Higher difficulty increases cost
- **Priority** → Higher priority reduces cost
- **Deadline** → Urgency increases cost

---

## 📂 Project Structure
smart-study-planner/
│
├── main.py # Entry point
├── task.py # Task class
├── planner.py # Output formatting
├── search_algorithms.py # BFS, DFS
├── hill_climbing.py # Hill Climbing logic
├── heuristic.py # A* implementation
├── utils.py # Cost function
├── README.md
└── report.pdf
---

## ▶️ How to Run

### 1️⃣ Clone Repository
```bash
git clone <your-repo-link>
cd smart-study-planner
python main.py



