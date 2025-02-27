#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
#  from console.HBNBCommand import classes  # debug


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models ot one type of class, if given,
        or all classes currently in storage"""

        all_dict = {}

        if cls:
            #  if cls not in classes.values():
            #      print("** class doesn't exist **")
            #      return
            #  for key, val in FileStorage.__objects.items():
            for key, val in self.__objects.items():
                if key.split('.')[0] == cls.__name__:
                    all_dict.update({key: val})
            return all_dict

        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        #  print("object?----->???\n", obj)  # debug
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside
        - if obj is equal to None, the method should not do anything"""
        if obj is not None:
            #  print("Obj: b4 del:", obj)  # debug
            self.__objects.pop(obj.to_dict()['__class__'] + '.' + obj.id)
            #  print("Obj: aft4 del:", obj)  # debug
        pass

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            # print("temp?", temp)   debug
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
            # print("Saved????????")   debug

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
