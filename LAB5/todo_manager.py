"""To-Do List and Task Manager module.

Provides functionality to add tasks with priorities, complete them,
list pending tasks, search by keyword, and save/load tasks as JSON.
"""
import json
import secrets
from datetime import datetime
from email.message import EmailMessage

tasks = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def add_task(title, priority="medium", labels=None):
    """Add a new task with given title, priority, and optional labels."""
    if labels is None:
        labels = []
    task_id = len(tasks) + 1
    labels.append(priority)
    tasks[task_id] = {
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().isoformat(),
        "labels": labels,
    }
    return task_id


def complete_task(task_id):
    """Mark a task as complete given its task ID."""
    if task_id in tasks:
        tasks[task_id]["done"] = True
        return True
    print("No task with id", task_id)
    return False


def pending_tasks():
    """Return a list of titles of pending tasks sorted by priority."""
    pending = [task for task in tasks.values() if not task["done"]]
    pending.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    return [task["title"] for task in pending]


def find_task(keyword):
    """Find a task ID by keyword in title, or return None if not found."""
    for task_id, task in tasks.items():
        if keyword.lower() in task["title"].lower():
            return task_id
    return None


def save_tasks(file_name="tasks.json"):
    """Save tasks dictionary to a JSON file securely."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def load_tasks(file_name="tasks.json"):
    """Load tasks dictionary from a JSON file safely."""
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
        return {int(k): v for k, v in data.items()}


def export_json(file_name="tasks.json"):
    """Export tasks to a formatted JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def remind_by_email(address):
    """Build (not send) an email reminder from tasks.json, without a shell.

    The original ran ``os.system`` with the address pasted into the command,
    which allowed shell injection. This version only builds an EmailMessage;
    sending it (e.g. via smtplib) is left to the caller.
    """
    # Helper kept for the lab: not called by the demo
    with open("tasks.json", "r", encoding="utf-8") as file:
        content = file.read()
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = "Pending tasks"
    msg["To"] = address
    return msg


def main():
    """Demonstrate task manager operations."""
    add_task("Submit lab report", "high")
    add_task("Buy groceries")
    add_task("Call plumber", "low")
    add_task("Book train tickets", "high")
    complete_task(2)
    complete_task(99)
    print("Pending tasks:", pending_tasks())
    print("Task id for 'plumber':", find_task("plumber"))
    print("Task id for 'gym':", find_task("gym"))  # returns None silently
    suggestion = secrets.choice(pending_tasks())
    print("Try this next:", suggestion)
    save_tasks()
    restored = load_tasks()
    print("Tasks restored from file:", len(restored))
    export_json()
    print("Exported tasks to tasks.json")


if __name__ == "__main__":
    main()
