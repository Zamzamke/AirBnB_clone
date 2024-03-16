#!/usr/bin/python3
"""
Module Contains BaseModel class
"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class from which other models will be defined from
    """
    def __init__(self):
          self.id = str(uuid.uuid4())
          self.created_at = datetime.now()
          self.updated_at = datetime.now()

    def __str__(self):
         """
         Returns representation of a string in an informal way
         """
         return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__ )
    
    def save(self):
         """
         when an instance is changed,it updates updated_at with current datetime
         """
         self.updated_at = datetime.datetime.now()

    def to_dict(self):
         """
         Returns a dictionary with key/value pairs of __dict__ of the instances created.
         """
         dictionary = {}
         dictionary.update(self.__dict__)
         dictionary["__class__"] = self.__class__.__name__
         dictionary["created_at"] = self.created_at.isoformat()
         dictionary["updated_at"] = self.updated_at.isoformat()
         return dictionary
