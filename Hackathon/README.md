Python CLI Todo App 

Project Description:
This is a simple Command Line Todo List Application built using Python. The app is simple to run and beginner-friendly. It uses a storage file (`tasks.json`) to save tasks permanently, so your tasks are not lost after closing the app.

The app allows users to manage their daily tasks directly from the terminal.
Users can:
Add new tasks
View all tasks
Update task titles
Mark tasks as done or pending
Delete tasks
The tasks are saved in a file, so they are not lost when the program is closed.

Technologies Used:
Python
JSON (for saving tasks)
Gemini CLI (as AI coding assistant)

How to Run the App:
Make sure Python is installed on your system
Open terminal in the project folder
Run the following command:
python main.py

Features:
Menu-based Command Line Interface
Add tasks with title and creation time
List all tasks with status (Done / Not Done)
Update existing task titles
Mark tasks as complete or incomplete
Delete tasks
Tasks are saved automatically using a JSON file

Data Storage:
Tasks are stored in a file called tasks.json
When the app starts, it loads existing tasks from the file
When tasks are added, updated, or deleted, the file is updated automatically
This ensures tasks are not lost when the program exits.

Use of Gemini CLI:
Gemini CLI was used as a coding assistant to:
Understand the project requirements
Get help in designing the menu structure
Improve error handling and code clarity
Debug small issues during development
All generated suggestions were carefully understood and modified before use.

File Structure:
├── main.py        # Main program with CLI logic
├── storage.py     # File handling (load and save tasks)
├── tasks.json     # Stores all tasks (created automatically)
└── README.md      # This file


Bonus Features:
File-based task saving using JSON
Task creation timestamp
Toggle task status (done / pending)
User-friendly messages and error handling

Conclusion:
This project helped me understand:
Python basics
Lists and dictionaries
Functions and loops
File handling using JSON
How to build a complete CLI-based application
This project is beginner-friendly and meets all hackathon requirements.
