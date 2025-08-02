import json
import cmd
import hashlib
from model import User, Task

class ToDoList(cmd.Cmd):
    intro = "Welcome To The To-Do_List App"
    prompt = ">> "

    def __init__(self):
        super().__init__()
        self.user = None
        self.do_login()

    def do_login(self):
        """
        do login for the app
        by use the password & name
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
        """ Add a task to the task manager"""
        # TODO: improve the method
        self.user.add_task(arg)

    def do_list(self, arg):
        """ List all tasks in the task manager"""
        self.user.list_tasks()

    def do_done(self, arg) :
        """ List done tasks in the task manager"""
        self.user.done_tasks()

    def do_inProgress(self, arg):
        """ List in progress tasks in the task manager """
        self.user.inProgress()

    def do_mark(self, arg):
        """ Mark a task as completed or In progress"""
        for task in self.user.tasks :
            if task["name"] == arg :
                new_status = input("write your new status --> Done , In progress, Not Done:\n")
                if new_status.lower() == "done" :
                    task["status"] = "Done"
                elif new_status.lower() == "In progress" :
                    task["status"] = "In progress"
                elif new_status.lower() == "not done" :
                    task["status"] = "Not Done"

    def do_delete(self, arg):
        """ Delete The task of the user from the task manager"""
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
        save_changes = input("Do you want to save your changes.(y/n): ").lower().strip()
        if save_changes == "y" :
            with open(self.user.FILEPATH, "r", encoding="utf-8") as f :
                data = json.load(f)

            if self.user.get() :
                for user in data :
                    if user["id_"] == self.user.id_ :
                        data.remove(user)
            data.append(self.user.__dict__)

            with open(self.user.FILEPATH, "w", encoding="utf-8") as f :
                json.dump(data, f, indent=3)
        return True

if __name__ == "__main__" :
    # TODO: rewrite the commit message :)
    # XXX: json.loads after f.read() & json.load directly after open the file add this for JSON explain File
    # as a Note

    ToDoList().cmdloop()
