# Python Module: Functions

> This file details how to declare and use functions in Python.

### Resources
* [Defining Your Own Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [Built-in Python Functions](https://docs.python.org/3/library/functions.html)

---

## What Is A Function?

A function is a block of code that accomplishes a particular task. A developer might, for instance, create a function which returns the sum of two numbers. 

Functions only run when they are referenced elsewhere in the program. In Python, a developer can call a function from within a module and within other functions.

Developers who only have experience with strictly object-oriented programming languages might see similarities between functions and methods. They should note, however, that while methods are also sets of instructions that perform specific tasks, methods are associated with objects whereas functions are not. Python supports both the creation of functions and methods.

## Defining and Calling Functions

In order to define a function in Python, a developer must use the following syntax:

```
def func_name(param1, param2):
    # Function logic here
```

Note the following:

- Programmers should use the `def` keyword to define a function. The function name follows this keyword.
- By convention, function names in Python do not typically contain capital letters. There is liberal use of underscores in function names.
- The function is not defined within a class. If it were, it would be a method. Regardless of whether a programmer is defining a function or a method, they should use the same syntax.
- The parameters defined for the method do not include types as Python is dynamically typed.
- There is a third parameter referred to as `self` defined if you are defining a method within a class.
- The indentation matters. Developers should indent when defining function logic. In fact, they should indent whenever they enter a new scope!

## The `Self` Parameter

As mentioned above, when a method rather than a function is defined, a parameter known as `self` is defined. This is a conventional parameter name in Python. The parameter allows developers to access the attributes and methods of a class.

The parameter is passed in as the first argument. As such, if the function definition above were placed inside of a class, it would be rewritten as:

```
def func_name(self, param1, param2):
    # Function logic here
```

## Return Statements and Values

Upon returning to the small code snippet defined in a previous section, perhaps you noticed that this function does not have a return type:

```
def func_name(param1, param2):
    # Function logic here
```

In Python, return types are not specified. As such, a developer can return whatever value they want to as such:

```
def func_name(param1, param2):
    # Function logic here
    some_val = True;
    return some_val;
```

This function now returns a boolean value of `True`. It could also, however, have returned a numeric value or even a custom type defined by the programmer.

Let's now return to our original function definition:

```
def func_name(param1, param2):
    # Function logic here
```

Despite the fact that there is no return statement present, this function does return a value as all functions in Python return a value. That value is `None` if no other return value is specified. The `None` keyword simply denotes the absence of a value. Developers can also explicitly return `None`.

```
def func_name(param1, param2):
    # Function logic here
    return None;
```

## Functions As Objects

Thus far, many of the code snippets have featured functions which are not syntactically valid. If a function has no logic, many integrated development environments will mark the lack of such logic as an error. In order to prevent this problem, developers can use the `pass` keyword:

```
def func_name(param1, param2):
    pass;
```

This keyword will provide the programmer with the opportunity to come back and provide the implementation later without worrying about leaving syntactically invalid code in their project. Of course, the developer also has the option to provide the actual implementation here as well:

```
def func_name(param1, param2):
    return param1 + param2;
```

Now that the function is fully "implemented", let's explore some ways in which we can use it. The first case use case, which entails calling a function from within another function, is fairly standard in many object-oriented programming languages.

### A Simple Function Call

Observe the following:

```
def func_name(param1, param2):
    return param1 + param2;

def func_two(param1, param2):
    result = func_name(3, 4);
```

This code snippet shows a simple function call. Function two, defined as `func_two`, calls `func_name` here. Notice that it passes the required positional arguments to the function in the call and stores the return value in a local variable called `result`.

Functions can also be called at the module level. For instance:

```
def func_name(param1, param2):
    return param1 + param2;

def func_two(param1, param2):
    result = func_name(3, 4);

func_two();
```

As you can see, the function call is perfectly valid outside of a class.

### Using Functions As Objects

In Python, functions are objects. As such, developers can not only define functions but pass them to other functions as arguments:

```
def some_func():
    return True;

def caller_func(param1):
    return param1;

caller_func(some_func);
```

Notice that `caller_func` takes `some_func` as a callback function. It is worth noting that the outer function does not actually call `some_func` in this example. It simply returns the function, which is an object. In order to call the function, the developer should do the following:

```
def some_func():
    return True;

def caller_func(param1):
    return param1();

caller_func(some_func);
```

The only difference here is that the function `param1` references has been invoked using parentheses.

Since functions are objects, we can also create references to them like so:

```
def some_func():
    return True;

def caller_func(param1):
    return param1();

func_ref = some_func;
```

We can then use the `func_ref` variable to later call `some_func`.

---

**Fun Fact**: Developers can also define functions within the scope of other functions. These local functions are scoped only to the functions in which they are defined:

```
def some_func():
    def inner_func():
        return True;
    return inner_func;
```

## Positional and Keyword Arguments

Python programmers have a lot of flexibility in how they define the arguments that should be passed to a function when it is called. Once again revisiting our short function definition, we can observe it defines two parameters:

```
def func_name(param1, param2):
    return param1 + param2;
```

Let's modify this function definition slightly:

```
def func_name(param1, param2, param3 = 100):
    return param1 + param2 + param3;
```

Notice that a third parameter called `param3` now exists. This parameter is known as a **keyword argument**. You might also hear the term **named parameter**.

A keyword argument is provided a default value when it is defined. As such, when the function is called, the caller is not required to pass in a value for the keyword argument. Some valid function calls for `func_name` now include:

```
func_name(2, 3);
func_name(2, 3, 4);
func_name(2, 3, param3 = 4);
```

Note the following:

- You must pass values for the first two parameters in. These are known as **positional arguments** and are mandatory.
- You have the option not to pass in values for keyword arguments; the default values for keyword arguments will simply be used. When you do pass in keyword arguments, you can do so by either using the name of the parameter or just passing in a value as if the named parameter was positional. 

The ability to use the name of a parameter comes in handy. For instance, let's imagine that we now have a fourth parameter:

```
def func_name(param1, param2, param3 = 100, param4 = 200):
    return param1 + param2;
```

Both `param3` and `param4` are optionally passed in when calling the function. That said, what happens when a developer wants to pass in a value for `param4` and rely on the default value for `param3`? Let's take a look:

```
func_name(2, 3, 4);
```

The above function call will not achieve this result as it is assumed that the third argument refers to the `param3` as no name is used to specify otherwise. The developer should instead write:

```
func_name(2, 3, param4 = 4);
```

Now the developer can take advantage of the named parameter's default value while passing in a custom value for the fourth parameter.

**Fun Fact**: You might have noticed that all of the keyword arguments come after the positional arguments. There is a reason for this. Keyword arguments cannot be defined before all of the function's positional arguments.