
"""Tests for filtering tasks by completion status."""

import pytest

from todo.filtering import filter_tasks
from todo.tasks import Task


def test_filter_pending_tasks():
    task1 = Task(id=1, title="Study", completed=False)
    task2 = Task(id=2, title="Homework", completed=True)
    tasks = [task1, task2]

    result = filter_tasks(tasks, "pending")

    assert result == [task1]
    assert result is not tasks


def test_filter_completed_tasks():
    task1 = Task(id=1, title="Study", completed=False)
    task2 = Task(id=2, title="Homework", completed=True)
    tasks = [task1, task2]

    result = filter_tasks(tasks, "completed")

    assert result == [task2]


def test_filter_all_tasks_and_preserve_order():
    task1 = Task(id=1, title="Study")
    task2 = Task(id=2, title="Homework", completed=True)
    tasks = [task1, task2]

    result = filter_tasks(tasks)

    assert result == [task1, task2]


def test_filter_empty_list():
    assert filter_tasks([], "pending") == []


def test_invalid_status_raises_value_error():
    task = Task(id=1, title="Study")

    with pytest.raises(ValueError):
        filter_tasks([task], "unfinished")
