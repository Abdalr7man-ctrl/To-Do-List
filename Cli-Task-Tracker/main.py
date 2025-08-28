import cmd
import hashlib
from model import User, Task

class ToDoList(cmd.Cmd):
    intro = "Welcome To The To-Do_List App"
    prompt = ">> "

    def __init__(self):
        super().__init__()
        self.user = None
        self.do_login(None)

    def do_login(self, arg):
        """
        do login for the app
        by use the password & the name
        """
        while True:
            user_input = input("Do you have an account? (y/n): ").lower().strip()
            if user_input not in ['y', 'n']:
                print("Invalid choose y or n.")
                continue
            username = input("Enter your username: ")
            password = hashlib.sha256(input("Enter your password: ").encode(encoding="utf-8")).hexdigest()
            user = User(username, password)
            is_user_there = user.get()
            if user_input == "n" and is_user_there:
                print("Invalid name or password")
                exit()
            elif user_input == "n":
                self.user = user
                break
            if user_input == "y" and is_user_there:
                self.user = is_user_there
                break
            else:
                print("Invalid input")
                exit()

    def do_add(self, arg):
        """
        Add a task to the Not Done tasks list
        Syntax: add <task_name>
        """
        self.user.add_task(arg)

    def do_list(self, arg):
        """ 
        list the tasks according to the status
        syntax:
         - list Done --> it will print all Done Tasks
         - list Not Done --> it will print all Not Done Tasks
        """
        self.user.list_tasks(arg)

    def do_mark(self, arg):
        """
        Mark a task as Done or Not Done
        syntax: mark <task_name>
        """
        for task in self.user.tasks :
            if task["name"] == arg :
                new_status = input("write your new status --> Done , Not Done:\n")
                if new_status.lower() == "done":
                    task["status"] = "Done"
                elif new_status.lower() == "not done":
                    task["status"] = "Not Done"
                break
        else:
            print(f"The task {arg} not found.")

    def do_delete(self, arg):
        """Delete The task of the user from the task manager"""
        self.user.delete_task(arg)

    def do_set_description(self, arg):
        for task in self.user.tasks :
            if task["name"] == arg :
                new_description = input("Set New Description for your Task.\n")
                task["description"] = new_description

    def do_task_info(self, arg):
        for task in self.user.tasks :
            if task["name"] == arg :
                task = Task(**task)
                print(task.task_info())

    def do_exit(self, arg):
        return True

if __name__ == "__main__" :
    # TODO: InProgress status of the task
    # TODO: tasks with the same name! use ID!!
    # TODO: use table to show the tasks
    # TODO: UX with commands commands & UI :D

    ToDoList().cmdloop()
