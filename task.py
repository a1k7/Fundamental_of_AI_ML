class Task:
    def __init__(self, name, difficulty, deadline, priority):
        self.name = name
        self.difficulty = difficulty
        self.deadline = deadline
        self.priority = priority

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)