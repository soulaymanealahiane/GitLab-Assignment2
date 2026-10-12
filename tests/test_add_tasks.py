"""Soulaymane's tests for task creation."""
import pytest

from todo.tasks import add_task


def test_add_tasks_assigns_unique_ids_and_preserves_existing_tasks():
    tasks = []
    first = add_task(tasks, "Read notes")
    second = add_task(tasks, "Submit assignment")
    assert tasks == [first, second]
    assert (first.id, second.id) == (1, 2)
    assert (first.title, second.title) == ("Read notes", "Submit assignment")
    assert first.completed is False
    assert second.completed is False


def test_add_task_trims_surrounding_whitespace():
    tasks = []
    task = add_task(tasks, "  Read notes  ")
    assert task.title == "Read notes"


def test_add_task_rejects_blank_title_without_changing_tasks():
    tasks = []
    existing = add_task(tasks, "Read notes")
    with pytest.raises(ValueError, match="cannot be empty"):
        add_task(tasks, "   ")
    assert tasks == [existing]
