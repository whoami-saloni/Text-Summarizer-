import os
import yaml
from src.textSummarizer.logging import logger
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
#import base64


@ensure_annotations
def read_yaml(path_to_you:Path) ->ConfigBox:
    """
    Reads a YAML file and returns a Box object.

    Args:
        path_to_you (Path): Path to the YAML file.
    Raises:
        ValueError: If the YAML file is empty.
        e:empty file
    Returns:
        ConfigBox: ConfigBox type 
    """
    try:
        with open(path_to_you, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_you} loaded Successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"The YAML file {path_to_you} is empty.")
    
    except Exception as e:
        raise e


@ensure_annotations
def create_directory(path_to_directories:list,verbose=True):
    """
    Creates a list of directories.

    Args:
        path_to_directories (list): List of directories to be created.
        ignore_log(bool,optional):ignore if multiple directories to be created.Default to false.
    """
    for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory {path} created successfully.")


@ensure_annotations
def get_size(path: Path) -> str:
     """ get size in KB
     Args:
         path (Path): Path to file.
     Returns:
         str: size in KB.
     """
     size_in_KB = round(os.path.getsize(path)/1024)
     return f"~ {size_in_KB} KB"