def dfs(tasks, path=None, best=None, best_cost=float('inf')):
    from utils import total_cost

    if path is None:
        path = []

    if len(path) == len(tasks):
        cost = total_cost(path)
        return path, cost

    for t in tasks:
        if t not in path:
            result, cost = dfs(tasks, path + [t], best, best_cost)
            if cost < best_cost:
                best = result
                best_cost = cost

    return best, best_cost