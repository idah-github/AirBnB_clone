#!/usr/bin/python3
"""File storageJSOn types serializes and deserializes """


from models.base_model import BaseModel
import json


class FileStorage:
    """Abstract storage engine
    Atributes:
    __file_path(str): file to save objs
    __objects(dict): a dic of instantiated objcts
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return obj dict"""

        return self.__objects

    def new(self,obj):
        """
        add obj to dict
        Args:
        objects: new object
        """
        clsnm = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clsnm, obj.id)] = obj

    def save(self):
        """
        serialize objescts to jsonfiles (__file_path)"""
        objdic = FileStorage.__objects
        objsdict = {obj: objdic[obj].to_dict() for obj in objdic.keys()}
        with open(FileStorage.__file_path, "w") as fl:
            json.dump(objsdict, fl)

    def reload(self):
        """Deserialises JSON files"""
        try:
            with open(self.__file_path, 'r') as fl:
                objdic = json.loads(fl.read())
                for objs in objsdict.values():
                    clas_name = objs["__class__"]
                    del objs["__class__"]
                    self.new(eval(clas_name)(**objs))
        except FileNotFoundError:
        #except Exception:
            return
