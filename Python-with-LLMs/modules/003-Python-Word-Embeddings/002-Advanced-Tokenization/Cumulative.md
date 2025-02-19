# Advanced Tokenization

<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Understand more advanced tokenization techniques used in NLP

</details>


<details>
<summary>Prerequisites</summary>

- Basic understanding text pre-processing techniques such as normalizing and tokenizing 
- Familiarity with RegEx

</details>

<details>
<summary>Description</summary>

Earlier, we explored techniques for pre-processing the text prior to the analysis. The techniques involved removing punctuations, removing stopwords, and word and sentence tokenization. In this module we continue to explore more advanced text processing techniques that will help the model understand the natural language better.

### Stemming
Stemming is a text processing technique where we reduce words to their root form. For example, words "learning" and "learner" would both be reduced to the root word "learn". Stemming allows us to focus on the core meaning of the word instead of being distracted by different ways in which they are being used. It is important to note that the words that they get reduced to may not be dictionary words and is less precise than lemmatization. However, stemming is computationally efficient and useful in scenarios where speed is crucial.

### Lemmatizing 
Coming from the word "lemma", lemmatizing is finding the lemma of a word. Lemma in linguistics is the basic form of a word. For example, the word "be" would be the lemma for words like "is", "am", "are", "was", etc. This is how dictionaries organize the words, by the words' lemma.
This technique yields more sophisticated and consistent result than stemming. Lemmatization can help in improving the accuracy of the text analysis and reducing the data size, as it reduces the variation a word can take. However, it is slower than stemming and it can lead to ambiguity since does not know the context in which the word is used.

</details>

<details>
<summary>Implementation</summary>

### Stemming
We will be using the Snowball stemmer provided by NLTK.
```python
from nltk.stem.snowball import EnglishStemmer
from nltk.tokenize import word_tokenize

text = "The artist decided to create a new painting. Creating art is a form of self-expression. She hoped to create an atmosphere of creativity in her studio where she could freely create. The act of creation brought her joy, and she believed that anyone could create something beautiful with a bit of inspiration."

words = word_tokenize(text)
print(words)
#['The', 'artist', 'decided', 'to', 'create', 'a', 'new', 'painting', '.', 'Creating', 'art', 'is', 'a', 'form', 'of', 'self-expression', '.', 'She', 'hoped', 'to', 'create', 'an', 'atmosphere', 'of', 'creativity', 'in', 'her', 'studio', 'where', 'she', 'could', 'freely', 'create', '.', 'The', 'act', 'of', 'creation', 'brought', 'her', 'joy', ',', 'and', 'she', 'believed', 'that', 'anyone', 'could', 'create', 'something', 'beautiful', 'with', 'a', 'bit', 'of', 'inspiration']


stemmer = EnglishStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
# ['the', 'artist', 'decid', 'to', 'creat', 'a', 'new', 'paint', '.', 'creat', 'art', 'is', 'a', 'form', 'of', 'self-express', '.', 'she', 'hope', 'to', 'creat', 'an', 'atmospher', 'of', 'creativ', 'in', 'her', 'studio', 'where', 'she', 'could', 'freeli', 'creat', '.', 'the', 'act', 'of', 'creation', 'brought', 'her', 'joy', ',', 'and', 'she', 'believ', 'that', 'anyon', 'could', 'creat', 'someth', 'beauti', 'with', 'a', 'bit', 'of', 'inspir']
```
Note how the words got truncated to their respective stems. For example, decided became decid, create became creat, and so on and so forth. In the stemmed words, notice how the words creating and create were stemmed to creat but creation stemmed to creation. This is called "understemming". When words with different meanings get stemmed into the same stem, it is called "overstemming"

### Lemmatizing
```python
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
string_for_lemmatizing = "Can you really have too many pens? They all serve different purposes and one simply cannot have too many!"
words = word_tokenize(string_for_lemmatizing)
print(words)
# ['Can', 'you', 'really', 'have', 'too', 'many', 'pens', '?', 'They', 'all', 'serve', 'different', 'purposes', 'and', 'one', 'simply', 'can', 'not', 'have', 'too', 'many', '!']

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized_words)
# ['Can', 'you', 'really', 'have', 'too', 'many', 'pen', '?', 'They', 'all', 'serve', 'different', 'purpose', 'and', 'one', 'simply', 'can', 'not', 'have', 'too', 'many', '!']

```
Note how the words such as pens and purposes were converted to pen and purpose.
</details>