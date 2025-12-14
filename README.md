Python CLI Todo App

Overview

A Command Line Todo App built in Python.
Manage tasks with features to add, list, update, mark done, and delete tasks. Tasks are saved in a JSON file for persistent storage.

Features:
Add tasks with unique IDs and creation timestamp
List tasks with status  Done /  Not Done
Update task titles
Mark tasks as done or pending
Delete tasks with automatic ID reassignment
Persistent storage in tasks.json

Project Structure:

├── main.py        
├── storage.py     
├── tasks.json     
└── README.md      

Challenges & Solutions:
IDs were not updating after: deleting tasks → solved by reassigning IDs automatically
JSON file was hard to read: added indent=4 for better formatting
Task updates sometimes didn’t save: ensured save_tasks() is called after every change

Gemini CLI Assistance:
Helped debug function logic and menu loop design
Suggested error handling improvements
Guided JSON handling and data persistence
Assisted in learning Python dictionaries, lists, and functions

Tools Used:
Python
JSON module
Gemini CLI for guidance and debugging

This project demonstrates a beginner-friendly, fully functional CLI Todo App with persistent storage and clean code structure.
