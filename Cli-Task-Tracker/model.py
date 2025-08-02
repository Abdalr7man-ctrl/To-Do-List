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

    def get(self):
        with open(self.FILEPATH, "r", encoding="utf-8") as f :
            data = json.load(f)
        for user in data:
            if self.name == user["name"] and self.password == user["password"]:
                return User(**user)
        return False

    def add_task(self, task_name: str, description_task: str = "No Description"):
        task = Task(task_name, description_task)
        self.tasks.append(task.__dict__)

    def list_tasks(self, status):
        task_number = 1
        for task in self.tasks:
            if task["status"] == status:
                print(f"{task_number}-{task['name']}")
                task_number += 1

    def delete_task(self, name_task) :
        for i in self.tasks :
            if i["name"].lower() == name_task.lower() :
                self.tasks.remove(i)


class Task:
    def __init__(self, name, description = "No Description", created_at = None, status = None):
        self.name = name
        self.created_at = created_at or ctime()
        self.description = description
        self.status = status or "Not Done"

    def edit_description(self):
        new_description = input(f"Write your new description for your task {self.name}:\n")
        self.description = new_description

    def task_info(self):
        return f"""The task: {self.name}
Created at: {self.created_at}
The status: {self.status}
Description: {self.description}"""


if __name__ == "__main__" :
    pass
