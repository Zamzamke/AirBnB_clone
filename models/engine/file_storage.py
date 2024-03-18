#!/usr/bin/python3
"""
This module will define a class used to manage the file storage for the AirBnB clone
"""
import json

class FileStorage:
    """
    This class manages the storage of the AirBnB clone models into JSON format
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """
        This returns dictionary of models currently in storage
        """
        return self.__objects
    
    def new(self, obj):
        """
        This adds new objects to the storage dictionary
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        """
        This saves the storage dictionary into a file
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        This loads the storage dictionary from the file
        """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_dict['__class__'] = class_name
                    obj_instance = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

