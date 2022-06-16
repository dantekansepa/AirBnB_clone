#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    This Class serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}
    def all(self):
        """
        This class method as requested returns dictionary of <class>.<id> : object instance
        :return: return self.__objects
        """
        return self.__objects

    def new(self, obj):
        """
        This class method as requested adds new objects to an existing dictionary of instances
        :param obj: object to added to dictionary
        :return:
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        This class method saves dictionary objects to JSON File
        :return:
        """
        my_dict = {}

        for key, obj in self.__objects.items():
            """
            In format key: value of dictionaries, in this case obj is the value assigned to key if it is dctionary
            """
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        This class method as requested converts dictionary objects from json file back to instances if the json file exists
        :return:
        """
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass






