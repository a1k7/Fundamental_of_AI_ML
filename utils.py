def calculate_cost(plan, energy_level, max_time):
    total_cost = 0
    total_time = 0
    fatigue = 0

    for i, task in enumerate(plan):
        # Base cost
        total_cost += task.difficulty * 3
        total_cost += (10 - task.priority)
        total_cost += task.deadline * 2

        # Time
        total_time += task.duration

        # Fatigue model
        fatigue += task.difficulty

        if fatigue > energy_level * 2:
            total_cost += 15

        # Bad sequencing penalty
        if i > 0:
            if plan[i-1].difficulty > 6 and task.difficulty > 6:
                total_cost += 10

    # Time overflow penalty
    if total_time > max_time:
        total_cost += (total_time - max_time) * 5

    return total_cost
def total_cost(task_list):
    return sum(calculate_cost(t) for t in task_list)
