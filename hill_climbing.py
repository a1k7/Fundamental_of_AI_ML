import random
from utils import calculate_cost


def hill_climbing(tasks, energy_level, max_time):
    current = tasks[:]
    random.shuffle(current)

    current_cost = calculate_cost(current, energy_level, max_time)

    while True:
        neighbor = current[:]

        i, j = random.sample(range(len(tasks)), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

        neighbor_cost = calculate_cost(neighbor, energy_level, max_time)

        if neighbor_cost < current_cost:
            current = neighbor
            current_cost = neighbor_cost
        else:
            break

    return current, current_cost
