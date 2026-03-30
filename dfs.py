from utils import calculate_cost


def dfs(tasks, energy_level, max_time, path=None, best=None, best_cost=float('inf')):
    
    if path is None:
        path = []

    # Goal state
    if len(path) == len(tasks):
        cost = calculate_cost(path, energy_level, max_time)

        if cost < best_cost:
            return path, cost

        return best, best_cost

    for t in tasks:
        if t not in path:
            result, cost = dfs(
                tasks,
                energy_level,
                max_time,
                path + [t],
                best,
                best_cost
            )

            if cost < best_cost:
                best = result
                best_cost = cost

    return best, best_cost
