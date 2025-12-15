# Python CLI Todo App

## Overview

A Command Line Todo App built in Python.
Manage tasks with features to add, list, update, mark done, and delete tasks. Tasks are saved in a JSON file for persistent storage.

# Features:

1.Add tasks with unique IDs and creation timestamp

2.List tasks with status  Done /  Not Done

3.Update task titles

4.Mark tasks as done or pending

5.Delete tasks with automatic ID reassignment

6.Persistent storage in tasks.json

# Project Structure:

├── main.py        
├── storage.py     
├── tasks.json     
└── README.md      

# Challenges & Solutions:

1.IDs were not updating after deleting tasks:  solved by reassigning IDs automatically

2.JSON file was hard to read: added indent=4 for better formatting

3.Task updates sometimes didn’t save: ensured save_tasks() is called after every change

# Gemini CLI Assistance:

1.Helped debug function logic and menu loop design

2.Suggested error handling improvements

3.Guided JSON handling and data persistence

4.Assisted in learning Python dictionaries, lists, and functions

# Tools Used:

1.Python

2.JSON module

3.Gemini CLI for guidance and debugging

This project demonstrates a fully functional CLI Todo App with persistent storage and clean code structure.
