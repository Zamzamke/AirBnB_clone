#!/usr/bin/python3
"""
test documentation of our base models
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime
import json
import os

class test_base_model(unittest.TestCase):
    """
    Tests the base model
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
        
    def test_save(self):
        """ 
        It tests save method
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        It checks if string documentation matches the expected output
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """
        It checks if the returned dictionary matches the expected format
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        
    def test_id(self):
        """ 
        Tests id properties of the base models
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()
