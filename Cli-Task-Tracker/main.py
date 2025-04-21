import os
import json
import cmd
import hashlib
from model import User, Task
# TODO : Use import rich.console to color the text.

class ToDoList(cmd.Cmd):
    _FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.json")
    intro = "Welcom To The To-Do_List"
    prompt = ">> "
    def __init__(self):
        super().__init__()
        self.user = None
        self.do_login()

    def do_login(self):
        """Login to the To Do List Cli App"""
        login = input("Do you have an account? (y/n): ").lower().strip()
        if login == "n" :
            username = input("Enter your username: ")
            password = hashlib.sha256(input("Enter your password: ").encode(encoding="utf-8")).hexdigest()
            user = User(username, password)
            if user.is_there() :
                print("valid name or password")
                exit()
            else :
                self.user = user
        elif login == "y" :
            username = input("Enter your username: ")
            password = hashlib.sha256(input("Enter your password: ").encode(encoding="utf-8")).hexdigest()
            user = User(username, password)
            if user.is_there() :
                self.user = user.is_there()
            else :
                print("valid input")
                exit()

    def do_add(self, arg):
        """ Add a task to the task manager """
        self.user.add_task(arg)

    def do_list(self, arg):
        """ List all tasks in the task manager """
        self.user.list_tasks()

    def do_done(self, arg) :
        """ List done tasks in the task manager """
        self.user.done_tasks()

    def do_inprogress(self, arg):
        """ List inprogress tasks in the task manager """
        self.user.inprogress()

    def do_mark(self, arg):
        """ Mark a task as completed or Inprogress"""
        for task in self.user.tasks :
            if task["name"] == arg :
                new_status = input("write your new status --> Done , Inprogress, Not Done:\n")
                if new_status.lower() == "done" :
                    task["status"] = "Done"
                elif new_status.lower() == "inprogress" :
                    task["status"] = "Inprogress"
                elif new_status.lower() == "not done" :
                    task["status"] = "Not Done"

    def do_delete(self, arg):
        """ Delete The task of the user from the task manager """
        self.user.delete_task(arg)

    def do_setdiscreption(self, arg):
        for task in self.user.tasks :
            if task["name"] == arg :
                new_descreption = input("Set New Descreption for your Task.\n")
                task["status"] = new_descreption

    def do_task_info(self, arg):
        for task in self.user.tasks :
            if task["name"] == arg :
                task = Task(**task)
                print(task.task_info())

    def do_exit(self, arg):
        if self.user.is_there() :
            save = input("Do you want to save your changes.(y/n): ").lower().strip()
            if save == "y" :
                with open(self._FILEPATH, "r", encoding="utf-8") as f :
                    data = json.load(f)
                for user in data :
                    if user["id_"] == self.user.id_ :
                        data.remove(user)
                data.append(self.user.__dict__)
                with open(self._FILEPATH, "w", encoding="utf-8") as f :
                    json.dump(data, f, indent=3)
        else :
            save = input("Do you want to save your new account.(y/n): ").lower().strip()
            if save == "y" :
                with open(self._FILEPATH, "r", encoding="utf-8") as f :
                    data = json.load(f)
                data.append(self.user.__dict__)
                with open(self._FILEPATH, "w", encoding="utf-8") as f :
                    json.dump(data, f, indent=3)
        return True

if __name__ == "__main__" :
    ToDoList().cmdloop()
