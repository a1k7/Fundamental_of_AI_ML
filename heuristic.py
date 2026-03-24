import heapq
from itertools import count
from utils import total_cost


def heuristic(path, tasks):
    remaining = [t for t in tasks if t not in path]
    return sum(t.difficulty for t in remaining)


def a_star(tasks):
    pq = []
    counter = count()  # unique sequence count

    # (f_cost, unique_id, path)
    heapq.heappush(pq, (0, next(counter), []))

    best = None
    best_cost = float('inf')

    while pq:
        cost, _, path = heapq.heappop(pq)

        if len(path) == len(tasks):
            final_cost = total_cost(path)
            if final_cost < best_cost:
                best = path
                best_cost = final_cost
            continue

        for t in tasks:
            if t not in path:
                new_path = path + [t]
                g = total_cost(new_path)
                h = heuristic(new_path, tasks)

                # push with UNIQUE counter → no comparisons on Task objects ever
                heapq.heappush(pq, (g + h, next(counter), new_path))

    return best if best else []