def build_report(tasks):
    lines = ["Branch Demo Report"]
    for index, task in enumerate(tasks, start=1):
        status = "done" if task["done"] else "todo"
        lines.append(f"{index}. {task['name']} [{status}]")
    return "\n".join(lines)
