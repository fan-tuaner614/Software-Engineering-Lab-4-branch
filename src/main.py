from task_manager import TaskManager
from report import build_report


def main():
    manager = TaskManager()
    manager.add_task("Setup repository")
    manager.add_task("Create branches")
    manager.add_task("Merge and resolve conflicts")
    print(build_report(manager.tasks))


if __name__ == "__main__":
    main()
