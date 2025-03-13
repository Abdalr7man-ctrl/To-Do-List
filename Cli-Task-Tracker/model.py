import json
import uuid
import time

class User :
    _FILEPATH = r"/home/abdalrhman/All/Programing & CS/My_Projects/Todo_list/To-Do-List/Cli-Task-Tracker/users.json"
    def __init__(self, name, password, id=None, tasks=None):
        self.name = name 
        self.password = password
        self.id = id or str(uuid.uuid4()) # random 32 char according to RFC 4122
        self.tasks = tasks or []

    def is_there(self):
        with open(self._FILEPATH, "r") as f :
            file = f.read()
            data = json.loads(file)
            for user in data :
                if self.name == user["name"] and self.password == user["password"] :
                    return User(**user)
            return False

    def add_task(self, task_name:str, discreption_task:str = "No Discreption"):
        task = Task(task_name, discreption_task)
        self.tasks.append(task.__dict__)

    def list_tasks(self):
        for task in self.tasks :
            print(task["name"])

    def done_tasks(self):
        for task in self.tasks :
            if task["status"] == "Done" :
                print(task["name"])

    def inprogress(self):
        for task in self.tasks :
            if task["status"] == "Inprogress" :
                print(task["name"])

    def not_done(self):
        for task in self.tasks :
            if task["status"] == "Not Done" :
                print(task["name"])

    def delete_task(self, name_task) :
        for i in self.tasks :
            if i["name"].lower() == name_task.lower() :
                self.tasks.remove(i)
                i = None
class Task:
    def __init__(self, name, discreption = "No Discreption", created_at=None, status=None):
        self.name = name 
        self.created_at = created_at or time.ctime()
        self.discreption = discreption
        self.status = status or "Not Done"

    def edit_discreption(self):
        new_discreption = input(f"Write your new discreption for your task {self.name}:\n")
        self.discreption = new_discreption

    def task_info(self):
        return f"The task {self.name}\nIts created at {self.created_at}\nand The status is {self.status}"

if __name__ == "__main__" :
    ...