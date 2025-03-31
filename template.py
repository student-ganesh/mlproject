import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)
project_name = "mlproject"

list_of_files = [
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py"
    f"src/{project_name}/component/data_ingestion.py",
    f"src/{project_name}/component/data_transformation.py",
    f"src/{project_name}/component/model_trainer.py",
    f"src/{project_name}/component/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/exception.py",
    f"src/{project_name}/pipeline/logger.py",
    f"src/{project_name}/pipeline/util.py",
    "app.py"
    "Dockerfile"
    "requirement.txt"
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != " ":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")

    if(not os.path.exists(filepath) or os.path.getsize(filepath == 0)):
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
