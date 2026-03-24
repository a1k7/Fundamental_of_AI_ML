from collections import deque
from utils import total_cost

from collections import deque
from utils import total_cost

def bfs(tasks):
    queue = deque()
    queue.append([])  # start with empty path

    best = None
    best_cost = float('inf')

    while queue:
        path = queue.popleft()

        # DEBUG (you can remove later)
        # print("Current path:", path)

        if len(path) == len(tasks):
            cost = total_cost(path)

            if cost < best_cost:
                best = path
                best_cost = cost

            continue

        for t in tasks:
            # safer comparison using names
            if t.name not in [p.name for p in path]:
                new_path = path + [t]
                queue.append(new_path)

    return best if best else []