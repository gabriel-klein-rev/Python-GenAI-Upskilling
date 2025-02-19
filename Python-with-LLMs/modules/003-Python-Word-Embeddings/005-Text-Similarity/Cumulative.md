# Text Similarity

<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Define text similarity and explain its significance in natural language processing
- Understand common methods for text similarity, such as cosine similarity and word embeddings
- Provide real world examples where text similarity is used
- apply text similarity comparison using NLTK library

</details>

<details>

<summary>Description</summary>

Text similarity measures the likeness between two texts, aiming to quantitatively assess the extent of shared content or meaning. Various techniques, including cosine similarity, Euclidean distance, and the Jaccard Index, are employed for different purposes.

Text similarity finds application in diverse areas such as information retrieval, recommendation systems, sentiment analysis, summarization, and plagiarism detection.

In this module, we focus on cosine similarity, and its use with word embeddings.

## Cosine Similarity
Cosine similarity aims to measure the similarity between two texts based on the angle between their respective word vectors. It is often applied to vectors representing the frequency of words in a sentence or document.

To calculate the cosine similarity between two texts, we first represent the texts in vector form. As mentioned earlier, these vectors indicate how frequently certain words are used in a given text. Subsequently, we normalize the vectors to a unit vector, one with a length of 1. Finally, cosine similarity is computed as the dot product of the two vectors, divided by the product of their lengths.

Cosine Similarity is a straightforward and simple technique to compare the similarity of two pieces of text. It works particularly well with sparse data, such as the bag-of-words representation. However, its use of sparse vectors, which do not store information about where a word occurs in a sentence or the role it plays, presents some limitations. Because of this, cosine similarity may lose semantic meaning, as it only considers the frequency of words appearing in the text.

Cosine Similarity is widely used in NLP and information retrieval, particularly in recommendation systems and document classification and clustering.

### Cosine Similarity with Embeddings
As mentioned earlier, cosine similarity commonly operates with sparse vectors. However, when applied to dense vectors produced by an embeddings model, cosine similarity enables the comparison of text bodies while capturing their semantics.

## Eucledean Distance 
Euclidean Distance is another distance metric used to measure the dissimilarity between two vectors or points in space. While cosine similarity captures the angle between vectors, Euclidean Distance quantifies the actual spatial distance. Here's an explanation:

### Euclidean Distance and Text Similarity:
In the context of text similarity, Euclidean Distance is often used to measure the dissimilarity between vectors representing documents or sentences.

Texts are treated as points in a high-dimensional space, where each dimension corresponds to a feature or term. The Euclidean Distance between these points reflects their dissimilarity.

## Jaccard similarity
Jaccard similarity is a measure of similarity between two sets. It is defined as the size of the intersection divided by the size of the union of the sets. The formula for Jaccard similarity is the size of intersection of two sets over the size of union of two sets.

In NLP, the Jaccard similarity is often used to compare the similarity between two sets of words. For example, it can be used to measure the similarity between two documents based on the sets of words they contain. This is particularly useful in tasks like document clustering, duplicate detection, and information retrieval.

Unlike Cosine similarity, Jaccard similarity is not sensitive to word frequency. It is a measure of set similarity, focusing on the presence or absence of elements rather than their frequency. The calculation considers the size of the intersection and the size of the union of sets, but the actual frequency of elements within the sets is not taken into account. As a result, Jaccard similarity provides a binary indication of whether elements are shared between sets, regardless of how many times they occur. This property makes it particularly useful in scenarios where the emphasis is on set membership rather than frequency, such as in document similarity or recommendation systems.

</details>

<details>
<summary>Implementation</summary>

The following demonstrates calculating cosine similarity between two texts using sklearn


```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample texts
text1 = "Natural language processing is fascinating."
text2 = "I'm intrigued by the wonders of natural language processing."

# Tokenize and vectorize the texts
vectorizer = CountVectorizer().fit_transform([text1, text2])

# Calculate cosine similarity
cosine_sim = cosine_similarity(vectorizer)

# Print the cosine similarity matrix
print(f"Cosine Similarity: {cosine_sim}")
```

The following is an sample implementation of Jaccard Similarity:

```python
# Function to calculate Jaccard similarity between two sets
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Sample sets of words
set1 = {"natural", "language", "processing", "fascinating"}
set2 = {"intrigued", "by", "the", "wonders", "of", "natural", "language", "processing"}

# Calculate Jaccard similarity
jaccard_sim = jaccard_similarity(set1, set2)

# Print the Jaccard similarity
print(f"Jaccard Similarity: {jaccard_sim}")
``` 
</details>