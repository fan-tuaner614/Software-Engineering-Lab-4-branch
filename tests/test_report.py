import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from report import build_report


def test_build_report_empty():
    result = build_report([])
    assert "Branch Demo Report" in result


def test_build_report_single_task():
    tasks = [{"name": "Setup repository", "done": False}]
    result = build_report(tasks)
    assert "Setup repository" in result
    assert "todo" in result


def test_build_report_done_task():
    tasks = [{"name": "Create branches", "done": True}]
    result = build_report(tasks)
    assert "Create branches" in result
    assert "done" in result


def test_build_report_multiple_tasks():
    tasks = [
        {"name": "Task A", "done": True},
        {"name": "Task B", "done": False},
    ]
    result = build_report(tasks)
    lines = result.split("\n")
    assert lines[0] == "Branch Demo Report"
    assert len(lines) == 3
