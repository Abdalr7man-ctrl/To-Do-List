# Cli-Task-Tracker

A simple command-line interface (CLI) application built with Python for managing your personal tasks (To-Do List). It allows users to create accounts, log in, add, view, update the status of, and delete tasks.

to practice and build by yourself see [roadmap.sh](https://roadmap.sh/projects/task-tracker)

## Features

* User authentication (signup and login).
* Add new tasks.
* List tasks.
* Mark tasks with a specific status (Done, Not Done).
* Delete tasks.
* Edit task descriptions.
* Persistent data storage using a local `users.json` file.

## Requirements

* Python 3.x

## Setup

1. **Clone the repository (or download the files):**

    ```bash
    git clone git@github.com:Abdalr7man-ctrl/To-Do-List.git
    cd To-Do-List/Cli-Task-Tracker
    ```

    *If you don't use Git, simply download the project folder.*

2. **Navigate to the project directory:**

    Make sure your terminal is open in the `Cli-Task-Tracker` directory containing the Python files.

## Usage

1. **Run the application:**

    ```bash
    python3 main.py
    ```

2. **Login/Signup:**
    * The application will first ask if you have an account (`y/n`).
    * Follow the prompts to either log in with your existing username and password or create a new account.

3. **Commands:**
    Once logged in, you can use the following commands at the `>>` prompt:

    * `add <task_name>`: Adds a new task with the status "Not Done" by default.
        * *Example:* `add Finish project report`
    * `list done`: Displays all your done tasks with numbers.
    * `list not done`: Displays all your not done tasks with numbers.
    * `mark <task_name>`: Changes the status of an existing task. It will prompt you to enter the new status (`Done` or `Not Done`).
        * *Example:* `mark Finish project report` (then enter 'Done' when prompted)
    * `set_description <task_name>`: Allows you to add or edit the description for a task. It will prompt you for the new description.
        * *Example:* `set_description Finish project report` (then enter the description)
    * `delete <task_name>`: Removes a task from your list.
        * *Example:* `delete Old task`
    * `help`: Shows a list of available commands.
    * `exit`: Exits the application. It will ask if you want to save your changes (for existing users) or save your new account (for new users).

## File Structure

* `main.py`: The main entry point of the application. Handles the command-line interface, user input, and command execution using the `cmd` module.
* `model.py`: Defines the `User` and `Task` classes, containing the data structure and logic for managing users and tasks.
* `users.json`: The file used to store user account information and their associated tasks persistently.
