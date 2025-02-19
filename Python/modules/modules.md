# Python Module: Modules

> This file details what a Python module is and how a developer can create a module.

### Resources
* [Python Modules](https://docs.python.org/3/tutorial/modules.html)

---

## What Is A Module?

A Python module is a file that may contain definitions for classes, functions, and variables. This file has a *.py* extension.

Python modules allow developers to split program logic into several file for easy maintenance. They also provide a means of producing reusable code that can easily be imported for use at a later time.

## Creating a Module

In order to create a module, a developer should create a file that has the *.py* extension. This is all that is required for the creation of a module; there do not have to be any definitions inside of the module. After creating the module, the developer can proceed with placing definitions inside of the module as they see fit. The definitions inside of a module are typically related in a meaningful way, giving the module an overall purpose or use case.

Take the following module for example:

```
# This code is inside of a file called "my_module.py".

variable_introduction = "I'm a variable inside of a module!";

def introduce_module():
    print("Hi! I'm a function inside of a module!");

class ClassInModule:
    introduction = "I'm a class member inside of a class inside of a module!";
```

Note the following:

- The naming convention for a module is all lower case letters.
- Any valid objects can be defined at the module level.

## Importing Modules

Once a developer has created a module, they can import the module elsewhere in order to access functions, classes, and variables that are defined within the module:

```
This code is inside of a file called "other_module.py".

import my_module

# Using the function defined inside of my_module.py
my_module.introduce_module();
```

When importing a module, you do not include the file extension. Note also that importing other modules can get more complex than the above example as modules are often located in different [namespaces](./namespaces.md) for more clarity and to help avoid naming conflicts.