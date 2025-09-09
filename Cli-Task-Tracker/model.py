import json
from time import ctime
from uuid import uuid4
from os.path import abspath, dirname, join


class User :
    FILEPATH = join(dirname(abspath(__file__)), "users.json")

    def __init__(self, name, password, id_=None, tasks=None):
        self.name = name
        self.password = password
        self.id_ = id_ or str(uuid4())
        self.tasks = tasks or []

    def get(self):
        """
        
        """
        with open(self.FILEPATH, "r", encoding="utf-8") as f :
            data = json.load(f)
        for user in data:
            if self.name == user["name"] and self.password == user["password"]:
                return User(**user)
        return False

    def add_user(self):
        with open(self.FILEPATH, "r", encoding="utf-8") as f :
            data = json.load(f)
        data.append(self.__dict__)
        with open(self.FILEPATH, "w", encoding="utf-8") as f :
            json.dump(data, f, indent=3)

    def delete_self(self):
        with open(self.FILEPATH, "r", encoding="utf-8") as f :
            data = json.load(f)
        for index in range(len(data)):
            if data[index]["id_"] == self.id_:
                data.pop(index)
        with open(self.FILEPATH, "w", encoding="utf-8") as f :
            json.dump(data, f, indent=3)

    def return_user(self):
        """
        
        """
        with open(self.FILEPATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        for user in data:
            if user["id_"] == self.id_ :
                return user

    def add_task(self, task_name: str, description_task: str = "No Description"):
        task = Task(task_name, description_task)
        with open(self.FILEPATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        for user in data:
            if user["id_"] == self.id_ :
                user["tasks"].append(task.__dict__)
        with open(self.FILEPATH, "w", encoding="utf-8") as f :
            json.dump(data, f, indent=3)

    def list_tasks(self, status):
        for task_number, task in enumerate(self.return_user()["tasks"], start=1):
            if task["status"].lower() == status.lower():
                print(f"{task_number}-{task['name']}")

    def delete_task(self, name_task):
        with open(self.FILEPATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        for user in data:
            if user["id_"] == self.id_ :
                for task in user["tasks"]:
                    if task["name"] == name_task:
                        user["tasks"].remove(task)
        with open(self.FILEPATH, "w", encoding="utf-8") as f :
            json.dump(data, f, indent=3)


class Task:
    def __init__(self, name, description = "No Description", id_=None, created_at = None, status = None):
        self.name = name
        self.id_ = id_ or str(uuid4())
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
