class Task:
    def __init__(self, name, difficulty, deadline, priority, duration):
        self.name = name
        self.difficulty = difficulty
        self.deadline = deadline
        self.priority = priority
        self.duration = duration

    def __repr__(self):
        return self.name
