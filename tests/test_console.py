#!/usr/bin/python3
"""
Unittest for console command interpreter
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):

    """Unittest for command interpreter"""
    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    """Check for docstring existance"""
    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_docstrings_in_test_console(self):
        """Test docstrings exist in test_console.py"""
        self.assertTrue(len(self.__doc__) >= 1)

    """Test command interpreter outputs"""
    def test_handle_empty(self):
        """Test no user input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    def test_create(self):
        """Test cmd output: create"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("create User")  # not used
            self.typing.onecmd("create User")  # just need to create instances

    def test_all(self):
        """Test cmd output: all"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("all NonExistantModel")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())

    def test_destroy(self):
        """Test cmd output: destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_update(self):
        """Test cmd output: update"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_show(self):
        """Test cmd output: show"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("show Review")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_class_cmd(self):
        """Test cmd output: <class>.<cmd>"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("User.count()")
            self.assertEqual(int, type(eval(f.getvalue())))


if __name__ == "__main__":
    unittest.main()
