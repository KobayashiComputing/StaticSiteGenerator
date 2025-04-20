import os.path
import shutil


from textnode import *
from htmlnode import *
from extractors import *

def do_copy(source, destination):
    entries = os.listdir(source)
    for entry in entries:
        path = os.path.join(source, entry)
        if os.path.isdir(path):
            dpath = os.path.join(destination, entry)
            os.mkdir(dpath)
            do_copy(path, dpath)
        if os.path.isfile(path):
            shutil.copy2(path, destination)
    pass
    return True


def clean_and_copy(source="./static", destination="./public"):
    # check to make sure the source exists...
    if not os.path.exists(source):
        raise Exception("Source: {source} does not exist...")
    
    # delete and recreate the destination 
    if os.path.exists(destination):
        shutil.rmtree(path=destination, ignore_errors=True)
    os.mkdir(destination)

    # copy the files...
    do_copy(source, destination)

    return True



def main():
    print("Welcome to the Static Site Generator!")
    result = clean_and_copy("./static", "./public")
    print(f"Result is '{result}'!")

main()
