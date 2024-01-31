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
        """Handle empty line."""

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
            obj = eval(args)
            #storage.new(obj)
            obj.save()
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
                print("** no instance found **")

    def do_destroy(self, args):
        """ Delete a cls instance of an Id."""

        if len(args) == 0:
            print("** class name missing **")
            return
        arg = args.split()
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if len(arg) < 2:
                print("** instance id missing **")
                return
            name = "{}.{}".format(arg[0], arg[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[name]
                storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, args):
        """Display str rep of all instances of a class.
        If not class spcfd, display all inatantiated objcs."""

        arg = args.split()
        obj_lst = []
        if len(args) == 0:
            for objs in storage.all().values():
                obj_list.append(str(objs))
            print(obj_lst)
        elif arg[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if arg[0] in key:
                    obj_lst.append(str(objs))
            print(obj_lst)
        else:
            print("** class doesn't exist **")
    def do_update(self, objs):
        """Update cls instance of an ID by adding/updating 
        an att key pair/dict"""

        arg = args.split()
        if len(arg) >= 4:
            key = "{}.{}".format(arg[0], arg[1])
            cast = type(eval(arg[3]))
            arg3 = arg[3].strip('"').strip("'")
            setattr(storage.all()[key], arg[2], cast(arg3))
            storage.all()[key].save()
        elif len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(arg[0], arg[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()



