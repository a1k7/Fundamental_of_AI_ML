import heapq
from itertools import count
from utils import calculate_cost


def heuristic(path, tasks):
    remaining = [t for t in tasks if t not in path]
    return sum(t.difficulty for t in remaining)


def a_star(tasks, energy_level, max_time):
    pq = []
    counter = count()

    heapq.heappush(pq, (0, next(counter), []))

    best = None
    best_cost = float('inf')

    while pq:
        _, _, path = heapq.heappop(pq)

        if len(path) == len(tasks):
            cost = calculate_cost(path, energy_level, max_time)

            if cost < best_cost:
                best = path
                best_cost = cost

            continue

        for t in tasks:
            if t not in path:
                new_path = path + [t]

                g = calculate_cost(new_path, energy_level, max_time)
                h = heuristic(new_path, tasks)

                heapq.heappush(pq, (g + h, next(counter), new_path))

    return best, best_cost
