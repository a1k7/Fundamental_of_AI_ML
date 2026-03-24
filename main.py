from task import Task
from planner import run_planner


def main():
    tasks = [
        Task("Math", 8, 2, 9),
        Task("Physics", 7, 3, 8),
        Task("AI", 6, 5, 10),
        Task("English", 3, 4, 5),
    ]

    run_planner(tasks)


if __name__ == "__main__":
    main()