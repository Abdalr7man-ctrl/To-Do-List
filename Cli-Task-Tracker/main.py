#!python
import json
import cmd
from model import User , Task


class ToDoList(cmd.Cmd):
    intro = "Welcom To The To-Do_List" # TODO : Use pyfiglet to add logo of (to do list app)
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
            password = input("Enter your password: ")
            user = User(username, password)
            if not user :
                print("valid name or password")
                exit()
            self.user = user

        elif login == "y" : # TODO : Fix it 
            if user.name == username and user.password == password :
                self.user = user 
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
            if task.name == arg :
                task.edit_status()

    def do_delete(self, arg):
        """ Delete a task from the task manager """
        self.user.delete_task(arg)

    def do_exit(self, arg): # TODO : save user and Tasks before Close
        return True


if __name__ == "__main__" :
    ToDoList().cmdloop()