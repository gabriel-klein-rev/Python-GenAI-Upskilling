# RAG Architecture

<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Understand the components of RAG architecture
- Explain the integration of retrieval and generation components
</details>

<details>

<summary>Description</summary>

## Retrieval Component:
- Information Retrieval Model: The retrieval component begins with an information retrieval model. This model is responsible for selecting relevant information from a knowledge base or a set of documents based on the input query or context.
- Knowledge Base or Document Store: The retrieved information is sourced from a knowledge base or document store. This repository can be a sql database, data warehouse, or vector database consisting of a wide range of texts, documents, or passages relevant to the domain or task.

## Generation Component:
Generation Model: Once relevant information is retrieved, the generation component takes over. This could involve a pre-trained language model such as GPT (Generative Pre-trained Transformer) or a more specialized model. The generation model is responsible for producing contextually appropriate and coherent responses or completions based on the retrieved content.
</details>