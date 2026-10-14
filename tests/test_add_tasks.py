"""Soulaymane's tests for task creation."""
import pytest

from todo.tasks import Task, add_task


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


def test_add_task_allocates_id_after_nonconsecutive_existing_ids():
    tasks = [Task(id=2, title="Read notes"), Task(id=7, title="Submit assignment")]
    task = add_task(tasks, "Review feedback")
    assert task.id == 8
    assert [item.id for item in tasks] == [2, 7, 8]
