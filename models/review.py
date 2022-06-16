#!/usr/binpython3
"""
This is Review class module
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    This Review class inherits from BaseModel as requested with following public attributes:
        place_id:            (str) will be Place.id
        user_id:             (str) will be User.id
        text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""

