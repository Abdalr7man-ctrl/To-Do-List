import os
import json
import uuid
import time

class User :
    _FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.json")
    def __init__(self, name, password, id_=None, tasks=None):
        self.name = name
        self.password = password
        self.id_ = id_ or str(uuid.uuid4()) # random 32 char according to RFC 4122
        self.tasks = tasks or []

    def is_there(self):
        with open(self._FILEPATH, "r", encoding="utf-8") as f :
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
        for num, task in enumerate(self.tasks,1) :
            print(f"{num}-{task['name']}")

    def done_tasks(self):
        num = 1
        for task in self.tasks :
            if task["status"] == "Done" :
                print(f"{num}-{task['name']}")
                num += 1

    def inprogress(self):
        num = 1
        for task in self.tasks :
            if task["status"] == "Inprogress" :
                print(f"{num}-{task['name']}")
                num += 1

    def not_done(self):
        for task in self.tasks :
            if task["status"] == "Not Done" :
                print(task["name"])

    def delete_task(self, name_task) :
        for i in self.tasks :
            if i["name"].lower() == name_task.lower() :
                self.tasks.remove(i)

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
    pass
