import os
from pathlib import Path
import logging
import shutil

# Setting up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = 'Movie_RecSys'

# List of all files and directories to be created in the project
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/data_pipeline.py",
    f"src/{project_name}/pipeline/model_pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/data_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "config/params.yaml",
    "schema.yaml",
    "data/raw/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",
    "data/external/.gitkeep",
    "tests/test_data_pipeline.py",
    "tests/test_model_pipeline.py",
    "tests/test_example.py",
    "scripts/preprocess.py",
    "scripts/train.py",
    "reports/figures/.gitkeep",
    "docs/architecture.md",
    "docs/usage.md",
    "templates/index.html",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
]

# Create directories and files as per the project structure
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

# Define the source directory where the template files are located
template_dir = "/Users/mak/Documents/Personal/Movie_RecSys/CRISP-DM_Template"  # Path to the notebooks

# Define the destination directory in your project for notebooks
notebook_dest_dir = "/Users/mak/Documents/Personal/Movie_RecSys/research"

# List of notebooks to be copied from the template directory
notebooks = [
    "01_business_understanding.ipynb",
    "02_data_understanding.ipynb",
    "03_data_preparation.ipynb",
    "04_modeling.ipynb",
    "05_evaluation.ipynb",
    "06_deployment.ipynb"
]

# Create the destination directory if it doesn't exist
os.makedirs(notebook_dest_dir, exist_ok=True)

# Copy the notebooks from the template directory to the project notebook directory
for notebook in notebooks:
    src_path = Path(template_dir) / notebook  # Correctly pointing to the notebook file
    dest_path = Path(notebook_dest_dir) / notebook

    if not dest_path.exists():
        if src_path.exists():
            shutil.copy(src_path, dest_path)
            logging.info(f"Copied {notebook} to {notebook_dest_dir}")
        else:
            logging.error(f"Source file {src_path} does not exist!")
    else:
        logging.info(f"{notebook} already exists in {notebook_dest_dir}")