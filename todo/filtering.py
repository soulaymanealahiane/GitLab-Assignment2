
"""Functions for filtering tasks by completion status."""

from todo.tasks import Task


def filter_tasks(tasks: list[Task], status: str = "all") -> list[Task]:
    """Return tasks matching the requested completion status."""
    if status not in ("all", "pending", "completed"):
        raise ValueError("Status must be 'all', 'pending', or 'completed'.")

    filtered_tasks = []

    for task in tasks:
        if status == "all":
            filtered_tasks.append(task)
        elif status == "pending" and task.completed is False:
            filtered_tasks.append(task)
        elif status == "completed" and task.completed is True:
            filtered_tasks.append(task)

    return filtered_tasks
