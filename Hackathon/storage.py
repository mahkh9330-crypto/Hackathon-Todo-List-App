# storage.py
# This file handles all saving and loading of tasks from a JSON file.

import json

TASKS_FILE = "tasks.json"

# Function to save tasks into the JSON file
def save_tasks(tasks, next_id):
    """
    Save all tasks and the next task ID to a JSON file.
    """
    with open(TASKS_FILE, "w") as f:
        json.dump(
            {"tasks": tasks, "next_id": next_id},
            f,
            indent=4  # makes JSON human-readable
        )

# Function to load tasks from the JSON file
def load_tasks():
    """
    Load tasks and next task ID from JSON file.
    Returns:
        tasks (list): list of task dictionaries
        next_id (int): the next available task ID
    """
    try:
        with open(TASKS_FILE, "r") as f:
            data = json.load(f)
            return data.get("tasks", []), data.get("next_id", 1)
    except (FileNotFoundError, json.JSONDecodeError):
        # File does not exist or is corrupted, start fresh
        return [], 1
