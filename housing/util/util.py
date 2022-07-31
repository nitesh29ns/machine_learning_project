import yaml
from housing.exception import HousingException
import os , sys
from housing.constant import *



# In util.py file it has additional funcation which is not a part of our pipeline code..

def read_yaml_file(file_path:str) ->dict :
    try :
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
