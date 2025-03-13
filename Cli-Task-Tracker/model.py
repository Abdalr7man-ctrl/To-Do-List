import json
import uuid
import time
class User :
    _FILEPATH = r"/home/abdalrhman/All/Programing & CS/My_Projects/Todo_list/To-Do-List/Cli-Task-Tracker/Data/users.json"
    def __init__(self, name, password):
        self.name = name 
        self.password = password
        self.id = str(uuid.uuid4()) # random 32 char according to RFC 4122
        self.tasks = []
        self.is_there()

    def is_there(self):
        with open(self._FILEPATH, "r") as f :
            file = f.read()
            data = json.loads(file)
            for user in data :
                if self.name in user and self.password in user :
                    return True
                else :
                    return False

    def add_task(self, task_name:str, discreption_task:str = "No Discreption"):
        task = Task(task_name, discreption_task)
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks :
            print(task.name)

    def done_tasks(self):
        for task in self.tasks :
            if task.status == "Done" :
                print(task.name)

    def inprogress(self):
        for task in self.tasks :
            if task.status == "Inprogress" :
                print(task.name)

    def not_done(self):
        for task in self.tasks :
            if task.status == "Not Done" :
                print(task.name)

    def delete_task(self, name_task) :
        for i in self.tasks :
            if i.name.lower() == name_task.lower() :
                self.tasks.remove(i)
                i = None
class Task:
    _FILEPATH = r"/home/abdalrhman/All/Programing & CS/My_Projects/Todo_list/To-Do-List/Cli-Task-Tracker/Data/tasks.json"
    def __init__(self, name, discreption = "No Discreption"):
        self.name = name 
        self.created_at = time.ctime()
        self.discreption = discreption
        self.status = "Not Done"

    def edit_discreption(self):
        new_discreption = input(f"Write your new discreption for your task {self.name}:\n")
        self.discreption = new_discreption

    def edit_status(self):
        new_status = input("write your new status --> Done , Inprogress, Not Done:\n")
        if new_status.lower() == "done" :
            self.status = "Done"
        elif new_status.lower() == "inprogress" :
            self.status = "Inprogress"
        elif new_status.lower() == "not done" :
            self.status = "Not Done"

    def task_info(self):
        return f"The task {self.name}\nIts created at {self.created_at}\nand The status is {self.status}"


if __name__ == "__main__" :
    print(uuid.uuid4())
    print(time.ctime())
    abdo = User("Abdalrhman", "2004/6/1//")
    abdo.add_task("play game", "i will play pes")
    abdo.add_task("study", "i will study math")
    abdo.add_task("visit", "i will visit the Family")
    print(abdo.tasks[0].task_info())
    print(abdo.tasks[0].status)
    # abdo.list_tasks()
    abdo.delete_task("visit")
    # abdo.list_tasks()
    # abdo.tasks[0].edit_status()
    abdo.done_tasks()
    abdo.inprogress()
    print(abdo.__dict__)
