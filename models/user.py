#!/usr/bin/python3
"""
This modules gives the definition of the class User
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Define user by the following attributes inheriting from BaseModel
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
    def __init__(self, *args, **kwargs):
        """
        This initializes the User instance
        """
        super().__init__(*args, **kwargs)
