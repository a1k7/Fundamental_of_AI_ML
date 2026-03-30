from task import Task
from planner import run_planner


def main():
    tasks = [
        Task("Math", 8, 2, 9, 2),
        Task("Physics", 7, 3, 8, 2),
        Task("AI", 6, 5, 10, 1),
        Task("English", 3, 4, 5, 1),
    ]

    energy_level = 6
    max_time = 5

    run_planner(tasks, energy_level, max_time)


if __name__ == "__main__":
    main()
