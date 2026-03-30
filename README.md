Adaptive AI Study Planner (AI Powered)

📌 Overview
Adaptive AI Study Planner is an AI-based system that helps in deciding the most effective order of studying tasks using search algorithms. Instead of only considering basic factors like difficulty and deadlines, the system models real-world conditions such as energy levels, fatigue, and time constraints.
This project demonstrates how Artificial Intelligence techniques can be extended to simulate human decision-making and improve practical usability.

🚨 Problem Statement
Students often struggle to decide what to study next. This leads to:
Poor time management
Increased stress
Mental fatigue
Inefficient study patterns
Most students randomly pick subjects without considering how task order affects productivity.
In reality, the problem is not just about selecting tasks, but about sequencing them intelligently under constraints.

💡 Solution
This project models the problem as a state-space search problem, where:
Each state represents a sequence of tasks
The goal is to find the optimal sequence with minimum cost

To make the solution realistic, I extended the system into an adaptive AI agent that considers:
Time constraints
Energy levels
Fatigue accumulation
Task sequencing

The system uses multiple AI search algorithms to generate study plans:
Breadth-First Search (BFS)
Depth-First Search (DFS)
Hill Climbing
A* Search

🧠 Algorithms Used

🔹 BFS (Breadth-First Search)
Explores all possible solutions level by level
Guarantees completeness
Computationally expensive
🔹 DFS (Depth-First Search)
Explores one path deeply before backtracking
Faster but not always optimal
🔹 Hill Climbing
Starts with a random solution
Improves solution step-by-step
May get stuck in local optimum
🔹 A* Search
Uses heuristic to guide search
More efficient than BFS
Combines actual cost + estimated future cost

⚙️ Cost Function
The system evaluates each study plan using a multi-factor cost model:
Cost =
Task difficulty
Priority factor
Deadline urgency
Fatigue penalty
Time overflow penalty
Bad sequencing penalty

Factors:
Difficulty → Higher difficulty increases cost
Priority → Higher priority reduces cost
Deadline → Urgency increases cost
Fatigue → Consecutive hard tasks increase penalty
Time → Exceeding available time adds penalty
Sequence → Poor ordering (hard → hard) increases cost

🚀 Intelligent Features
⏱️ Time-aware
Ensures total study duration stays within available time.
⚡ Energy-aware
Adapts plan based on user energy level.
🧠 Fatigue-aware
Tracks mental fatigue and penalizes overload.
🔁 Sequence-aware
Avoids placing multiple difficult tasks consecutively.

📂 Project Structure
project/
│
├── main.py                  # Entry point
├── task.py                  # Task class
├── planner.py               # Output formatting
├── search_algorithms.py     # BFS implementation
├── dfs.py                   # DFS implementation
├── hill_climbing.py         # Hill Climbing logic
├── heuristic.py             # A* implementation
├── utils.py                 # Cost function
├── README.md
└── report.pdf

▶️ How to Run
1️⃣ Clone Repository
git clone <your-repo-link>
cd project
2️⃣ Run Program
python main.py
🧪 Example Input
tasks = [
    Task("Math", 8, 2, 9, 2),
    Task("Physics", 7, 3, 8, 2),
    Task("AI", 6, 5, 10, 1),
    Task("English", 3, 4, 5, 1),
]

energy_level = 6
max_time = 5
📊 Example Output
🧠 ADAPTIVE AI STUDY PLANNER

🚀 BFS PLAN
Math → English → Physics → AI
Cost: 143

🚀 DFS PLAN
Math → English → Physics → AI
Cost: 143

🚀 A* OPTIMAL PLAN
English → Math → AI → Physics
Cost: 143

⚡ HILL CLIMBING PLAN
English → Physics → AI → Math
Cost: 143

🌍 Real-Life Application
This system can be used by students to:
Plan study schedules based on available time
Avoid burnout by managing fatigue
Improve productivity by intelligent sequencing
Make structured decisions instead of random choices
It reflects real-world behavior where energy and fatigue influence performance.

⚠️ Observations
Different algorithms produced different sequences
Cost values may remain similar, but sequence quality differs
A* generally produces more balanced plans
Hill Climbing is faster but less stable
This shows that optimization is not only about cost, but also about sequence quality and practicality.

🚧 Challenges Faced
Debugging priority queue issues in A*
Handling object comparison errors
Designing a realistic cost function
Balancing multiple constraints simultaneously

📚 Learnings
Real-world AI problems require proper modeling
Heuristic search improves practical solutions
Constraints like fatigue and time are crucial
AI is not just algorithms, but decision-making design

🔮 Future Scope
Add machine learning for personalized planning
Build a web/mobile interface
Track user performance over time
Dynamic adjustment of energy levels
