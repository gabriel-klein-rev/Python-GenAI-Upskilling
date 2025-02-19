# POS Tagging 

<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Understand Part of Speech tagging and their usecases
- Implement POS Tagging using NLTK

</details>

<details>

<summary>Description</summary>

Part of Speech(POS) Tagging refers to a task that identifies each token with their part of speech. Part of speech is a grammatical concept that denotes which role a word is playing in a sentence. The examples of them would be noun, verb, adverbs, adjectives, pronouns, etc. 

The significance of POS tagging lies in its ability to enhance the understanding and analysis of textual data. Without POS tagging, we would be limited to the vocabularies and frequencies of appearance in the text. However, by tagging each token with part of speech, it allows models to understand the context and the words usage in a sentence. 

POS tagging is employeed frequently in tasks such as sentiment analysis, syntax analysis, speech recognition, and grammar and style checking. Moreover, it is a precursor to Named Entity Recognition, which will be introduced in the next module.


</details>

<details>
<summary>Implementation</summary>
We will be using NLTK's POS Tagging class for the implementation

```python
from nltk.tag import pos_tag, pos_tag_sents
from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "John's big idea isn't all that bad."
print(pos_tag(word_tokenize(sentence)))
# [('John', 'NNP'), ("'s", 'POS'), ('big', 'JJ'), ('idea', 'NN'), ('is', 'VBZ'), ("n't", 'RB'), ('all', 'PDT'), ('that', 'DT'), ('bad', 'JJ'), ('.', '.')]

# With multiple sentences, we can use pos_tag_sents function
multiple_sentences_text = "Can you really have too many pens? They all serve different purposes and one simply cannot have too many!"

# We first break it up to each sentence
sentence_tokens = sent_tokenize(multiple_sentences_text)

#and then word tokenize each sentence, so the structure is List[List[string]]
word_tok_mult_sents = [word_tokenize(sent) for sent in sentence_tokens]

# finally call the pos_tag_sents function
print(pos_tag_sents(word_tok_mult_sents))
# [[('Can', 'MD'),
#   ('you', 'PRP'),
#   ('really', 'RB'),
#   ('have', 'VB'),
#   ('too', 'RB'),
#   ('many', 'JJ'),
#   ('pens', 'NNS'),
#   ('?', '.')],
#  [('They', 'PRP'),
#   ('all', 'DT'),
#   ('serve', 'VBP'),
#   ('different', 'JJ'),
#   ('purposes', 'NNS'),
#   ('and', 'CC'),
#   ('one', 'CD'),
#   ('simply', 'RB'),
#   ('can', 'MD'),
#   ('not', 'RB'),
#   ('have', 'VB'),
#   ('too', 'RB'),
#   ('many', 'JJ'),
#   ('!', '.')]]

```

The following is the table of POS tags in the default NLTK tagset.
|Tag Name | Part of Speech                                                           |
|---------|--------------------------------------------------------------------------|
|CC       | Coordinating Conjunction                                                 |
|CD       | Cardinal Digit                                                           |
|DT       | Determiner                                                               |
|EX       | Existential There. Example: “there is” … think of it like “there exists” |
|FW       | Foreign Word.                                                            |
|IN       | Preposition/Subordinating Conjunction.                                   |
|JJ       | Adjective.                                                               |
|JJR      | Adjective, Comparative.                                                  |
|JJS      | Adjective, Superlative.                                                  |
|LS       | List Marker 1.                                                           |
|MD       | Modal.                                                                   |
|NN       | Noun, Singular.                                                          |
|NNS      | Noun Plural.                                                             |
|NNP      | Proper Noun, Singular.                                                   |
|NNP      | S Proper Noun, Plural.                                                   |
|PDT      | Predeterminer.                                                           |
|POS      | Possessive Ending. Example: parent’s                                     |
|PRP      | Personal Pronoun. Examples: I, he, she                                   |
|PRP      | $ Possessive Pronoun. Examples: my, his, hers                            |
|RB       | Adverb. Examples: very, silently,                                        |
|RBR      | Adverb, Comparative. Example: better                                     |
|RBS      | Adverb, Superlative. Example: best                                       |
|RP       | Particle. Example: give up                                               |
|TO       | to. Example: go ‘to’ the store.                                          |
|UH       | Interjection. Example: errrrrrrrm                                        |
|VB       | Verb, Base Form. Example: take                                           |
|VBD      | Verb, Past Tense. Example: took                                          |
|VBG      | Verb, Gerund/Present Participle. Example: taking                         |
|VBN      | Verb, Past Participle. Example: taken                                    |
|VBP      | Verb, Sing Present, non-3d take                                          |
|VBZ      | Verb, 3rd person sing. present takes                                     |
|WDT      | wh-determiner. Example: which                                            |
|WP       | wh-pronoun. Example: who, what                                           |
|WP$      | possessive wh-pronoun. Example: whose                                    |
|WRB      | wh-abverb. Example: where, when                                          |

</details>