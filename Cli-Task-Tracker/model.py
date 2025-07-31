import os
import json
from time import ctime
from uuid import uuid4


class User :
    FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.json")

    def __init__(self, name, password, id_=None, tasks=None):
        self.name = name
        self.password = password
        self.id_ = id_ or str(uuid4())
        self.tasks = tasks or []

    def is_there(self):
        with open(self.FILEPATH, "r", encoding="utf-8") as f :
            file = f.read()
            data = json.loads(file)
            for user in data :
                if self.name == user["name"] and self.password == user["password"] :
                    return User(**user)
            return False

    def add_task(self, task_name:str, description_task:str = "No Description"):
        task = Task(task_name, description_task)
        self.tasks.append(task.__dict__)

    def list_tasks(self):
        for num, task in enumerate(self.tasks,1) :
            print(f"{num}){task['name']}")

    def done_tasks(self):
        num = 1
        for task in self.tasks :
            if task["status"] == "Done" :
                print(f"{num}-{task['name']}")
                num += 1

    def inProgress(self):
        num = 1
        for task in self.tasks :
            if task["status"] == "InProgress" :
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
    def __init__(self, name, description = "No Description", created_at=None, status=None):
        self.name = name
        self.created_at = created_at or ctime()
        self.description = description
        self.status = status or "Not Done"

    def edit_description(self):
        new_description = input(f"Write your new description for your task {self.name}:\n")
        self.description = new_description

    def task_info(self):
        return f"The task: {self.name}\nCreated at: {self.created_at}\nThe status: {self.status}\nDescription: {self.description}"


if __name__ == "__main__" :
    pass
