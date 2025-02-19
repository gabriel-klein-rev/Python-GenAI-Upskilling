# Python Module: Exceptions

> This file details what an exception is and how to handle an exception in Python.

### Resources:
* [Exceptions](https://docs.python.org/3/library/exceptions.html)
* [User-Defined Exceptions](https://docs.python.org/3/tutorial/errors.html#tut-userexceptions)

---

## What Is An Exception?

When executing a program, developers sometimes find that errors are detected during the execution of the program. These errors are referred to as **exceptions**. Fortunately, exceptions are not fatal. As such, a program can reasonably recover from an exception if a developer properly handles the exception.

## Exception and BaseException

At its core, an exception is a type. All exceptions are instances of a class that inherits from the built-in class `BaseException`.

Despite the fact that all exception types inherit from `BaseException`, this class is not designed to be directly inherited from. If a developer wishes to create a custom exception by way of a user-defined class, they should use the `Exception` class. The `Exception` class is derived from `BaseException` and is used to define non-system-exiting exceptions. 

### A Side Note: SyntaxError

The Python [documentation for user-defined exceptions](https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions) specifically identifies *syntax errors* and *exceptions* as two distinct kinds of errors.

A *syntax error*, also called a parsing error, occurs when a developer writes syntactically invalid Python code. Take the following code for example:

```
if True:
print('This is syntactically invalid.');
```

This code raises an `IndentationError`, which is a specific type of `SyntaxError` in Python.

Many exception types in Python deceptively include the term "error" in their names. For instance, the `ZeroDivisonError` is actually a type of exception despite its name.

That said, do not be fooled by Pythonic naming conventions. As you dive deeper into the language, keep in mind that *syntax errors* and *exceptions* are not the same.

## How To Create An Exception

Developers have the ability to create their own custom exceptions while writing their applications. The syntax for creating an exception in Python is as follows:

```
class MyCustomException(Exception):
    # The pass statement is simply here for lack of a proper class body.
    pass;
```

The class `MyCustomException` extends `Exception`. As we discussed earlier, the `Exception` class should be extended by user-defined classes to create custom exceptions.

Once a programmer has created an exception, they make use of it with the `raise` keyword:

```
class MyCustomException(Exception):
    # The pass statement is simply here for lack of a proper class body.
    pass;

# This line of code stops the execution of the script.
raise MyCustomException();

# This line of code does not run.
print("Now back to our regularly scheduled program!");
```

Note the following:

- The above example will always raise an exception of the type `MyCustomException`. A developer would likely never want to always raise an exception of a certain type. We've done so only for demonstration purposes. The ideal situation involves conditionally raising exceptions.
- The print statement which follows will not run as the exception has not been handled by the developer. While developers do not have to handle exceptions &mdash; and in fact many exceptions in Python go unhandled &mdash; we recommend handling exceptions when possible.

## Handling Exceptions

In the code snippet above, we raise an exception but fail to handle it. As such, our program does not continue executing. If we want our program to continue its execution, we need to handle the exception with the `try` and `except` keywords.

The modified code snippets looks like this:

```
class MyCustomException(Exception):
    # The pass statement is simply here for lack of a proper class body.
    pass;

try:
    # This line of code stops the execution of the script.
    raise MyCustomException();
except MyCustomException:
    # Taking the appropriate corrective action
    print("Got away safely!");

# This line of code now runs.
print("Now back to our regularly scheduled program!");
```

Now our program continues to execute despite the fact that an exception is raised at some point. If we break down the revised snippet, we can observe the following:

- Risky code that could raise an exception is placed inside of a `try` scope. We emphasize the word "could" because, under ordinary circumstances, there is no guarantee that an exception will be raised.
- The `except` scope provides the corrective plan of action if the custom exception is raised. Note that we could have anticipated any parent exception type of `MyCustomException` to handle our exception. That said, using the specific exception type is practical in this case.

### The Optional `Finally` Block

Aside from the `try` and `except` scopes, there is a third scope called the `finally` scope. This scope can follow the `except` scope:

```
class MyCustomException(Exception):
    # The pass statement is simply here for lack of a proper class body.
    pass;

try:
    # This line of code stops the execution of the script.
    raise MyCustomException();
except MyCustomException:
    # Taking the appropriate corrective action
    print("Got away safely!");
# The finally scope always executes
finally:
    print("I always execute.");

# This line of code now runs.
print("Now back to our regularly scheduled program!");
```

It is important to understand that the `finally` scope will always execute &mdash; even if the exception that is raised is not handled by an `except` scope. As such, the `finally` keyword is often used to ensure that resources are closed and that any necessary cleanup occurs.

**Fun Fact**: A `try` block must be accompanied by either an `except` block or a `finally` block. It is not syntactically valid to use it on its own:

**Invalid**:

```
class MyCustomException(Exception):
    # The pass statement is simply here for lack of a proper class body.
    pass;

# Not valid
try:
    # This line of code stops the execution of the script.
    raise MyCustomException();

# This line of code now runs.
print("Now back to our regularly scheduled program!");
```

**Valid**:

```
class MyCustomException(Exception):
    # The pass statement is simply here for lack of a proper class body.
    pass;

# Valid
try:
    # This line of code stops the execution of the script.
    raise MyCustomException();
except MyCustomException:
    # Taking the appropriate corrective action
    print("Got away safely!");

# This line of code now runs.
print("Now back to our regularly scheduled program!");
```

**Also Valid**:

```
class MyCustomException(Exception):
    # The pass statement is simply here for lack of a proper class body.
    pass;

# Also valid
try:
    # This line of code stops the execution of the script.
    raise MyCustomException();
# The finally scope always executes
finally:
    print("I always execute.");

# This line of code now runs.
print("Now back to our regularly scheduled program!");
```