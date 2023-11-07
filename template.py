import os
from pathlib import Path
import logging

# Initiate logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Cocci_Classifier"

# List of directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath) # Creating a path with filepath
    filedir, filename = os.path.split(filepath) # Spliting filepath into directory and file


    if filedir !="": # If filedir does not exist
        os.makedirs(filedir, exist_ok=True) # Crreating the file directory
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    # Creating the files in the directory
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # Create file If the file does not exist or if the file is empty
        with open(filepath, "w") as f: # Creating an empty file with a writing permission
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")