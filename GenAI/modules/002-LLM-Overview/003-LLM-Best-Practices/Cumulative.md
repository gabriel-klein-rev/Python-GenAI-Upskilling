<details><summary>Prerequisites & Learning Objectives</summary>

# Prerequisites and Learning Objectives for the LLM Best Practices topic

## Prerequisites

- Foundational Knowledge of LLMs

## Learning Objectives

After completing this module, associates should be able to:

- Understand the best practices for using LLMs

</details>

<details><summary>Description</summary>

# Description for the LLM Best Practices topic

LLMs, or Large Language Models, are extremely powerful tools that can be used for many different tasks. Accordingly, it is important to keep the following best practices in mind to maximize the effectiveness of LLMs. 

## Best Practices
1. Prompt Clarity - When writing prompts, the prompts should explicitly convey what should be accomplished. This can include
    - The task to be accomplished
    - The context of the task
    - The desired format of the output
    - What should NOT be included in the output
    - Examples of some desired output
    - Note that clarity doesn't necessarily convey length. Short prompts are fine as long as they include all necessary information. Long prompts are also fine as long as they don't include "fluff" or irrelevant information. 
2. Choose the Most Appropriate LLM - Because there are many different LLMs available, we have the luxury of choosing the LLM that most closely fits the need of what are trying to accomplish
    - GPT - GPT is a general choice for a wide variety of tasks. It can be useful for answering questions, generating some sample text, summarizing texts, etc.
    - Copilot - Copilot is a great choice for code-related tasks. Copilot can help generate code, review code, answer questions about code, etc.
3. Verify Correctness - Since LLMs are not perfect, it is important to verify the generated output using some other means. The following methods can be used to verify the correctness of generated output.
    - Simple Inspection - By simply looking at the output, it is sometimes possible to detect errors and flaws (grammatical, factual, etc.)
    - Peer Review - Having a peer review the output can also help detect errors and flaws that might fly under your radar
    - Research - If the output contains factual information, it can be verified by comparing said information to other online sources
    - Execution - Particularly with generated code, running the code and examining the output can help determine if the generated code is correct
    - Using other LLMs - A different LLM can be used to verify the correctness of a response. This could be done in 2 ways:
        - Explicitly asking "Is this {answer} factually and grammatically correct? And does it properly answer the {question}?"
        - Using a different LLM to generate a response to the same question and comparing the two responses
4. Security - Security is such a broad topic that will be explored in great detail in future modules. In short, however, it is best to keep a "better safe than sorry" approach when dealing with LLMs. This means, for example, if you are unsure if the information you want to provide an LLM is sensitive, it is best to assume that it *is* sensitive and not provide it to the LLM.
</details>

<details><summary>Implementation</summary>

## Implementation for the LLM Best Practices topic

Imagine a sample scenario. We will use an LLM to solve the scenario and employ best practices as we do so. 

### Scenario
Imagine we have a simple Customer class:

```python
class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.address
```

We want to use an LLM to generate a function that will take in a list of customers and return a list of customers who are over 18 years old. 

### The Solution

#### Picking the Correct Tool
Before we think about constructing our prompt, we should pick an appropriate tool. Since we are dealing with code generation, we know that Copilot is a great tool for this task. 

Alternatively, we could use other coding-based LLMs such as Codeium, or even a non-coding-based LLM such as ChatGPT. Of course, Codeium or Copilot would be the best choices for this task. 

#### Constructing the Prompt
Prompts should be clear, concise, and explicit. When generating methods, the arguments and return types can also be specified. The prompt for this scenario could be something like:

"Generate a Python function that takes in a list of Customer objects and returns a list of Customer objects whose age is greater than 18."

This prompt is fairly clear and isn't too long. It specifies the input, output, and desired behavior of the function. 

#### Verify Correctness
After the function is generated, we can inspect the code to verify correctness. We can also run the code against some sample Customer objects and verify that all returned Customer objects are over 18 years old.

Imagine this is the generated code:
```python
def filter_customers(customers):
    filtered = []
    for customer in customers:
        if customer.age > 18:
            filtered.append(customer)
    return filtered
```

Upon inspection, we notice that the function body creates an empty list, iterates through the given list of customers, and appends the customer to the empty list if the customer's age is greater than 18. This seems correct! To gain even more assurance, we can run the following code:

```python
customers = [Customer("John", 17, "123 Main St"), Customer("Jane", 21, "456 Main St"), Customer("Joe", 15, "789 Main St")]

for customer in filter_customers(customers):
    print(str(customer))
```

and check that all printed customers are over 18 years old.

#### Security
Since this is an isolated scenario, it is hard to imagine what type of security considerations should be taken into place. Do we need to hide information such as name, address, or age?

For this example, we can assume that address data should not be returned from this function. We can update the original prompt:

"Generate a Python function that takes in a list of Customer objects and returns a list of Customer objects whose age is greater than 18. The returned Customer objects should not include the address field."

And we might get this code:

```python
def filter_customers(customers):
    filtered = []
    for customer in customers:
        if customer.age > 18:
            filtered.append(Customer(customer.name, customer.age, ""))
    return filtered
```

Inspecting this code reveals that the address is entered as an empty string. We can also run the previous code to ensure that the address is not printed out.

### Conclusion
Using the LLM best practices, we were able to generate some code that addresses the scenario. We also have reasonable assurance that the generated code is correct and secure.
</details>

<details><summary>Summary</summary>

# Summary for the LLM Best Practices topic

- It is important to keep the following practices in mind when working with LLMs:
    - Prompt Clarity
    - Choosing the Most Appropriate LLM
    - Verifying Correctness
    - Security
- Security is a broad topic and will be explored in greater detail in future modules
</details>

