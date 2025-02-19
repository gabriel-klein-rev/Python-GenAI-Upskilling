# Word2Vec & GloVe

<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Understand Word2Vec at high level
- Utilize the technique using Gensim
  
</details>

<details>

<summary>Description</summary>

Both Word2Vec and GloVe are word embedding techniques that represents words as vectors, allowing the models to capture of semantic relationships and meanings between words. They are standard methods of generating word embeddings, and has a variety of applications, such as text similarity, recommendation systems, and sentimental analysis.

## Word Embedding
Word embeddings are vectors of words created via an embedding technique. Converting words and sentences to vector embeds allows mathematical operations to be done on them, helping to establish the association of a word with other words with similar meaning. For example, the words such as dog and cat will be placed closer together compared to a word such as 'fire'

## Word2Vec
Word2Vec is a word embedding technique that operates under the following assumption: two words sharing similar contexts also share a similar meaning.

It comprises two main architectures: Continuous Bag of Words (CBOW) and Skip-gram.
CBOW predicts a target word based on its context (surrounding words) and Skip-gram predicts the context words given a target word.

The main takeaway here is that Word2Vec is a predictive model focused on the local context.

## GloVe
GloVe stands for Gloval Vectors for Word Representation. It is similar to Word2Vec in a way that it takes a corpus of text and turns them into word embeddings. However, unlike Word2Vec, GloVe is not a predictive model. It instead relies on constructing a global co-occurrence matrix that counts how frequently a word appears in a given context. Moreover, since GloVe constructs a global co-occurance matrix, it is aware of how the given word is used in the entire corpus instead of in the window. 


</details>

<details>
<summary>Implementation</summary>
The library Gensim provides python implementation and already trained models for Word2Vec. In this module, we'll focused on utilizing the pre-trained models for Word2Vec, but GloVe also provides a similar functionality.

## Word2Vec
We'll use the pretrained model from Gensim to explore word2vec's features.
This particular model has been trained on the entire Google News dataset, of about 100 billion words.

```python
import gensim.downloader as api

w2v = api.load('word2vec-google-news-300')
```

Get the most frequently appearing words
```python
print(f"Out of total {len(w2v.index_to_key)} words")
for index, word in enumerate(w2v.index_to_key):
    if index <= 10:
        print(f"#{index}: {word}")
    else:
        break
```
Output: 
Out of total 3000000 words
#0: </s>
#1: in
#2: for
#3: that
#4: is
#5: on
#6: ##
#7: The
#8: with
#9: said
#10: was

We can also get the vector representation of the word it knows
```python
vec_computer = w2v['computer']
print(vec_computer)
```

It is known shortcoming of Word2Vec that it cannot infer vectors of an unknown words
```python
w2v['revature'] #will throw a KeyError
```

We can also do similarity comparisions
```python
pairs = [
    # Going from more similar to less similar 
    ('cup', 'mug'),
    ('cup', 'bowl'),  
    ('cup', 'beverage'),
    ('cup', 'cat'),  
]
for w1, w2 in pairs:
    print('%r\t%r\t%.2f' % (w1, w2, w2v.similarity(w1, w2)))
```
Output is the following:
'cup'	'mug'	0.46
'cup'	'bowl'	0.40
'cup'	'beverage'	0.27
'cup'	'cat'	0.13

It can also retrieve the most similar words to the list of words given
```python
print(w2v.most_similar(positive=['cup', 'mug'], topn=5))
# [('cups', 0.6790143847465515), ('coffee_mug', 0.6448789238929749), ('mugs', 0.6135846376419067), ('jug', 0.5957605242729187), ('pint_glass', 0.5718879103660583)]
```
The higher the number, more similar they are in meaning.

The doesnt_match function takes in a list and finds the least similar word.
```python
print(w2v.doesnt_match(['cup', 'cat', 'mug', 'jar']))
# cat
```
</details>