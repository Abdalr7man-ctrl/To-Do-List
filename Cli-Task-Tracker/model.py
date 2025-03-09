import uuid
import time
import json

class User :
    def __init__(self, name, password):
        self.name = name 
        self.password = password
        self.id = str(uuid.uuid4()) # random 32 char according to RFC 4122
        self.tasks = []

    def add_task(self, task:str):
        self.tasks.append(task)





class Task:
    def __init__(self, name, discreption):
        self.name = name 
        self.discreption = discreption
        self.status = "to-do"
        self.id = str(uuid.uuid4())
        self.created_at = time.ctime()

    def delet(self):
        ...

    def edit(self):
        ...




if __name__ == "__main__" :
    print(uuid.uuid4())
    print(time.ctime())