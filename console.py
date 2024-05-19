#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program gracefully"""
        print()
        return True

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
