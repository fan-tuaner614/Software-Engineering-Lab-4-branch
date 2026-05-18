class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name: str):
        self.tasks.append({"name": name, "done": False})

    def complete_task(self, name: str):
        for task in self.tasks:
            if task["name"] == name:
                task["done"] = True
                break
