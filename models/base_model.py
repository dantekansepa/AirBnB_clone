#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
This BaseModel Module is the foundation of our classes
The parent of all classes, so to speak
"""

class BaseModel():
    """
    This is our Base class for the project with the following methods as required:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        This class method initializes the attributes :random uuid, date created/updated
        :param args:
        :param kwargs:
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],"%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],"%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        The class method as required
        :return: the model's information as a string
        """
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        The class method as required
        :return: a string representation
        """
        return (self.__str__())

    def save(self):
        """
        The class method as required updates the current instance on the updated time and saves it to a serialized file
        :return:
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This class method as required
        :return: dictionary with string formats of time while also adding class information to the dictionary
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        return dic

