#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """
    As requested this a basemodel class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
