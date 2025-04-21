import os.path
import shutil

from textnode import *
from htmlnode import *
from extractors import *
from markdown import *

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
        raise Exception(f"Source: '{source}' does not exist...")
    
    # delete and recreate the destination 
    if os.path.exists(destination):
        shutil.rmtree(path=destination, ignore_errors=True)
    os.mkdir(destination)

    # copy the files...
    do_copy(source, destination)

    return True

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    if not os.path.exists(from_path):
        print(f"Input file '{from_path}' does not seem to exist...")
        return ""
    if not os.path.exists(template_path):
        print(f"Cannot find template file '{template_path}'")
        return ""
    if not os.path.exists(os.path.dirname(dest_path)):
        print(f"Destination directory '{os.path.dirname(dest_path)}' not found...")
        return ""
    
    with open(from_path) as f:
        md = f.read()

    with open(template_path) as f:
        template = f.read()

    page_title = extract_title(md)
    template = template.replace("{{ Title }}", page_title)
    page_html = markdown_to_html_node(md).to_html()
    template = template.replace("{{ Content }}", page_html)

    with open(dest_path, mode="w") as f:
        f.write(f"{template}")

    return page_title

def main():
    print("Welcome to the Static Site Generator!")
    result = clean_and_copy("./static", "./public")
    result = generate_page("./content/index.md", "./template.html", "./public/index.html")
    print(f"Finished creating HTML page for '{result}'!")
main()
