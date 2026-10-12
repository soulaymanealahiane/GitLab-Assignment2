"""Soulaymane's task creation feature."""
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


def add_task(tasks: list[Task], title: str) -> Task:
    """Append a pending task with an ID above every existing task ID."""
    if not isinstance(title, str):
        raise TypeError("Task title must be a string.")
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    task = Task(id=max((item.id for item in tasks), default=0) + 1, title=title)
    tasks.append(task)
    return task
