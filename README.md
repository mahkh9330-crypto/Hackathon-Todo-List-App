# Hackathon-Todo-List-App
## Overview
This is a Beginner-friendly Command Line Interface (CLI) Todo App built in Python.  
You can:

- Add new tasks
- List all tasks
- Update tasks
- Mark tasks as done or pending
- Delete tasks

---

## Features

1. Add Task
   - Enter a task title
   - Automatically records **creation date and time**
   - Assigns a unique ID

2. List Tasks**  
   - Shows all tasks with:
     - ID
     - Title
     - Status (Done / Not Done)
     - Created date and time

3. Update Task 
   - Change the task title
   - Double quotes display current title for clarity
   - Press Enter to keep the old title

4. Mark Task Done/Undone  
   - Toggle task status between Done and Pending
   - Friendly messages show the change

5. Delete Task 
   - Remove a task by ID
   - Automatically reassigns IDs for remaining tasks
   - Keeps numbering continuous and clear

6. Persistent Storage
   - Tasks are saved in `tasks.json`  
   - Automatically loaded on program start

7. Better User Interface (UI)
   - Friendly messages and readable timestamps  
   - Clean menu for easy navigation

## How to Run

1. Make sure Python is installed on your computer.
2. Clone or download this project from GitHub.
3. Open terminal / command prompt in the project folder.
4. Run the app with:

python main.py
Follow the on-screen menu to manage your tasks.

How I Built This App & Challenges I Faced
Starting as a Beginner: 

I had never built a CLI app before.
At first, I was unsure how to store tasks so they don’t disappear.

Identifying Problems:
Task IDs were not updating after deleting tasks.
JSON file was saving tasks in a single line → hard to read.
Some functions were not saving tasks correctly after updates.

Solving Problems:
Learned to reassign IDs after deletion.
Added indent=4 in json.dump() → makes JSON file readable.
Made functions call save_tasks() after every change → prevents losing data.
Used double quotes for task titles → improves readability in updates and lists.

How Gemini CLI Helped:
Gemini CLI helped me identify small mistakes in function logic.
Example: forgot to increment next_id after adding a task
Example: forgot to pass tasks and next_id to save_tasks()
Helped me build proper menu loop logic, Suggested user-friendly error handling for invalid inputs

Project Structure:

├── main.py        
├── storage.py     
├── tasks.json     
└── README.md      

Bonus Features / Improvements I Added:
Double quotes for task titles.
Automatic ID reassignment after deletion.
Created timestamp shown in a readable format.
Friendly messages for errors and invalid input.
JSON file formatting with indentation.

Tools Used:
Python (for building the app).
JSON module (for storing tasks).
Gemini CLI (for assistance with logic, debugging, and suggestions).

Lessons Learned: 

Learned how to use Python dictionaries and lists to manage complex data.
Learned persistent storage with JSON.
Understood how to structure a Python project.
Learned how to debug common mistakes with the help of Gemini CLI.
Practiced clean code and readable CLI design.

How Gemini CLI Helped:

Generated starter code for menu loop
Checked logic in add_task, update_task, and delete_task functions
Suggested error handling improvements
Helped me understand how to save and load tasks properly
Overall, accelerated my learning as a beginner and helped avoid common mistakes

Conclusion:
This project is a beginner-friendly Python CLI Todo App that meets hackathon requirements.
It’s modular, user-friendly, and persistent. Using Gemini CLI helped me learn and improve my coding skills while completing the project efficiently.
I am proud that I could build a fully working Todo app with my own understanding as a beginner, solve problems along the way, and improve the user experience.
