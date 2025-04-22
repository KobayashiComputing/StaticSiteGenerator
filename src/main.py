import os.path
import shutil

from textnode import *
from htmlnode import *
from extractors import *
from markdown import *

def get_file_list(source):
     filelist = []
     entries = os.listdir(source)
     for entry in entries:
         path = os.path.join(source, entry)
         if os.path.isdir(path):
             filelist.extend(get_file_list(path))
         if os.path.isfile(path):
             filelist.append(path)
     return filelist

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
        # os.mkdir(os.path.dirname(dest_path))
        create_dir_path(os.path.dirname(dest_path))
        # print(f"Destination directory '{os.path.dirname(dest_path)}' not found...")
    
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

def create_dir_path(path):
    parts = path.split('/')
    path2 = ""
    for part in parts:
        if not part == '.':
            path2 += part
            if not os.path.exists(path2):
                os.mkdir(path2)
            path2 += '/'

        pass
    pass
    return True

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = get_file_list(dir_path_content)
    for file in files:
        dfile = file.replace("./content", "./public", 1)
        dfile = dfile.replace(".md", ".html", 1)
        generate_page(file, template_path, dfile)
        pass
    pass
    return True

def main():
    # Welcome message...
    print("Welcome to the Static Site Generator!")

    # Clean out and populate the destination directory...
    result = clean_and_copy("./static", "./public")

    # Generate the page(s)...
    result = generate_pages_recursive("./content", "./template.html", "./public")
    # result = generate_page("./content/index.md", "./template.html", "./public/index.html")
    
    print(f"Finished creating HTML page for '{result}'!")
main()
