# Named Entity Recognition

<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Gain a foundational understanding of Named Entity Recognition (NER), including the definition and purpose.
- Familiarize with the significance of NER in natural language processing and its applications in various domains.
- Implement simple NER using NLTK library

</details>

<details>

<summary>Description</summary>

Named entities are proper nouns that refer to specific entities. They can be a person, organization, location, date, etc. For example, in the sentence "Bill Gates and Paul Allen founded Microsoft", we have three named entities. Bill Gates and Paul Allen are two named entities, of type person, and Microsoft is the third, of type organization. 

Commonly Used Types of Named Entity is the following:

|Named Entity Type       |Examples                                |
|------------------------|----------------------------------------|
|ORGANIZATION            |Georgia-Pacific Corp., WHO              |
|PERSON                  |Eddy Bonte, President Obama             |
|LOCATION                |Murray River, Mount Everest             |
|DATE                    |June, 2008-06-29                        |
|TIME                    |two fifty a m, 1:30 p.m.                |
|MONEY                   |175 million Canadian Dollars, GBP 10.40 |
|PERCENT                 |twenty pct, 18.75 %                     |
|FACILITY                |Washington Monument, Stonehenge         |
|GPE(GeoPoliticalEntity) |South East Asia, Midlothian             |

Named entity recognition, or NER, is the process of extracting Named Entities from the text. It has many different use cases in the real world. Let's explore a few:

1. Classifying content: Being able to identify a named entity allows a model to scan contents/documents/articles and appropriately categorize them based on their keywords
2. Content Recommendation: Similar to content classification, the model can detect the named entity (NE) in the content user prefers and suggest contents that also contain the similar set of NE.
3. Personally Identifying Information Detection and Removal: Personally Identifying Information, or PII, is any information that can be used to identify a person. This can be a person's name, phone number, or address. PII detection and removal uses NER to detect possible PIIs.


</details>

<details>
<summary>Implementation</summary>
NLTK offers a convenient ne_chunk function to detect Named Entities. Following is a code snippet that will walk you through the process of extracting NE and plotting the resulting tree.

```python
from nltk import ne_chunk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

ner_text = """
John Doe, a software engineer at ACME Corporation, recently attended a conference in New York City on January 15-17, 2023. The event, organized by Tech Innovations Inc., focused on artificial intelligence and machine learning. During the conference, John had the opportunity to network with professionals from Google, Microsoft, and other leading tech companies.
"""

tokens = word_tokenize(ner_text)
print(tokens)

pos_tagged = pos_tag(tokens)
print(pos_tagged)

tree = ne_chunk(pos_tagged)

tree.draw()
```
The function successfully identifies 'John Doe', 'ACME Corporation', 'New York City', 'Tech Innovations', 'Google', and 'Microsoft' as named entities.

</details>