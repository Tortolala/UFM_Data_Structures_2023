'''
Module to write/read objects in pickle format.
'''
import pickle


def pickle_object(_object: any, file_path: str) -> None:

    with open(file_path, 'wb') as object_file:
        pickle.dump(_object, object_file, pickle.HIGHEST_PROTOCOL)
        
    return None


def unpickle_object(file_path: str) -> any:
    
    with open(file_path, 'rb') as object_file:
        _object = pickle.load(object_file)

    return _object
