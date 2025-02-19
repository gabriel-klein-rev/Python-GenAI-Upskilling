# Python Module: Dunder Methods

> This file details what a dunder method is and how to use dunder methods.

### Resources
* [Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)

---

## What Is A Dunder Method?

A dunder method is a method that allows a class to define its own behavior with respect to valid Python language operators. In other words, dunder methods allow for operator overloading. This operator overloading permits classes to emulate built-in types.

Note that the term "dunder" is not used in Python's official documentation; the official documentation simply refers to these methods as methods with "special names". The term "dunder" is simply a colloquial abbreviation for "double underscore" since dunder methods' names are prefixed *and* suffixed with two underscores. A few sources might also call dunder methods "magic methods".

Regardless of the name used to refer to dunder methods, the developer should understand that they do not define dunder methods themselves. In fact, these methods are inherited from the `object` class. As a result, any class which inherits from `object` &mdash; which is every class in Python &mdash; can provide its own implementation of these methods.

Examples of dunder methods include:

- \__init__: called after an instance of a class been created
- \__str__: provides a printable string representation of an object
- \__lt__: allows for operator overloading of the `<` symbol
- \__gt__: allows for operator overloading of the `>` symbol

## How To Use A Dunder Method

In order to take advantage of dunder methods, a developer should first define a class. As such, we've defined the following class:

```
class Teenager:
    _moody = True;

    def __init__(self, age, height):
        self.age = age;
        self.height = height;
```

We've already overridden the **\__init__** method as we typically would in any class. That said, we'll override another method that will make the benefits of using dunder methods for operator overloading clear. 

Before doing so, however, let's imagine that we want to compare two instances `Teenager`. If, for instance, we wanted to compare two instances of the class based on which instance has a higher value for the `age` property, perhaps we'd want to write the following code:

```
teen_one = Teenager(13, 65);
teen_two = Teenager(15, 70);

# This raises a TypeError
if teen_one > teen_two:
    print('Teen one is teen two's senior.');
else:
    print('Teen two is teen one's senior.);
```

Unfortunately, the above code will raise a `TypeError` because there is no built-in way of comparing instances of the `Teenager` class using this operator. As a result, we have to tell Python how to compare instances of the class when using this operator. In order to do so, we'll use the **\__gt__** method:

```
class Teenager:
    _moody = True;

    def __init__(self, age, height):
        self.age = age;
        self.height = height;

    def __gt__(self, other):
        if self.age > other.age:
            return True;
        else:
            return False;
```

We've implemented the dunder method in such a way that it uses each instance's `age` property to determine which instance is "greater".

With the addition of the **\__gt__** method, we should now be able to legally use the `>` operator to compare instances of `Teenager`:

```
teen_one = Teenager(13, 65);
teen_two = Teenager(15, 70);

# This prints "Teen two is teen one's senior."
if teen_one > teen_two:
    print('Teen one is teen two's senior.');
else:
    print('Teen two is teen one's senior.);
```