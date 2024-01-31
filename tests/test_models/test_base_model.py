#!/usr/bin/python3
"""
unittests for base model
"""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """tests modules in BaseModel"""
    @classmethod
    def setUpClass(cls):
        """sets up an istance"""
        cls.base1 = BaseModel()
        cls.base1.name = "Greg"
        cls.base1.my_number = 29

    @classmethod
    def tearDownClass(cls):
        """deletes the instance"""
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_functions_available(self):
        """checks if class has functions"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """checks if attributes are present"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """checks if init is called"""
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
        """checks if save updates updated_at"""
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        """checks if to_dict creates a dict with keys below"""
        base1_dict = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
