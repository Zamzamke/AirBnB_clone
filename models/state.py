#!/usr/bin/python3
"""
This is the state module
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    State class inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes State instance
        """
        super().__init__(*args, **kwargs)

