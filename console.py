#!/usr/bin/python3

""" The Hbnb cmd interpreter; entry point """


import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def handle_empty(args):
        """
        Handle empty line
        """

        pass

    def do_quit(self, args):
        """Handle shell exit,quit"""
        return True

    def do_EOF(self, args):
        """EOF to exit program."""
        print("")
        return True

    def do_create(self,args):
        """
        Method creating BaseModel new instance and prints its ID.

        Args:
        args: Arguments to enter with cmd

        """

        if len(args) == 0:
            print("** class name missing **")

        elif args not in HBNBCommand.__classes:
            print("**class does nit exist **")

        else:
            obj = self.classes[args]()
            models.storage.save()
            print(obj.id)

    def do_show(self, args):
        """Display str rep of class inst of an id"""

        if not args:
            print ("** class name missing **")

            arg_list = args.split()
        if arg_list[0] not in self.__classes:
            print("** class doesn't exist **")

        elif len(arg_list) < 2:
            print ("** instance id missing **")

        else:
            instance_key = "{}.{}".format(arg_list[0], arg_list[1])
            all_instances = storage.all()

            if instance_key in all_instances:
                print(all_instances[instance_key])
            else:
                print("** no instance found **"")


