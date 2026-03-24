import random
from utils import total_cost

def hill_climbing(tasks):
    current=tasks[:]
    random.shuffle(current)
    current_cost=total_cost(current)

    while True:
        neighbour=current[:]
        i,j=random.sample(range(len(tasks)),2)
        neighbour[i],neighbour[j]=neighbour[j],neighbour[i]

        neighbour_cost=total_cost(neighbour)
        if neighbour_cost<current_cost:
            current=neighbour
            current_cost=neighbour_cost
        else:
            break
    return current