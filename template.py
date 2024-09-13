import os
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/exception/exception.py",
    "src/logger/logging.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",  # Added missing comma here
    "tox.ini",
    "experiment/experiments.ipynb"
]

for file in list_of_files:
    filepath = Path(file)  # Corrected variable use
    filedir, filename = os.path.split(filepath)
    
    if filedir:  # Check if filedir is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Check if file does not exist or is empty, and then create an empty file
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
