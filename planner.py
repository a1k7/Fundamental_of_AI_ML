from search_algorithms import bfs
from utils import total_cost
from heuristic import a_star
from hill_climbing import hill_climbing
from dfs import dfs


def format_plan(plan):
    if not plan:
        return "❌ No valid plan found"

    return " → ".join([t.name for t in plan])


def print_section(title, plan):
    print("\n" + "=" * 50)
    print(f"🚀 {title}")
    print("=" * 50)

    print("Plan:")
    print(format_plan(plan))

    if plan:
        print(f"\nTotal Cost: {total_cost(plan)}")


def run_planner(tasks):
    print("\n🧠 SMART STUDY PLANNER (AI POWERED)")
    print("=" * 50)

    bfs_plan = bfs(tasks)
    dfs_plan = dfs(tasks)[0]
    hill_plan = hill_climbing(tasks)
    astar_plan = a_star(tasks)

    print_section("BFS PLAN", bfs_plan)
    print_section("DFS PLAN", dfs_plan)
    print_section("HILL CLIMBING PLAN", hill_plan)
    print_section("A* PLAN", astar_plan)