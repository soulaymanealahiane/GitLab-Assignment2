"""Run the To-Do List in memory."""

from todo.tasks import add_task
from todo.completion import complete_task, reopen_task
from todo.filtering import filter_tasks


def main():
    tasks = []

    print("To-Do List")

    while True:
        print("\n1. Add task")
        print("2. Complete task")
        print("3. Reopen task")
        print("4. List all tasks")
        print("5. List pending tasks")
        print("6. List completed tasks")
        print("0. Exit")

        try:
            choice = input("Choose: ").strip()

            if choice == "0":
                print("Goodbye!")
                return

            elif choice == "1":
                title = input("Task title: ")
                task = add_task(tasks, title)
                print(f"Added task {task.id}: {task.title}")

            elif choice == "2":
                task_id = int(input("Task ID to complete: "))
                complete_task(tasks, task_id)
                print(f"Task {task_id} marked as completed.")

            elif choice == "3":
                task_id = int(input("Task ID to reopen: "))
                reopen_task(tasks, task_id)
                print(f"Task {task_id} marked as pending.")

            elif choice == "4":
                selected_tasks = filter_tasks(tasks, "all")

                if len(selected_tasks) == 0:
                    print("No tasks found.")
                else:
                    for task in selected_tasks:
                        if task.completed:
                            status = "Completed"
                        else:
                            status = "Pending"

                        print(f"{task.id}. {task.title} - {status}")

            elif choice == "5":
                selected_tasks = filter_tasks(tasks, "pending")

                if len(selected_tasks) == 0:
                    print("No pending tasks.")
                else:
                    for task in selected_tasks:
                        print(f"{task.id}. {task.title} - Pending")

            elif choice == "6":
                selected_tasks = filter_tasks(tasks, "completed")

                if len(selected_tasks) == 0:
                    print("No completed tasks.")
                else:
                    for task in selected_tasks:
                        print(f"{task.id}. {task.title} - Completed")

            else:
                print("Invalid choice. Choose a number from 0 to 6.")

        except ValueError as error:
            print(f"Invalid input: {error}")
        except LookupError as error:
            print(f"Task not found: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return


if __name__ == "__main__":
    main()