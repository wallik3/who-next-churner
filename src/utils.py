from os import PathLike
import pickle
import json

def load_pkl_object(path:PathLike):
    """
    Load pickle object from model
    """
    with open(path, 'rb') as pickle_file:
        pkl_model = pickle.load(pickle_file)
    return pkl_model

def load_json(path:PathLike):
    with open(path, "r") as f:
        return json.load(f)
