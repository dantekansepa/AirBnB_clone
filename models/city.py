#!/usr/bin/python3
"""
This is a City class Module
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    This class inherits from BaseModel as requested with the following attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    state_id = ""
    name = ""

