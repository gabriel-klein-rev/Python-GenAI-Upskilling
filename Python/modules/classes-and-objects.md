# Python Module: Classes and Objects

> This file details how to use classes and objects in Python.

### Resources
* [Classes in Python](https://docs.python.org/3/tutorial/classes.html)
* [Multiple Inheritance and the Diamond Problem](https://en.wikipedia.org/wiki/Multiple_inheritance)

---

## Defining Classes and Objects

Classes and objects are key concepts in any object-oriented programming language. Since Python is a multi-paradigm programming language, it also supports the creation of classes and objects.

A **class** is a template that developers define and use to later create objects. This template might include properties for managing state and methods for altering this state. 

An **object** is an instance of a class. Each object follows the template laid out by the class, receiving its own copies of the class' properties.

## Creating Classes and Objects In Python

The syntax for creating a class in Python is as follows:

```
class MyClass:
    pass;
```

Here are few things to note about this class definition:

- You must use the `class` keyword before the class name.
- The naming convention for classes in Python follows **Pascal Case**.
- A class definition cannot be empty. If a class is defined and has no member functions or variables, use the `pass` keyword as a placeholder.
- Indentation is required when defining the any members within the scope of the class.

Of course, an empty class definition is not useful to us right now. We can add methods and state to our class as well:

```
class MyClass:
    prop1 = 0;
    prop2 = 'prop 2';

    def my_method(self):
        return self.prop1;
```
This updated example creates two properties and a method which simply prints a message to standard output. Take notice of the `self` parmeter which is defined as a method parameter. This is required within the context of a class as the `self` parameter allows developers to access the properties of a class. Note that the first parameter can technically be called anything of the developer's choice, but `self` is the conventional, descriptive choice.

With this class definition, we'll now create an instance of the class:

```
my_class_instance = MyClass();
```

Note the following:

- We've used a constructor to create the instance of our class. A call to a class' constructor follows the form of the class name followed by parentheses.
- We did not have to define this constructor in order to use it. A default constructor is provided if we do not specify a constructor.

### Constructors

Though Python developers can rely on the default constructor to create instances of classes, the default constructor is limited in its use. Programmers can't use it to provide default values to fields upon creating an object.

Take the previously defined class for example:

```
class MyClass:
    prop1 = 0;
    prop2 = 'prop 2';

    def my_method(self):
        return self.prop1;
```

It is not currently possible for a developer to create an instance of `MyClass` while simultaneously specifying the starting values of `prop1` and `prop2`. As such, we need a custom constructor that we can use to pass in starting values for these properties. The syntax for defining a constructor is as follows:

```
class MyClass:
    prop1 = 0;
    prop2 = 'prop 2';

    # Constructor definition
    def __init__(self):
        pass;

    def my_method(self):
        return self.prop1;
```

The constructor must be called `__init__` and developers must define a first parameter for the constructor, which is typically called `self`. The constructor currently has no logic, so let's define what our constructor should do.

```
class MyClass:
    prop1 = 0;
    prop2 = 'prop 2';

    # Constructor definition
    def __init__(self, prop1, prop2):
        self.prop1 = prop1;
        self.prop2 = prop2;

    def my_method(self):
        return self.prop1;
```

The constructor now accepts two additional parameters. The constructor's logic takes the values of this two parameters and assigns them to the class properties. If we did not use the `self` keyword, we would not have been able to access those class properties.

As an additional note, developers are not required to define class properties outside of constructors. For instance, the following code snippet is equivalent to the previous snippet in that it defines two class properties called `prop1` and `prop2`:

```
class MyClass:
    # Constructor definition
    def __init__(self, prop1, prop2):
        self.prop1 = prop1;
        self.prop2 = prop2;

    def my_method(self):
        return self.prop1;
```

It is important to remember that once you define a constructor, you can no longer use the default constructor. That is to say that you would not be able to legally call the default constructor.

### Accessing Class Properties

With the newly created instance, Python programmers can directly access the properties and methods that are defined at the class level:

```
my_class_instance = MyClass(1, 'Trainer Name');
my_class_instance.prop1 = 10;
my_class_instance.prop2 = 'Not Trainer Name';
my_class_instance.my_method();
```

This direct access is possible because there are no access modifiers in Python. Despite this lack of access modifiers, developers who wish to properties as if they were private members of a class prefix those property names with an underscore:

```
class MyClass:
    _prop1 = 0;
    _prop2 = 'prop 2';

    def my_method(self):
        return self._prop1;
```

Understand that this naming convention is just that: convention. It does not actually prevent direct access to a property. As such, the following code is syntactically valid:

```
my_class_instance = MyClass(1, 'Trainer Name');
my_class_instance._prop1 = 10;
my_class_instance._prop2 = 'Not Trainer Name';
my_class_instance.my_method();
```

## Child Classes and Inheritance

Like many other programming languages, Python supports inheritance by allowing developers to create child classes of existing classes. The syntax for creating a child class is as follows:

```
class MyClass:
    # Constructor definition
    def __init__(self, prop1, prop2):
        self.prop1 = prop1;
        self.prop2 = prop2;

    def my_method(self):
        return self.prop1;

class MyChildClass(MyClass):
    pass;
```

In this example, `MyChildClass` is a child class of `MyClass`. As such, it inherits properties and methods from its parent class.

It is worth noting that even the parent class, `MyClass` inherits from another class: `object`. It is implicitly the case that it extends the `object` class, so we do not have to write the following:

```
class MyClass(object):
    # Constructor definition
    def __init__(self, prop1, prop2):
        self.prop1 = prop1;
        self.prop2 = prop2;

    def my_method(self):
        return self.prop1;
```

**Fun Fact**: Python supports **multiple inheritance**. As a result, a class can inherit from several different classes. Some programming languages do not support multiple inheritance because of the "diamond problem" the feature brings about. In order to avoid this problem, Python changes method resolution orders dynamically.