def calculate_cost(task):
    return (task.difficulty*3+(10-task.priority)+task.deadline*2)
def total_cost(task_list):
    return sum(calculate_cost(t) for t in task_list)