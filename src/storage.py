def save_tasks(tasks, path):
    with open(path, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task['name']}\n")
