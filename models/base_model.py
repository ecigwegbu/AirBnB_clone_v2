#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #  storage.new(self)  # debug
        else:
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)
            if 'created_at' in kwargs:
                try:
                    kwargs['created_at'] = datetime.strptime(
                            kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                except Exception:
                    pass
            else:
                self.created_at = datetime.now()

            if 'updated_at' in kwargs:
                try:
                    kwargs['updated_at'] = datetime.strptime(
                            kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                except Exception:  # date error
                    pass
            else:
                self.updated_at = datetime.now()

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

            # del kwargs['__class__']
            self.__dict__.update(kwargs)

        #  print("About to call save in constructor ....")  # debug
        self.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        #  print("~~~~~~~~~saving..............")  # debug
        storage.new(self)  # debug  # register object with storage
        storage.save()  # serialize ( to_dict())and save all objects in memory

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        #  print("DDDDDD__dict__when raw", self.__dict__)  #  debug
        dictionary.update(self.__dict__)
        #  parse eg 'models.place.Place'  :
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        #  print("AfterTo_Dict:", dictionary)  # debug
        return dictionary
