# Python Module: String Literals

> This file covers the basics of string literals in Python and details how to use them.

### Resources:
* [String Literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)
* [Interning Strings](https://docs.python.org/3/library/sys.html#sys.intern)
* [CPython](https://github.com/python/cpython)
* [Literal String Interpolation](https://www.python.org/dev/peps/pep-0498/)
* [`str.format()`](https://docs.python.org/3/library/string.html#formatstrings)

---

## Strings

Strings are a data type used in several programming languages &mdash; including Python &mdash; to represent sequences of characters. They are implemented as arrays of bytes that represent characters.

In Python, programmers can create strings by using the string constructor, single quotes, double quotes, or even triple quotes:

```
# A string created using the string constructor
string_zero = str('I am a string.');

# A string enclosed by single quotes
string_one = 'I am a string.';

# A string enclosed by double quotes
string_two = "I'm a string.";

# A string enclosed by triple quotes 
string_three = """I'm
                    a
                    string.""";
```

Note the following about the above code snippet:

- Developers can use the string constructor to create string objects, but the use of this constructor is not as common as simply using quotation marks.
- Many Python programmers prefer the single quotes when creating strings.
- A string that is surrounded by double or triple quotes allows developers to avoid using the escape character to account for the additional `'` symbol in the string itself. This can be useful.
- Using the triple quotes allows for the creation of multiline strings which no not require the use of any escape characters.
- Strings are immutable in Python, which means the strings created in this snippet cannot be changed.

Because strings are really just sequences or characters, Python allows developers to easily access specific elements of a string using the same syntax they would use to access elements of a container such as a list:

```
# A string enclosed by single quotes
string_one = 'I am a string.';

# Accessing the first character in the string
elem_one = string_one[0];
```

**Fun Fact**: Python does not include a character data type as many other languages. As such, a single character is still just a string in Python.

## What Is A String Literal?

The term "literal" refers to a notation for a constant value. A **string literal** allows for a simple way of specifying the contents of a string in a program. Take the following snippet for example:

```
my_string = 'a string literal';
```

In the above statement, `a string literal` is a string literal which the variable `my_string` points to.

## Formatting Strings

Python provides developers with several utilities for easily formatting strings. One such utility is the `format` method. Take a look the example below:

```
# Creates a string with a parameter with an index of 0
christina = 'Christina {0}';

# Replaces the first parameter with 'Russ' and then prints the newly returned string
print(christina.format('Russ'));
```

Note the following:

- Strings can contain replacement fields denoted by braces. The fields use zero-based indexes inside of the `{}`.
- The `format` method receives an argument which is used to replace the field in the string. This method can receive any number of arguments as a string might have multiple replacement fields.

Python programmers can also take advantage of literal string interpolation. Strings that use the syntax for literal string interpolation are sometimes called *f-strings*:

```
color = 'brown';
animal_one = 'fox';
animal_two = 'dog';

pangram = f'The quick {color} {animal_one} jumps over the lazy {animal_two}.';
```

The name for an *f-string* is fitting given that is simply a string that is preceded with an "f". Notice that *f-strings* make use of string interpolation by simply embedding existing strings into the newly created string.

Programmers can also enjoy easy date formatting with *f-strings*:

```
date = datetime.date(2021, 6, 3);

# This prints: "Today is 2021-06-03 and it is a Thursday."
print(f'Today is {date} and it is a {date:%A}.');
```

## Interned Strings

Several programming languages provide mechanisms for making the use of strings more memory-efficient. Python uses a common technique called *interning*.

Interning a string entails adding it to a special table or pool upon its creation so that it can be reused later. This strategy can save memory as it reduces the number of redundant string objects that are created in a program.

Developers should note, however, that Python's interning strategy differs with each [Python implementation](https://wiki.python.org/moin/PythonImplementations). That is to say, each implementation interns to different degrees; in fact, some might make no guarantees of interning at all. The standard implementation of Python, known as CPython, guarantees some interning.

**Fun Fact**: If a programmer is unsure of which implementation of Python they're using, they can write the following code to find out this information:

```
import platform

print(platform.python_implementation());
```

As CPython does guarantee some degree of interning, developers can easily verify this interning. Observe the following:

```
christina = 'christina';
canisha = 'canisha';
christina_again = 'christina';
christina_thrice = str('christina');

print(id(christina));
print(id(canisha));
print(id(christina_again));
print(id(christina_thrice));
```

This code snippet creates four reference variables for string objects, but only two strings objects are created. The proof is in what is printed to the console in the last four statements of the script. These final four statements do two things:

1. They obtain the unique ID of the underlying object that each reference points to. The [`id` function](https://docs.python.org/3/library/functions.html#id) returns the identity of an object, which is just an integer that is "guaranteed to be unique and constant for this object during its lifetime". In CPython, this ID is actually just the address of the object in memory.

2. They print the unique ID for the underlying object.

When we run the above script, four numbers are printed to the console. These numbers consistently show that, while the object that `canisha` points to has an ID that is different from the three other objects, the objects that `christina`, `christina_again`, and `christina_thrice` point to are not different objects at all; they are the exact same object as the IDs that are printed for these three objects are identical. It is also worth nothing that we are using CPython for this example, so these IDs are the memory addresses of the underlying objects.