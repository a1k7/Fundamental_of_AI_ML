from collections import deque
from utils import calculate_cost


def bfs(tasks, energy_level, max_time):
    queue = deque()
    queue.append([])

    best = None
    best_cost = float('inf')

    while queue:
        path = queue.popleft()

        # Goal state
        if len(path) == len(tasks):
            cost = calculate_cost(path, energy_level, max_time)

            if cost < best_cost:
                best = path
                best_cost = cost

            continue

        # Expand
        for t in tasks:
            if t not in path:
                new_path = path + [t]
                queue.append(new_path)

    return best, best_cost
