# Python Module: Lists

> This file details the features of a list and how to use lists in Python.

### Resources:
* [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

---

## What Is A List?

A list is a mutable sequence of items. Developers typically use lists to store a collection of related items. For instance, if a developer creates a custom type, they can store instances of that type inside of a list object.

Some notable features of a list include:

- **Mutability**: Lists are mutable, meaning that they can be changed after they've been created. A developer can add to or remove from lists as they see fit.
- **Guaranteed Order**: Lists maintain their order. As such, they support random access. Elements within a list can be accessed by index in constant time.
- **Support For Duplicates**: Lists support duplicates. That is to say, a developer may add the same element to a list multiple times.

## Creating and Using Lists

The syntax for creating a list in Python is as follows:

```
# An empty list
my_list = [];
```

Of course, this list is empty. We can also create a list that contains elements already:

```
# A list with numbers
my_list = [1, 2, 3];
```

Also note that Python uses [duck typing](https://en.wikipedia.org/wiki/Duck_typing). This means that a developer can add any type to a container. As a result, following list initialization is valid as well:

```
# A list with random, unrelated elements
my_list = [1, 'one', [1]];
```

When using such a list, a programmer must be extremely careful when iterating over the list. All of the elements are of different types and likely do not support the exact same operations as a result.

Yet another option allows developers to use the list constructor:

```
# A list with random, unrelated elements
my_list = [1, 'one', [1]];

# Creating an empty list using the list constructor
other_list = list();

# Creating a list using the list constructor that takes an existing list as an argument
other_other_list = list(my_list);
```

## Accessing A List Element

Let's imagine that we have an existing list:

```
# A list with random, unrelated elements
my_list = [1, 'one', [1]];
```

As we mentioned earlier, lists support random access. Consequently, we can easily and efficiently access any element by its index like so:

```
# Print the first element of the list
print(my_list[0]);

# Print the second element of the list
print(my_list[1]);
```

There are several more useful operations a developer can perform while using lists. View the official Python documentation for a complete list of [common sequence operations](https://docs.python.org/3/library/stdtypes.html#typesseq-common) available to Python programmers.