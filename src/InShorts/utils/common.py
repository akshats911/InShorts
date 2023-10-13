import os
import yaml
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from InShorts.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directiories(path_to_directories: list, verbose=True):
    """Creates directories if they don't exist."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory {path} created successfully")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in kb"""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb}kb"