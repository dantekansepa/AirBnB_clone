#!/usr/bin/python3
"""
This program contains the entry point to the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    This class is the entry point to the command interpreter
    """
    prompt = "(hbnb)"
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def do_EOF(self, line):
        """
        Exit the program on keyboard shortcut Ctr-D
        :param line:
        :return:
        """
        print()
        return True

    def do_quit(self, line):
        """
        Exit the program when you type keyword quit
        :param line:
        :return:
        """
        return True

    def emptyline(self):
        """
        An requested, an empty line + ENTER shouldnt execute anything.
        So it will overwrite default behaviour to repeat the most recent command
        :return:
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel saves it (to the JSON file) and prints the id
        :param self:
        :param line:
        :return:
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def parse(line):
        """Helper method to parse user typed input"""
        return tuple(line.split())


    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        :param line:
        :return:
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Destroy instance specified by user; Save changes to JSON file"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")
            

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name
        :return:
        """
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        :param line:
        :return: save the changes into JSON file
        """
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """
        This class method counts the number of instances specified E.G: number of users
        :param line:
        :return:
        """
        if line in HBNBCommand.classes:
            count = 0
            for key, objects in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unkown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.all(self, class_arg)
            elif command == 'count':
                HBNBCommand.count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.show(self, arg)
            elif command  == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))

            



    

if __name__ == "__main__":
    HBNBCommand().cmdloop()
