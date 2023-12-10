#1/usr/bin/python3
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
    __objects == {}

    def all(self):
        """Return obj dict"""

        return self.__objects

    def new(self,objs):
        """
        add obj to dict
        Args:
        objs: new object
        """

        self.__objects[object.__class__.__name__+ '.' + str(object)] = object

    def save(self):
        """
        serialize objescts to jsonfiles (__file_path)"""
        objdic = FileStorage.__objects
        objsdict = {objs: objdic[objs].to_dict() for objs in objcdic.keys()}
        with open(FileStorage>__file_path, "w") as file:
            json.dump(objsdict, file)

    def reload(self):
        """Deserialises JSON files"""

        try:
            with open(self.__file_path, 'r') as file:
                dict = json.loasds(file.read())
                for value in dict.values():
                    clas_name = value["__class__"]
                    self.new(eval(clas_name)(**value))
        #except FileNotFoundError:
        except Exception:
            return
