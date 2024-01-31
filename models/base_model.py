#!/usr/bin/python3
""" Parent Class"""

import models
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """
Parent Class init
    """

    def __init__(self, *args, **kwargs):
        """
        Pub inst Attr init

        Args:
            *args(agrs): the argumnets
            **kwargs(dict): attr values
        """
        dt_fromat = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method returns a dictionary containing all 
        keys/values of __dict__ instance
        """
        map_obj = self.__dict__.copy()
        map_obj['__class__'] = self.__class__.__name__
        map_obj['created_at'] = self.created_at.isoformat()
        map_obj['updated_at'] = self.updated_at.isoformat()
        return map_obj
