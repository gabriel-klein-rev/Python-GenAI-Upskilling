# Python Module: Variable Scopes

> This file details scopes in Python. It also covers the basics of using the `nonlocal` and `global` keywords in Python.

### Resources

* [The `nonlocal` Statement](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-s)
* [The `global` Statement](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-s)

---

## Scopes In Python

A **scope** in a programming language governs how variables and names are looked up in your program. Python builds its scopes around the **LEGB rule**. LEGB stands for:

- Local
- Enclosing
- Global
- Built-in

These are the four official scopes in Python. We'll explore how each of these scopes works in a bit more detail.

### The Local Scope

The local scope is a standard scope in programming languages. A variable's scope is local if it is defined within the block of code inside of which it is being referenced. For instance:

```
def my_func():
    local_var = 'local variable';
    print(local_var);
```

The variable `local_var` is local to the `my_func` function. If there were another variable called `local_var` defined before the function, the local variable would take precedence:

```
local_var = 'not local variable';

def my_func():
    local_var = 'local variable';
    print(local_var);
```

When `my_func` is invoked, it still prints the value of the local variable.

### The Enclosing and Global Scopes

Sometimes developers want to access a variable from an outer scope. As such, we'll revisit our previous example:

```
local_var = 'not local variable';

def my_func():
    local_var = 'local variable';
    print(local_var);
```

As we mentioned earlier, the `local_var` referenced within the function is not the same `local_var` that is defined before the function. This behavior is called *shadowing* as declaring a variable with the same name as another variable that is in an outer scope hides the variable from the outer scope.

**Note**: Shadowing is generally not good practice as it makes code harder to read and manage.

Fortunately, Python allows programmers to reference variables from outer scopes using the `global` and `nonlocal` keywords.

A variable that is created outside of a function is considered a global variable. As such, we must use the `global` keyword in order to access our outer `local_var` variable:

```
local_var = 'not local variable';

def my_func():
    global local_var;
    local_var = 'still not local variable';

my_func();

print(local_var);
```

We've refactored the code to show how the `global` keyword works. We still have the outer `local_var` variable declared. This time, however, we use the `global` keyword within the function in order to specify that we are referencing the global variable for the duration of the scope rather than declaring a new one. This allows us to prevent the shadowing that would normally occur here.

When the print statement in the script finally executes, it is clear that the `local_var` variable within the function references the global variable.

There is another keyword which helps eliminate the problem of shadowing: `nonlocal`. In order to showcase the keyword's behavior, we'll modify the current example:

```
local_var = 'not local variable';

def my_func():
    global local_var;
    local_var = 'still local variable';
    another_local_var = 'another local variable';

    def inner_func():
        another_local_var = 'not another local variable';

    inner_func();

    print(another_local_var);

my_func();
```

We've added a local variable called `another_local_var` and a nested inner function to the `my_func` function. The inner function also declares a variable called `another_local_var`, shadowing the outer variable. The scope inside of which this outer variable exists is known as the *enclosing scope*.


Because the variable within the enclosing scope is shadowed, the inner function does not have the effect some developers would want it to have. As such, we must use the `nonlocal` keyword to refer to the variable within the enclosing scope:

```
local_var = 'not local variable';

def my_func():
    global local_var;
    local_var = 'still local variable';
    another_local_var = 'another local variable';

    def inner_func():
        nonlocal another_local_var;
        another_local_var = 'not another local variable';

    inner_func();

    print(another_local_var);

my_func();
```

The addition of the `nonlocal` keyword within the inner function ensures that we reference the existing `another_local_var` variable rather than shadowing it.

### The Built-in Scope

The built-in scope is the "highest" scope, meaning that it is always in scope. The [`id`](https://docs.python.org/3/library/functions.html#id) function, for instance, is a built-in function that some developers who are new to Python accidentally shadow frequently as it always in scope:

```
# Shadowing the built-in name "id"
id = 0;
```

**Note**: Developers should not shadow built-in names. We've only done so in the example above for demonstration purposes.