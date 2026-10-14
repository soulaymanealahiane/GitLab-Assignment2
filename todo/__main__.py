"""Run the To-Do List in memory."""
from todo.tasks import add_task


def main():
    tasks = []
    print("To-Do List")
    while True:
        print("1. Add task\n0. Exit")
        try:
            choice = input("Choose: ").strip()
            if choice == "0":
                return
            if choice != "1":
                print("Choose 1 or 0.")
                continue
            task = add_task(tasks, input("Task title: "))
            print(f"Added task {task.id}: {task.title}")
        except ValueError as error:
            print(error)
        except (EOFError, KeyboardInterrupt):
            return


if __name__ == "__main__":
    main()
