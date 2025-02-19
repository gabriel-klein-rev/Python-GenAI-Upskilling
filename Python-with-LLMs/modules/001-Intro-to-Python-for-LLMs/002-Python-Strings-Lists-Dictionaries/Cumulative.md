#  Python Strings, Lists, and Dictionaries
<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Use common Python datatypes of lists, sets, tuples, dictionaries, and strings
- Know which datatypes are mutable and immutable
- implement common Python datatypes in code

 
</details>
<details><summary>Description</summary>

Python has 4 commonly used datatypes to contain other data: lists, sets, tuples, and dictionaries. Each one has its own rules for what it can and can not do:
|Collection|	Mutable|	Duplicates|	Indexable|
|----|----|----|----|
|list	|Yes	|Yes	|Yes|
|Set	|Yes|	No|	No|
|Tuples	|No	|Yes	|Yes|
|Dictionary	|Yes	|No (keys)	|version
```python
l = [1,2,2,4] # List
s = {1,2,3,4} # Set
t = (1,2,3,4,5,5,5,6) # Tuple
d = {"a":1, "b":2, "c":3} # dictionary
```

### Strings
Many Python objects can be converted to a string using the str function:
```Python
num1 = 10.2
s = str(num1)
print(num1)
#10.2
```
Strings are a sequence of Unicode characters and therefore can be treated like other sequences, such as lists and tuples:
```Python
s = 'python'
list(s)
#['p', 'y', 't', 'h', 'o', 'n']
s[:3]
#'pyt'
```
The syntax `s[:3]` is known as slicing and is implemented for many kinds of Python sequences. 


### Lists
Lists are the most flexible container datatypes we will look at. They are maleable (can add and remove elements no problem), they allow duplicate values, and they are indexible. This makes them a good catch-all container, but if you want any sort of limits for the data the list will hold you will have to manually impose them with your implementation

### Dictionaries
Dictionaries are collections that hold key/value pairs. You can make just about any datatype a key, and any data type its value. You create them by placing the key and value inside curly braces, seperate pairs with a comma {key:value, another key: another value}


### Mutable and Immutable Objects
Most objects in Python, such as lists, dicts, NumPy arrays, and most userdefined types (classes), are mutable, i.e. the object or values that they contain can be modified:
```Python
a_list = ['foo', 2, [4, 5]]
a_list[2] = (3, 4)
a_list
#['foo', 2, (3, 4)]
```
Others, like strings and tuples, are immutable:
```Python
a_tuple = (3, 5, (4, 5))
a_tuple[2] = (1,2)

#---------------------------------------------------------------------------
#TypeError                                 Traceback (most recent call last)
#Input In [33], in <module>
#----> 1 a_tuple[2] = (1, 2)
#
#TypeError: 'tuple' object does not support item assignment
```

</details>
<details><summary>Implementation</summary> 

### Lists
example:
```python
# list.append(x) x is the value to be added to the end of the list
appended_list = ["I","declare","a","thumb"]
print(appended_list)
appended_list.append("war")
print(appended_list)

# list.extend(iterable) iterable is an iterable object, like another list
final_numbers = [5,6,7,8]
appended_list.extend(final_numbers)
print(appended_list)

# list.insert(i, x) index position that the object will be insert in front of 
# (so index 0 means front of the list) , x is the value to be added
appended_list.insert(0,"one, two, three, four")
print(appended_list)

# list.remove(x) removes the first element to match x. Raises an ValueError if the item does not exist
appended_list.remove("I")
print(appended_list)

# list.pop([i]) i represents the OPTIONAL index position of the item you wish to return and remove from the list
# if no index is given then the last element in the list will be both returned and removed
print(appended_list.pop())
print(appended_list)

# list.clear() removes all items from the list.
appended_list.clear()
print(type(appended_list))
# del appended_list[2] this deletes the object in index position 2

# list.index(x[, start[, end]]) returns index of value x, where start and end are the optional start/end points
new_list = [1,2,3,4,5,6,"seven"]
print(new_list.index(4, 1, 5))

# list.count(x) returns the ammount of times object x appears in the list
print(new_list.count(3))

# list.sort(*, key=None, reverse=False)
to_sort_numbers = [1,3,2,4,6,5,7,9,8,10]
print(to_sort_numbers)
to_sort_numbers.sort()
print(to_sort_numbers)
to_sort_numbers.sort(reverse=True)
print(to_sort_numbers)
sort_using_key = [[1,"c"],[2,"a"],[3,"b"]]
def my_key(element):
    return element[1] # takes the second element in the nested list and uses it to sort the list
sort_using_key.sort(key=my_key) # don't include the (): you are referencing the method, not calling it
print(sort_using_key)

# list.reverse() this reverses the list
to_sort_numbers.reverse()
print(to_sort_numbers)
to_sort_numbers.append(11)
to_sort_numbers.reverse()
print(to_sort_numbers)

# list.copy() returns a "shallow" copy of your list
#  shallow copy includes references to the original objects
#  deep copy recursively inserts copy of original items: can create recursive loops, or copy data meant to be
#  shared and not copied
copied_list = sort_using_key.copy()
print(sort_using_key)

# see documentation for all this and more

```
### Sets
Sets are useful when you need to filter redundant data in a collection, since they do not allow for duplicate data. You have to be careful with them though: they are not indexable, so you can not pinpoint the data you want from the set. You can add and remove from the set freely.
```python
well = "well"
lets = "let's"
see = "See"
how = "how"
this = "this"
works = "works"

my_set = {1} # this lets intelisense know it is a set and not a dictionary

print(my_set)
my_set.add(well)
my_set.add(well)
my_set.add(well)
my_set.add(lets)
my_set.add(see)
my_set.add(4)
my_set.add(how)
my_set.add(this)
my_set.add(works)
print(my_set)

#set.pop() removes an element and returns it from the set. Can't be sure which it is
print(my_set.pop())
print(my_set)

# set.discard(x) and set.remove(x) both try to remove the specified item, discard will not raise an error if the element does not exist
my_set.discard("Luke")
print(my_set)

# set.update(x) updates the set with the elements from another ITERABLE collection
other_siblings = {"Jed", "Katie", "Kristen"}
my_set.update(other_siblings)
print(my_set)

# this is not an exhaustive list

```
### Tuples
Tuples are collections that are set after creation. They allow duplicates and are indexable, but they are immutable. They are useful when you have data that needs to remain constant while working with it, and for when you need to access a particular element within the collection
```python
this_is_fixed = ("these","are","stuck")

# tuple.count(x) returns the number of instances of x
print(this_is_fixed.count("um"))

# tuple.index(x) returns index of where element x is found. Returns ValueError if element is not found
print(this_is_fixed.index("these"))

```
### Dictionaries
example:
```python
def inside_the_dictionary():
    return "nice"

my_dictionary = {
    "key": "value",
    100: 1000,
    "string key": 5,
    10: "string value",
    None: "this still works",
    "can also do this": None,
    "function": inside_the_dictionary(),
    inside_the_dictionary(): "does this work"
}

print(my_dictionary[inside_the_dictionary()])

my_dictionary["new key"] = 23 # this adds a new key value pair to the dictionary, same as dic.update({key:value})

print(my_dictionary["new key"])

print(my_dictionary.items()) # returns a list with the key value pairs stored as tuples
print(my_dictionary)

# dic.setdefault(key,[value]) returns the value of the provided key, if it does not exist it creates it with the provided value

print(my_dictionary.setdefault("key", "new value?"))
print(my_dictionary.setdefault("new new key", "new created value")) # this returns the new new value :)

# dic.values() returns all values, dic.keys() returns all keys
```




</details>
