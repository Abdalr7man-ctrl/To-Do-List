import cmd
import pyfiglet 
from model import User , Task


class ToDoList(cmd.Cmd):
    intro = "Welcom" # TODO : Use pyfiglet to add logo of (to do list app)
    prompt = ">>"
    
    def __init__(self):
        ...
        











if __name__ == "__main__" :
    print("Hello")
