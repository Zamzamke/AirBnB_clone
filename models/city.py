#!/usr/bin/python3
"""
This is our city module
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherits from BaseModel
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes City instance
        """
        super().__init__(*args, **kwargs)

