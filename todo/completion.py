"""Operations for changing task completion state."""

from todo.tasks import Task


def complete_task(tasks: list[Task], task_id: int) -> Task:
    """Mark the task with ``task_id`` complete and return the same task."""
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    raise LookupError(f"Task with ID {task_id} was not found.")


def reopen_task(tasks: list[Task], task_id: int) -> Task:
    """Mark the task with ``task_id`` pending and return the same task."""
    for task in tasks:
        if task.id == task_id:
            task.completed = False
            return task
    raise LookupError(f"Task with ID {task_id} was not found.")
