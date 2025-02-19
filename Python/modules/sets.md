# Python Module: Sets

> This file details the features of a set and how to use sets in Python.

### Resources:
* [Sets](https://docs.python.org/3/tutorial/datastructures.html)
* [Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

---

## What Is A Set?

A set is an unordered collection of items. Sets are often contrasted with [lists](./lists.md) as some of the collection's features are the opposite of those of a standard list.

Some notable features of a set include:

- **Mutability**: Like lists, sets are mutable. Developers can freely add and remove elements from a set using the standard Python library.
- **No Guaranteed Order**: Unlike lists, sets do not preserve the order of the elements they contain.
- **No Random Access**: Sets do not support random access. As such, a developer cannot access an element within a set by its index.
- **No Support For Duplicates**: Set do not allow for duplicates. As a result, programmers often use sets to remove duplicates from an existing collection.

## Creating and Using Sets

The syntax for creating a set in Python is as follows:

```
# A set of numbers
my_set = {1, 2, 3};
```

The above code snippets creates a simple set of three integers using a simple syntax. Despite this easy syntax, there is one "trick" to using sets in Python. Take a look at the following code:

```
# Not a set
my_set = {};
```

A programmer who is not familiar with Python might think that this snippet creates an empty set. Unfortunately, this code instead creates an empty [dictionary](./dictionaries.md). If a developer wants to create an empty set, they should use the set constructor like so:

```
my_set = set();
```

## Accessing A Set Element

Let's imagine that we have our existing set of integers as defined in the example above:

```
# A set of numbers
my_set = {1, 2, 3};
```

For a fresh Python developer who wants to access the first element of the set, writing the following code is tempting:

```
# A set of numbers
my_set = {1, 2, 3};
# Not valid
my_set[0];
```

As we mentioned earlier, programmers are not permitted to access elements by their index in Python. They must instead iterate over the set if they wish to access its elements:

```
# A loop that prints each element in the set
for el in my_set:
    print(el);
```

There are several more useful operations a developer can perform while using sets. View the official Python documentation for a complete list of [common sequence operations](https://docs.python.org/3/library/stdtypes.html#typesseq-common) available to Python programmers.