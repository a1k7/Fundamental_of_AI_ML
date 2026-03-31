from heuristic import a_star
from hill_climbing import hill_climbing
from search_algorithms import bfs
from dfs import dfs

def format_plan(plan):
    return " → ".join([t.name for t in plan])


def run_planner(tasks, energy_level, max_time):
    print("\n🧠 ADAPTIVE AI STUDY PLANNER")
    print("=" * 50)

    bfs_plan, bfs_cost = bfs(tasks, energy_level, max_time)
    dfs_plan, dfs_cost = dfs(tasks, energy_level, max_time)
    astar_plan, astar_cost = a_star(tasks, energy_level, max_time)
    hill_plan, hill_cost = hill_climbing(tasks, energy_level, max_time)

    print("\n🚀 BFS PLAN")
    print(format_plan(bfs_plan))
    print("Cost:", bfs_cost)

    print("\n🚀 DFS PLAN")
    print(format_plan(dfs_plan))
    print("Cost:", dfs_cost)

    print("\n🚀 A* OPTIMAL PLAN")
    print(format_plan(astar_plan))
    print("Cost:", astar_cost)

    print("\n⚡ HILL CLIMBING PLAN")
    print(format_plan(hill_plan))
    print("Cost:", hill_cost)
