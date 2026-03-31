Adaptive AI Study Planner (AI Powered)

The Adaptive AI Study Planner is an AI-driven system designed to optimize the sequencing of study tasks through the application of search algorithms. Beyond merely accounting for fundamental elements such as task difficulty and due dates, the system incorporates real-world variables, including energy levels, fatigue, and temporal limitations. This project serves as a demonstration of how Artificial Intelligence methodologies can be leveraged to replicate human decision-making processes, thereby enhancing practical applicability.


🚨 Problem Statement Students often struggle to decide what to study next. This leads to: Poor time management Increased stress Mental fatigue Inefficient study patterns Most students randomly pick subjects without considering how task order affects productivity. In reality, the problem is not just about selecting tasks, but about sequencing them intelligently under constraints.

This project approaches the problem as a state-space search, where each state represents a sequence of tasks. The goal is to find the best sequence, which has the lowest cost.

To make the solution more practical, the system was expanded into an adaptive AI agent. This agent considers time limits, energy levels, fatigue, and the order of tasks.

The system uses several AI search algorithms to create study plans: Breadth-First Search (BFS), Depth-First Search (DFS), Hill Climbing, and A* Search.

Algorithms Used

BFS (Breadth-First Search) explores all possible solutions level by level, ensuring completeness, but it is computationally expensive. DFS (Depth-First Search) explores one path deeply before backtracking; it's faster but not always optimal. Hill Climbing starts with a random solution and improves it step-by-step, but it can get stuck in a local optimum. A* Search uses a heuristic to guide the search, making it more efficient than BFS by combining actual cost with estimated future cost.

Cost Function

The system evaluates each study plan using a multi-factor cost model, which includes task difficulty, priority, deadline urgency, fatigue, time overflow, and bad sequencing penalties.

Factors: Difficulty → Higher difficulty increases cost; Priority → Higher priority reduces cost; Deadline → Urgency increases cost; Fatigue → Consecutive hard tasks increase penalty; Time → Exceeding available time adds penalty; Sequence → Poor ordering (hard → hard) increases cost 🧠 Fatigue-aware Tracks mental fatigue and penalizes overload. 🔁 Sequence-aware Avoids placing multiple difficult tasks consecutively.

📂 Project Structure project/ │ ├── main.py # Entry point ├── task.py # Task class ├── planner.py # Output formatting ├── search_algorithms.py # BFS implementation ├── dfs.py # DFS implementation ├── hill_climbing.py # Hill Climbing logic ├── heuristic.py # A* implementation ├── utils.py # Cost function ├── README.md └── report.pdf

▶️ How to Run 1️⃣ Clone Repository git clone cd project 2️⃣ Run Program python main.py

🧪 Example Input

tasks = [ Task("Math", 8, 2, 9, 2), Task("Physics", 7, 3, 8, 2), Task("AI", 6, 5, 10, 1), Task("English", 3, 4, 5, 1), ]

energy_level = 6 max_time = 5

📊 Example Output 🧠 ADAPTIVE AI STUDY PLANNER

🚀 BFS PLAN Math → English → Physics → AI Cost: 143

🚀 DFS PLAN Math → English → Physics → AI Cost: 143

🚀 A* OPTIMAL PLAN English → Math → AI → Physics Cost: 143

⚡ HILL CLIMBING PLAN English → Physics → AI → Math Cost: 143

🌍 Real-Life Application This system can be used by students to: Plan study schedules based on available time Avoid burnout by managing fatigue Improve productivity by intelligent sequencing Make structured decisions instead of random choices It reflects real-world behavior where energy and fatigue influence performance.

⚠️ Observations Different algorithms produced different sequences Cost values may remain similar, but sequence quality differs A* generally produces more balanced plans Hill Climbing is faster but less stable This shows that optimization is not only about cost, but also about sequence quality and practicality.

🚧 Debugging priority queue problems in A* was a headache. I also ran into object comparison errors. Designing a cost function that made sense was another hurdle. And then there was the challenge of juggling multiple constraints at once.

📚 I learned that real-world AI problems demand careful modeling. Heuristic search techniques can really make a difference in practical applications. Constraints, such as fatigue and time, are absolutely vital. AI isn't just about the algorithms; it's about how you design the decision-making process.

🔮 Looking ahead, I want to incorporate machine learning for personalized planning. A web and mobile interface is also on the agenda. I'll be tracking user performance over time, and I plan to implement dynamic adjustments to energy levels.
