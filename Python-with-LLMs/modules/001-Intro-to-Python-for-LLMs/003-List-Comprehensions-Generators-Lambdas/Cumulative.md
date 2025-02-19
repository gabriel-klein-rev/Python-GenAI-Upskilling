# List Comprehensions, Generators, and Lambdas
<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Write List Comprehensions, Generators and Lambdas
- Understand use cases for Lambdas, List Comprehensions, and Generator Expressions
 
</details>
<details><summary>Description</summary>

### List Comprehensions
List comprehensions stand out as a cherished feature within the Python programming language. They enable you to succinctly create a fresh list by sifting through the elements of a collection and altering the elements that meet the filtering criteria, all encapsulated in a single, compact expression.
They adhere to the fundamental structure:
```Python
[expr for val in collection if condition]
```
This is equivalent to the following for loop construction:
```Python
result = []
for val in collection:
    if condition:
        result.append(expr)
```
The omission of the filtering condition is permissible, retaining solely the expression. 

As an illustration, in a list of strings, strings with a length of 2 or less can be excluded, and simultaneously, they can be transformed to uppercase using the following approach:
```Python
list_strings = ['b', 'is', 'tiger', 'far', 'love', 'language']
[q.upper() for q in list_strings if len(q) > 3]
#['TIGER', 'LOVE', 'LANGUAGE']
```

### Generators
A generator presents an efficient means of crafting a new iterable object. While typical functions execute and furnish a solitary result sequentially, generators supply a sequence of multiple results lazily, halting after each one until the subsequent request. To establish a generator, employ the yield keyword in lieu of return within a function:

### Anonymous (Lambda) Functions
Python supports anonymous or lambda functions, offering a way to compose functions that comprise just a single statement, and the outcome of that statement serves as the return value. These functions are declared using the lambda keyword, carrying no significance other than indicating the declaration of an anonymous function:
```Python
def first_function(x):
    return x * 10
same_anon = lambda x: x * 10
```







</details>
<details><summary>Implementation</summary> 

In addition to list comprehensions there are also Set and dict comprehensions, producing sets and dicts in a similar way to lists. A dict comprehension looks like this:
```Python
dict_comp = {key-expr : value-expr for value in collection if condition}
```
A set comprehension is the same except with curly braces instead of square brackets:
```Python
set_comp = {expr for value in collection if condition}
```
Like list comprehensions, set and dict comprehensions can make code easier to write and read.

Consider the list of strings from before. Suppose we wanted a set containing just the lengths of the strings contained in the collection; we could easily compute this using a set comprehension:
```Python
str_lengths = {len(x) for x in list_strings}
str_lengths
#{1, 2, 5, 3, 4, 8}
```
More functionally we can use the map function:
```Python
set(map(len, list_strings))
#{1, 2, 5, 3, 4, 8}
```
As a simple dict comprehension example, we could create a lookup map of these strings to their locations in the list:
```Python
map_pos = {val : index for index, val in enumerate(str_lengths)}
map_pos
#{'b': 0, 'is': 1, 'tiger': 2, 'far': 3, 'love': 4, 'language': 5}
```
### Nested list comprehensions
Take a list of lists containing some names:
```Python
names_data = [['Will', 'Emily', 'Eric', 'Eddie', 'Steven'],
    ['Maria', 'Juan', 'Javier', 'Joseph', 'Pilar']]
```
Now, suppose we wanted to get a single list containing all names with two or more of the letter e in them. We could certainly do this with a simple for loop:
```Python
names_kept = []
for names in names_data:
    more_es = [name for name in names if name.count('e') >= 2]
    names_kept.extend(more_es)
```
You could use a single nested list comprehension, as such:
```Python
flattenedName=[x for List in names_data for x in List]
result = [name for name in flattenedName if name.count('e')>=2]
```
Take another example where we flatten a list of tuples of integers into a simple list of integers:
```Python
examp_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [element for tup in examp_tuples for element in tup]
flattened
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
Note that order of the for expressions would be the same if you wrote a nested for loop or list comprehension:
```Python
flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)
```
You can incorporate numerous levels of nesting as needed, although, when the nesting surpasses two or three levels, it is advisable to scrutinize whether it enhances code readability. It is crucial to differentiate the previously illustrated syntax from a list comprehension embedded within another list comprehension, a construct that is equally valid:

```python
[[element for element in tup] for tup in examp_tuples]
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
This results in a list of lists, as opposed to a flattened list encompassing all the inner elements.


## Generators
example:
```Python
def cubes(n=10):
    print('Generating cubes from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 3
```
Upon calling the generator, no code is immediately executed:
```Python
gen = cubes()
gen
```
When you request elements from the generator, it begins to execute the code:
```Python
for x in gen:
    print(x, end=' ')

#Generating cubes from 1 to 1000
#1 8 27 64 125 216 343 512 729 1000
```
### Generator expresssions
A more succinct way to make a generator is to use a generator expression. This is a generator analogue to list, dict, and set comprehensions; to create one, enclose what would otherwise be a list comprehension within
parentheses instead of brackets:
```Python
gen = (x *** 3 for x in range(1000))
gen
```
This is completely equivalent to the following more verbose generator:
```Python
def _create_gen():
    for x in range(1000):
        yield x ** 3
gen = _create_gen()
```
Generator expressions can be used in place of list comprehensions as function arguments:
```Python
sum(x ** 3 for x in range(1000))
```
or with dictionaries such as:
```Python
dict((i, i **3) for i in range(5))
#{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
```


### Lambda Functions
Lambda functions prove to be particularly advantageous in data analysis since frequently, data transformation functions accept functions as arguments. Employing a lambda function is often not only more concise but also enhances clarity, compared to crafting an entire function declaration or assigning the lambda function to a local variable. 
```Python
def applied_to_list(a_list, f):
    return [f(x) for x in a_list]
ints = [10, 6, 9, 5,2 5]
applied_to_list(ints, lambda x: x * 3)
```
You can also write `[x * 3 for x in ints]`, but here we passed a custom operator to the applied_to_list function.  Suppose you wanted to sort a collection of strings by the number of distinct letters in each string:
```Python
strings = ['foo', 'carded', 'bar', 'aaaaccc', 'abab']
```
You can pass a lambda function to the lists sort method:
```Python
strings = ['foo', 'carded', 'bar', 'aaaaccc', 'abab']
strings2=sorted(strings,key=lambda x: len(x))
strings2

strings.sort(key=lambda x: len(x))
strings
```

Lambda functions are referred to as anonymous functions for a specific reason. In contrast to functions declared using the def keyword, lambda functions lack an explicit `__name__` attribute assigned to the function object itself.


</details>
