#!/usr/bin/python3
"""
This is our amenity module
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Amenity instance
        """
        super().__init__(*args, **kwargs)

