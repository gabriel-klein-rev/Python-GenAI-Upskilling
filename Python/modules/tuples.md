# Python Module: Tuples

> This file details the features of tuples and how to use tuples in Python.

### Resources

* [Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-seque)

---

## What Is A Tuple?

A tuple is a sequence data type that consists of several values separated by commas. It is a bit syntactically different from some of the other data structures we've covered thus far.

Some notable features of tuples include:

**Immutability**: Tuples are immutable. Once a developer creates a tuple, they cannot alter it.
**No Support For Assigning To Items**: Unlike lists, tuples do not support assigning to a tuple's individual items.

## How To Create A Tuple

The basic syntax for a creating a tuple is as follows:

```
# Creates an empty tuple
my_tuple = ();
```

The above snippet creates an empty tuple. In order to create a tuple with values, use the following syntax:

```
# Creates a tuple with 4 values
my_tuple = (1, 'string 1', object(), 'string 2');
```

The syntax for creating a tuple is straightforward, but there is a trick to creating a tuple with a single value:

```
# Creates a tuple with a single value
my_tuple = 'val 1',;

# Also creates a tuple with a single value
my_second_tuple = ('val 1',);
```

In both of the statements above, we've included a trailing comma after the single value. This trailing comma is necessary in Python &mdash; even if the parentheses are present. As such, the following syntax, while valid, does not create a tuple with a single value:

```
# Does not create a tuple
my_tuple = ('val 1');
```

## Tuple Packing and Unpacking

*Tuple packing* and *sequence unpacking* can make creating tuples and and working with their values easier. Tuple packing allows developers to initialize a tuple with multiple values without using parentheses:

```
# Creating a tuple using tuple packing
my_tuple = 1, 'string 1', object(), 'string 2';
```

All of tuple's values are assigned to the tuple &mdash; "packed" together as a single tuple &mdash; despite the absence of the parentheses.

The values of a tuple can also be unpacked into individual variables like so:

```
my_tuple = 1, 'string 1', object(), 'string 2';

# Sequence unpacking
num, string_one, an_object, string_two = my_tuple;
```

This snippet initializes four variables by unpacking the contents of the tuple. Note that this sequence unpacking will not work if the number of variables to initialize does not match the number of values in the tuple.