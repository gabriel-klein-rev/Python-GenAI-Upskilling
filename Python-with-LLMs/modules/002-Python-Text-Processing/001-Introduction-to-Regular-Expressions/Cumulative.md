# Introduction to Regular Expressions

<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
1. Understand the concept of regular expressions and their importance in text processing.
2. Identify common use cases where regular expressions can be applied.
3. Comprehend the basic syntax and structure of regular expressions.
4. Implement regular expressions in Python for pattern matching and text manipulation.

</details>

<details><summary>Description</summary>

### What are Regular Expressions?

Regular expressions, often referred to as regex, are powerful tools for pattern matching and text manipulation. They provide a concise and flexible way to describe and match patterns within strings. Regular expressions are widely used in various programming languages and are particularly useful for tasks such as data validation, searching, and text processing.

### Why Learn Regular Expressions?

Regular expressions offer a versatile and efficient way to handle textual data. They enable programmers to define complex search patterns, making it easier to locate, extract, or manipulate specific information within strings. Whether you're validating user input, searching for specific patterns in a document, or extracting data from a large dataset, regular expressions can significantly streamline these tasks.
</details>

<details>
<summary>Real World Application</summary>

## Common General Use Cases

#### Email Validation

Ensuring that an email address provided by a user follows a valid format

#### Phone Number Validation

Verifying that a user-entered phone number consists of exactly 10 digits, preventing incorrect or incomplete entries.

#### Password Strength Checker

Validating the password fits the strength requirement

## Common Use Cases in Machine Learning and Natural Language Processing

#### Data Cleaning in Text Classification 

Removing non-alphabetic characters from the text to focus on relevant information

#### Named Entity Recognition (NER) Preprocessing: 

Extracting potential named entities (like names) by identifying words that start with an uppercase letter in unstructured text data.

#### Tokenization

Splitting text into sentences or words for creating embeddings

</details>

<details><summary>Implementation</summary>

### Basic Syntax:

In Python, the `re` module provides support for regular expressions. Here's a basic overview of the syntax:

```python
import re

# Input text
text = "insert_your_text_here"

# Define a pattern
pattern = r"insert_your_pattern"

# Use re.search() to find the first match
match = re.search(pattern, text)

# Use re.findall() to find all matches in a string
all_matches = re.findall(pattern, text)

# Use re.sub() to replace matched patterns
replacement = "insert_replacement_text"
modified_text = re.sub(pattern, replacement, text)
```
### Common Patterns:
 
#### 1. Literal Characters:
You can match exactly character for character. The following pattern looks for the world "hello" in any string 
```python
pattern = r"hello"
text = "hello, world!"
match = re.search(pattern, text)

print(match) #re.Match object; span=(0, 5), match='hello'
```
You can also look for special characters
```python
pattern=r"@"
text = "example@example.com"
```
This will match the '@' symbol in the example email address.

#### 2. Character Classes:
You can match multiple characters by listing them inside the hard bracket '[ ]'. The following pattern will match characters 'a', 'e', 'i', 'o', and 'u'
```python
pattern = r"[aeiou]"
text = "hello, world!"

matches = re.findall(pattern, text)

print(matches) # ['e', 'o', 'o', 'e', 'o']

pattern = r"[A-Z]" #Matches all uppercase alphabet
pattern = r"[A-Za-z0-9]" #Matches all alphanumeric
```    
Some commonly used character classes have shorthands. 
- `\d`== `[0-9]`
- `\w` == `[A-Za-z]`
- `\s` == whitespaces

#### 3. Quantifiers: specify number of occurrences of a character or group in the given pattern
```python
#matches exactly 4 characters of lower case alphabet
pattern = r"[a-z]{4}"

# Matches digits in patterns of 333-333-3333
pattern = r"\d{3}-\d{3}-\d{4}"

# Matches 0 or more 'a's
pattern = r"a*"

# Matches 1 or more a's
pattern = r"a+"

# Matches 2 or more a's
pattern = r"a{2,}"
```
4. Anchors:
```python
pattern = r"^start"  # Matches if the string starts with "start"
pattern = r"$end"  # Matches if the string ends with "end"
```
5. Grouping:
```python
# matches exactly 2 contiguous occurrences of string "abc"
pattern = r"(abc){2}"
```
</details>