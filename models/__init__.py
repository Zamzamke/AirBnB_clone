#!/usr/bin/python3
"""
This module contains base files
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

