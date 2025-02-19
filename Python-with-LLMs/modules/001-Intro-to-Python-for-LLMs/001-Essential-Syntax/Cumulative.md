# Python Essential Syntax
<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Understand Pythons identifiers, keywords, and types and values
- Know how to write and implement functions, classes, and objects in Python
- Implement inheritance, abstraction, and write constructors in Python
 
</details>
<details><summary>Description</summary>

# Python   
## Introduction
Python is one of the most popular programming languages in the world, second only to Javascript in one study ([the study](https://bootcamp.berkeley.edu/blog/most-in-demand-programming-languages/)). Youtube, Google, and other tech giants have made use of Python, and there is a high demand for the language in the market today. It was created by Guido Von Rosssum, who named it after "Monty Python's Flying Circus" because he wanted the langauge to be "fun". The language is easy to use, easy to read, and easy to jump into.

There are a few things to know about Python before jumping into the code itself:
1. Python is a "High Level" language
    - this means Python automates memory management for you. It assigns and frees memory for you so that you can focus on your coding. Freeing memory is called garbage collection
    - this allows for fast programming, but the tradoff is optimization: you can not min/max your performance efficency with a high level language like you can with a language like C++.
2. Python is a "Dynamic" language
    - You do not need to tell your code what type of data you are working with: Python handles that for you.
    - This is useful for speed and readability, but it has drawbacks
        - If you read code someone else developed you might have a harder time understanding what kind of data you are working with
        - Not having type security can lead to unexpected outcomes in your code
3. Python is a "Strongly Typed" language
    - Python will not implicitly coerce your data types: you must reassign variables if you want to change their type
4. Python is an "Interpreted" language
    - Python code is compiled and executed line by line, as opposed to the entirety of the code being compiled before run (like Java).
    - This is generally slower than a compiled language, but it does allow you to modularly test your application (can test one part without having to compile other parts)
    - You lose the benefits of having a compiler check your code for errors and/or optimize your code
## Identifiers
Identifiers are the names you give to variables, classes, functions, etc. They are user created names that reference something within your code. These identifiers must start with a letter, and there are some best practices for naming conventions:
- Classes and Exceptions: PascalCase (no spaces, uppercase first letter for each unique word)
- Constants: SCREAMING_SNAKE_CASE (no spaces, all uppercase letters, underscore seperates unique words)
- Everything else: snake_case (no spaces, all lowercase letters, underscore seperates unique words)
To create an identifier you simply have to use the assignment operator and define what you want the identifier to reference
```Python
my_identifier = "It is this easy"
```
You can add a type annotation that makes it easier for developers to know what you EXPECT the data type to be, but that is all the annotation accomplishes: It has no effect on the code itself.
```Python
my_number: int = 5
my_string: str = "This is a string"
my_string_number: float = "This is a string despite saying I expect a float"
```
## Key Words
Python has some reserved Key Words you do not want to try and overwrite: they provide functionality for your code
#### control flow
```Python
for # used if you want something to loop
in # use this when you want to reference something inside another element
while # use this when you want to loop for specified conidtion
```
#### exceptions
```Python
try # this is used to start your try except block. Use this when you think something can go wrong
except # use this to handle things going wrong
finally # use this when you need something to happen whether your code executes successfully or not
raise # use this to raise an exception
```
#### importing
```Python
from # use this to specify where you are importing your code from
import # use this to import your code
as # you can set a reference to whatever it is you are importing
```
#### logical operators
```Python
is # use this when you want a True result when A = B
is not # use this when you want a True result when A != B
and # use this when you want to set up multiple trigger conditions
or # use this when you want to set up multiple optional trigger conditiona
if # use this when you want code to run under specified conditions
elif # use this when you want code to run under conditions not covered by the if statement
else # use this to run code if your if and elif statements do not run
True # boolean indicating something is true
False # boolean indicating something is false
```
#### others
```Python
None # default function return value
pass # use this to ignore code
def # used to create functions
class # used to create classes
assert # used for testing to get a boolean result
break # used to escape a loop
```
## Operators
```Python
+ # addition
- # subtraction
* # multiplication
/ # division
** # power of
% # modulus
// # floor division
== # comparison operator
```
## Types and Values
Python is unique from many other programming languages in that it has no primative data types. Primatives are the most basic type of data that can be used in a programming language, and are built into their respective languages. Python forgoes this and makes everything an object. So if you create a reference for the number 5 you are creating a numeric object
```python
this_is_an_object = 5
```
There are a couple built in data types in Python:
```Python
# numeric datatypes are integer and float
my_integer = 1 # no decimal
my_float = 1.1 # can handle decimals

# String is the data type that handles words/text
my_string = "this handles words/text"

# booleans can either be True or False
my_true_boolean = True
my_false_boolean = False

# None can be assigned as a type: uesful for avoiding errors
my_none = None
```
## String Literals
Strings are one of, if not the most common data forms in coding. A string literal is the value of the string
```Python
my_string_literal = "the string literal is the content of the string"
```
You can get fancy with the way you create strings by doing string interpolation. String interpolation is adding variables into strings
```Python
my_basic_string = "No interpolation happening here"

# You can concatonate strings together by using the + operator
name = "Will"
greeting = "Hello " + name 

# if you place an f before the first quote you can make a formatted string
formatted_string = f"Hello {name}"

# you can also use the .format() method to format your string
formatted_by_method_string = "Hello {}".format("Will")
```
String slicing is where you work with a sub-string of a string (work with specific parts of a string)
```Python
my_string = "Hello Will"
just_hello = my_string[0:5] # this will read from the start to the 4th index position EXCLUDING the 5th element
just_will = my_string[6:10] # This will read from the 6th index to the last index position (notice it is one number larger than the string itself)

# use a negative number to work backwards in a string (-1 is the last element of the string)
using_negative_index = my_string[0:-1] # this will be "Hello Eri" because it goes up to and excludes the last index

# You can use a 3rd position to designate the increment steps (every other character, every third, etc)
every_other_letter = my_string[0::2] # this starts with the first character and appends every other letter after it

# you can also work backwards with the increment

reversed_letters = my_word[::-1]

# be careful you remember that the length of the string is not the same as the number of index positions
print(len(my_string)) # this is 10
print(my_string[10]) # this will cause an error, because indexing starts at 0

# finally, you can make anything in Python a string by calling the str() function on it

a_number = 3
print(type(str(a_number))) # this will return string, the method creates a string version of our object

```



</details>
<details><summary>Implementation</summary> 

### Functions
Functions are blocks of code that can be reused in multiple locations. They are useful for reducing redundancy, and they can also be attached to classes to give them functionality.
```python
# to create a function you use the def keyword, name the function, give it ():, and then write the code with a single indent. Use the return key word if you want to return something specific
def basic_function():
    return "this is the basic function"

# you can add parameters to your function by adding them inside the ()
def basic_function_2(parameter):
    return parameter + 1 # you can add an argument to this function and get it back plus 1

# You can add type annotations to the parameters, and even declare a return type. This still has no actual effect on the code
def add_type_annotation(param1: str, param2: int) -> str:
    return "you are indicating you want a string and int param entered into this function and you expect a string back"

# if you add numeric types you will get addition, if you add strings you will get string concatonation
def annotations_dont_matter(num: int, num2: int) -> int:
    return num + num2
print(annotations_dont_matter(3,5)) # this works as expected
print(annotations_dont_matter("these"," are not numbers")) # this also works, despite types not matching annotation

# you can add a variable to the end of the paramaters called a variable argument, which takes an unspecified ammount of information in and places them inside a Tuple
def variable_arguments(*args): # use this vararg when you don't know how much information the function will work with
    for element in args:
        print(element)
variable_arguments(1,2,3,4,5)

def vararg_many_objects(*can_be_named_whatever): # the convention is to call it args, but you can name it what you want
    for element in can_be_named_whatever:
        print(element)

# you can mix and match data types in your vararg
vararg_many_objects(1,"two",3,"four")

# this allows you to enter information in key/value pairs. The kwargs is a dictionary
def key_word_function(**kwargs): # this adds key:value arguments into your function
    print(kwargs["password"])
    print(kwargs["username"])

key_word_function(password="my password", username="my username")

def more_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

more_kwargs(first_key="first value", second_key="second value", third_key="third_value")

# you can even add functions as arguments in your functions
def called_function():
    return"this is called by the outter function"

def calls_a_function(function):
    return function()


print(calls_a_function(called_function)) # leave off the parentheses: you want the reference for the function, not to call it
```
### Classes and Objects
You can bind variables and functions to classes in Python. This allows you to have more control over the flow of your code, and it especially allows for Object Oriented(esque) Programming. This is also useful if you need to model something in life within your program: it gives you a repeatable template to create a representation of the real life thing within your code
```python
# This needs to be added to the example when you get to abstract classes and methods
from abc import ABC, abstractmethod

# basic class syntax is the class keyword, ClassName:, init under method(add instance variables here), then associated functions
class MyNewClass:
    # this sets up the constructor for the class. There can only be one
    # notice you can set default values for parameters by declaring them within the ()
    def __init__(self, age=0, name="default name"):
        self.name = name
        self.age = age

    def my_new_class_function(jeeves):  # first parameter is always a reference to self, doesn't have to be called self
        return "this is my class function"

    # the __str__ method is used when you pass the object in the str() method. You can overwrite it to best suit your class
    def __str__(jeeves):
        return f"my name is {jeeves.name} and my age is {jeeves.age}"

    # the __repr__ method should allow you to create a clone of the class. I could create a new variable and call this method to create a clone of the object
    def __repr__(self):
        return f"MyNewClass(self,{self.age},{self.name})"

# the self parameter is included because Python, under the hood, is actually using the class to call the function, and the particular object you want to use is being passed in as the first argument
my_class = MyNewClass()
print(my_class.__str__()) # this is the same as below
print(MyNewClass.__str__(my_class)) # this is the same as the above

# Python supports abstract classes. You make a class abstract by adding ABC inside the parenthesis
class MyAbstractClass(ABC):
    
    # this is a class variable, accessed by calling the class itself, not an instantiated object
    class_count = 0

    # class methods take in the class as an implicit first argument, can interact with and change the state of the class
    @classmethod
    def print_class_count(cls): # still need to add a parameter for the class here
        return cls.class_count

    # abstract methods have no body: they need to be defined in their child class
    @abstractmethod
    def to_be_determined(self):
        pass

    # static methods are similar to class methods in that they are called by the class itself, but they do not recieve the class or an instance of the class as an IMPLICIT argument. You can add it, but might as well use a class method at that point
    @staticmethod
    def static_method():
        return "This is my static method, notice it does not interact with the state of the class"


class MyInheritsTheAbstractClass(MyAbstractClass):

    def __init__(self):
        print("I inherited from the abstract class")
        MyAbstractClass.class_count = MyAbstractClass.class_count + 1

    # you can now define what the abstract method does within the child class
    def to_be_determined(self):
        return "I have defined what this function actually does"


class AlsoInheritsAbstractmethod(MyAbstractClass):
    def __init__(self):
        print("I also inherited from the abstract class")
        MyAbstractClass.class_count = MyAbstractClass.class_count + 1

    def to_be_determined(self):
        return "I have also defined what this function does"


# my_class = MyInheritsTheAbstractClass()
# print(my_class.print_class_count())
# my_other_class = AlsoInheritsAbstractmethod()
# print(my_other_class.print_class_count())
# print(my_class.to_be_determined())
# print(my_other_class.to_be_determined())

class OuterClass:
    def __init__(self, number, word, inner_class="my inner class"):
        self.number = number
        self.word = word
        self.create_inner_class(inner_class)

    class InnerClass:
        def __init__(self, name):
            self.name = name
            print("the inner class has been created")

    def create_inner_class(self, name):
        self.inner_class = self.InnerClass(name)

    def __str__(self):
        return f"my number is {self.number}, my word is {self.word}, and my inner class is called {self.inner_class.name}"


# outter_class = OuterClass(5, "pie")
# print(str(outter_class))

class InheritedConstructor:
    def __init__(self, name):
        self.name = name
        print("the parent constructor was called")


class Inheritsconstructor(InheritedConstructor):
    def __init__(self, age, name):
        # super(Inheritsconstructor, self).__init__(name)
        super().__init__(name)
        self.age = age
        print("the child class constructor was called")

class A:
    def __init__(self):
        print("parent constructor was called")

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("the child was called")

# Python supports multiple inheritance, but it can get real messy real quick. Avoid it if you can early in the training

# you can explicitly call each parent constructor within the child constructor to make multiple inheritance work

class Class1:
    def __init__(self, name) -> None:
        self.name = name
        print("Class1 constructor called")

class Class2:
    def __init__(self, age) -> None:
        self.age = age
        print("Class2 constructor called")

class Person(Class1, Class2):
    # make sure you declare the parameters that match the parent constructors
    def __init__(self, name, age) -> None:
        Class1.__init__(self,name)
        Class2.__init__(self,age)
        # anything pertinent to this class in particular goes after the parent constructors
        print("Person Constructor finished")

my_person = Person("Will", 27)
print(my_person.name) # shows Will
print(my_person.age) # shows 27

```


</details>
