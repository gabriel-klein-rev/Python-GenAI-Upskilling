# NLTK

<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Learn how to use RegEx in combination with the NLTK library for NLP tasks.
- Explore the re module functions for pattern matching in NLTK.
- Apply RegEx in NLTK for tokenized text manipulation.

</details>

<details><summary>Description</summary>

In this module, you will explore the practical application of Regular Expressions (RegEx) in Natural Language Processing (NLP) using the NLTK library. Before diving into the technical details, let's clarify two essential NLP concepts: normalization and tokenization.

## Normalization:
Normalization in NLP refers to the process of transforming text into a consistent and standardized format. It involves handling variations in language, such as converting words to lowercase, removing punctuation, and addressing different spellings of the same word. Normalization ensures that the text is uniform and ready for analysis, reducing the impact of irregularities in language.

For example, consider the words "Text," "text," and "TEXT." Normalizing these words would involve converting all of them to lowercase, so they are treated as the same word during analysis.

## Tokenization:
Tokenization is the process of breaking down a text into smaller units called tokens. Tokens are the building blocks of language, representing individual words or meaningful sub-word units. In English, tokens are typically words, but they can also be phrases or sub-word units, depending on the context.

For instance, the sentence "I love NLTK!" can be tokenized into the following words: ["I", "love", "NLTK", "!"]. Tokenization is a crucial step in NLP, as it allows us to analyze and manipulate text at a granular level, facilitating tasks like counting words, identifying patterns, and extracting meaningful information.

## Regular Expressions with NLTK:
Let's first normalize the text by making everything to lower case and removing punctuations using regex.
The following pattern `\W` will match any character that is not alphanumeric.
```python
import re

text = "If a quick, brown fox jumps! over the lazy cat and takes- a long nap themselves... does that make the fox itself lazy?"
text = text.lower() # we first make all text lower case
pattern = r"\W" # and write a regex that matches all non-alphanumeric characters
normalized = re.sub(pattern, ' ', text) # and replace all the matches with the white characters
print(normalized) # if a quick  brown fox jumps  over the lazy cat and takes  a long nap themselves    does that make the fox itself lazy

```

We can use the nltk library to tokenize the normalized text
Before we can begin, we first need to install the nltk library
```bash
$ pip install nltk
```

Once NLTK library is installed, import the word_tokenize function from nltk.tokenize. We use word tokenization function to break each word into a token. There is also a sentence tokenization that breaks each sentences into tokens.

```python
from nltk.tokenize import word_tokenize

word_tokens = word_tokenize(normalized)
print(word_tokens) #['if', 'a', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'cat', 'and', 'takes', 'a', 'long', 'nap', 'themselves', 'does', 'that', 'make', 'the', 'fox', 'itself', 'lazy']
```

## Stopwords
Stopwords are common words in a language that does not offer a lot of meaning or context in a sentence. In English, words such as 'a', 'the', 'this', or 'in' are examples of stopwords. We utilize NLTK to remove such words

```python
from nltk.corpus import stopwords

# create a set of nltk's english stopwords
stop_words = set(stopwords.words('english'))

# take the tokenized text from earlier and remove stopwords
filtered = [w for w in word_tokens if not w in stop_words]

print(filtered)
# ['quick', 'brown', 'fox', 'jumps', 'lazy', 'cat', 'takes', 'long', 'nap', 'make', 'fox', 'lazy']
```

## nltk.text module
This module brings together a variety of NLTK functionality for text analysis, and provides simple, interactive interfaces.

1. FindAll(regexp)
Finds instances of the regular expression in the text. The text is a list of tokens, and a regexp pattern to match a single token must be surrounded by angle brackets.
```python
from nltk.book import text1, text5

text5.findall("<.*><.*><bro>") # finds 2 tokens that preceeds the word "bro"
# you rule bro; telling you bro; u twizted bro

text1.findall("<a>(<.*>)<man>") # finds the token that is between the word 'a' and the word 'man', essentially returning adjectives describing a man.
# monied; nervous; dangerous; white; white; white; pious; queer; good; mature; white; Cape; great; wise; wise; butterless; white; fiendish; pale; furious; better; certain; complete; dismasted; younger; brave; brave; brave; brave

```

2. Collocation(num=20, window_size=2)
Discover which words appear near each other. Ignores stopwords
```python
from nltk.book import text1
text1.collocations()
#Sperm Whale; Moby Dick; White Whale; old man; Captain Ahab; sperm whale; Right Whale; Captain Peleg; New Bedford; Cape Horn; cried Ahab; years ago; lower jaw; never mind; Father Mapple; cried Stubb; chief mate; white whale; ivory leg; one hand
```

3. Concordance(word, width=79, lines=25)
This function shows in which context the word you specify appears
```python
from nltk.book import text1
text1.concordance('monstrous')

"""
Displaying 11 of 11 matches:
ong the former , one was of a most monstrous size . ... This came towards us , 
ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
ll over with a heathenish array of monstrous clubs and spears . Some were thick
d as you gazed , and wondered what monstrous cannibal and savage could ever hav
that has survived the flood ; most monstrous and most mountainous ! That Himmal
they might scout at Moby Dick as a monstrous fable , or still worse and more de
th of Radney .'" CHAPTER 55 Of the Monstrous Pictures of Whales . I shall ere l
ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
ere to enter upon those still more monstrous stories of them which are to be fo
ght have been rummaged out of this monstrous cabinet there is no telling . But 
of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u
"""
```

4. Similar(word, num=20)
This function returns words appear in the same context as the word provided
```python
from nltk.book import text1
text1.similar('monstorous')
# true contemptible christian abundant few part mean careful puzzled mystifying passing curious loving wise doleful gamesome singular delightfully perilous fearless
```

</details>