import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        The quit command to exit the program
        """
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        This exit the program when end of file is reached
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

        def do_create(self, arg):
        """
        This creates a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        This prints the string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objs:
            print("** no instance found **")
        else:
            print(objs[key])

    def do_destroy(self, arg):
        """
        This deletes an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objs:
            print("** no instance found **")
        else:
            del objs[key]
            storage.save()

    def do_all(self, arg):
        """
        This prints all string representation of all instances
        """
        objs = []
        if not arg:
            for obj in storage.all().values():
                objs.append(str(obj))
            print(objs)
            return
        elif arg not in storage.classes():
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                if arg in key:
                    objs.append(str(obj))
            print(objs)

    def do_update(self, arg):
        """
        This updates an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objs:
            print("** no instance found **")
        else:
            obj = objs[key]
            try:
                setattr(obj, args[2], eval(args[3]))
                obj.save()
            except AttributeError:
                pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
