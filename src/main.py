import os.path
import shutil


from textnode import *
from htmlnode import *
from extractors import *

dir_level = -1
def clean_and_copy(source="./static", destination="./public"):
    global dir_level
    dir_level += 1

    if dir_level == 0:
        if os.path.exists(source):
            print(f"Path '{source}' exists!")
        else:
            print(f"Path '{source}' does not exist!")
            return False

        if os.path.exists(destination):
            shutil.rmtree(path=destination, ignore_errors=True)
        os.mkdir(destination)
    
        entries = os.listdir(source)
    
    return True



def main():
    print("Welcome to the Static Site Generator!")
    result = clean_and_copy("./static", "./public")
    print(f"Result is '{result}'!")

main()
