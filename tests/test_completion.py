"""Tests for completing and reopening tasks."""

import pytest

from todo.completion import complete_task, reopen_task
from todo.tasks import Task


def test_complete_task_updates_and_returns_existing_task():
    task = Task(id=4, title="Read notes")
    tasks = [task]

    result = complete_task(tasks, 4)

    assert result is task
    assert task.completed is True
    assert tasks == [task]


def test_reopen_task_clears_completed_state_and_returns_existing_task():
    task = Task(id=4, title="Read notes", completed=True)
    tasks = [task]

    result = reopen_task(tasks, 4)

    assert result is task
    assert task.completed is False
    assert tasks == [task]


@pytest.mark.parametrize("operation", [complete_task, reopen_task])
def test_unknown_id_raises_lookup_error_without_changing_tasks(operation):
    task = Task(id=4, title="Read notes", completed=True)
    tasks = [task]

    with pytest.raises(LookupError, match="ID 9"):
        operation(tasks, 9)

    assert tasks == [task]
    assert task.completed is True


@pytest.mark.parametrize("operation", [complete_task, reopen_task])
def test_unknown_id_in_empty_list_raises_lookup_error(operation):
    tasks = []

    with pytest.raises(LookupError, match="ID 9"):
        operation(tasks, 9)

    assert tasks == []
