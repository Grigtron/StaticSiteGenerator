# hello world
import os
import shutil
from textnode import *
from htmlnode import *
from inline_markdown import *

def main():
    static_to_public_move("/home/grigaroni/workspace/github.com/Grigtron/static_site_generator/static", 
                      "/home/grigaroni/workspace/github.com/Grigtron/static_site_generator/public")


def static_to_public_move(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    else:
        shutil.rmtree(destination)
        os.mkdir(destination)
    
    entries = os.listdir(path=source)
    for entry in entries:
        entry_path = os.path.join(source, entry)
        dest_path = os.path.join(destination, entry)

        if os.path.isfile(entry_path):
            shutil.copy(entry_path, dest_path)
        elif os.path.isdir(entry_path):
            os.mkdir(dest_path)
            static_to_public_move(entry_path, dest_path)



if __name__ == "__main__":
    main()
