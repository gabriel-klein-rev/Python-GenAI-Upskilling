# Python Module: Namespaces

> This file details what a namespace is and how to create and take advantage of namespaces.

### Resources:
* [Namespaces](https://docs.python.org/3/tutorial/classes.html)

---

## What Is A Namespace?

Python defines a namespace as "[a mapping from names to objects](https://docs.python.org/3/tutorial/classes.html)". To put it simply, namespaces are the reason that names can be reused in various modules and functions.

Some examples of namespaces include:

- global names within a module
- local names that exist within functions
- the collection of [built-in names](https://docs.python.org/3/library/functions.html) available for use in Python

## Defining a Namespace

Many developers likely do not create namespaces for the sake of creating namespaces. They create modules and functions which act as namespaces by default.

Take the following code snippets for example:

**Snippet 1**:

```
# This code is inside of a file called "my_module.py".

variable_introduction = "I'm a variable inside of a module!";

def introduce_module():
    print("Hi! I'm a function inside of a module!");

class ClassInModule:
    introduction = "I'm a class member inside of a class inside of a module!";
```

**Snippet 2**:

```
This code is inside of a file called "other_module.py".

import my_module

# Using the function defined inside of my_module.py
my_module.introduce_module();
```

Both snippets define modules. These modules serve as namespaces regardless of whether or not that's our intention.

Since these modules are namespaces, we can freely define functions and variables without worrying about naming conflicts. For instance, let's say that we want to define a function called `no_conflict` in *both* modules:

**Snippet 1**:

```
# This code is inside of a file called "my_module.py".

variable_introduction = "I'm a variable inside of a module!";

def introduce_module():
    print("Hi! I'm a function inside of a module!");

def no_conflict():
    pass;

class ClassInModule:
    introduction = "I'm a class member inside of a class inside of a module!";
```

**Snippet 2**:

```
This code is inside of a file called "other_module.py".

import my_module

# Using the function defined inside of my_module.py
my_module.introduce_module();

def no_conflict():
    pass;
```

Because both function definitions are in separate namespaces, the existence of both functions is legal. As such, we could invoke both functions from within `other_module.py` with no problems:

```
This code is inside of a file called "other_module.py".

import my_module

# Using the function defined inside of my_module.py
my_module.introduce_module();

def no_conflict():
    pass;

# Calls the local no_conflict function
no_conflict();

# Calls the no_conflict function from the imported module
my_module.no_conflict();
```