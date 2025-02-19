<details><summary>Prerequisites & Learning Objectives</summary>

# Prerequisites and Learning Objectives for the <> topic

## Prerequisites

- None

## Learning Objectives

After completing this module, associates should be able to:

- Explain what Machine Learning is
- Identify practical use cases for machine learning
</details>

<details><summary>Description</summary>

# Description for the Machine Learning Introduction topic

## Machine Learning
Machine Learning (ML) is a sub-field of Artificial Intelligence. ML involves the development of programs that can perform tasks without explicit instructions. ML revolves around data, whether this is the input data that is used to train the model or the predictions that the model can create for new data. 

### Supervised Learning

The model uses known input data to make inferences about new data.

#### Training Data

For example, an ML model can be trained on thousands of pictures of clothing with verified labels (coats, pants, etc.). By analyzing these pictures along with the labels that are guaranteed to be correct, the ML model can "learn" the factors that indicate why a given image of clothes is labeled as "pants", for example.

#### Making Predictions

Using this understanding, the model can make predictions about entirely new data. If given a new picture of clothes, with no label, the model can try to predict what type of clothing is depicted in the picture based on what it learned from the training data. This way, ML can make human-like predictions on data.

#### Testing Data

Sometimes, test data is used to evaluate a model's accuracy. By having the model predict labels for a separate set of known data, we can compare these results with the actual label and thus compute a percentage of images guessed. For example, if a testing data set contained 5 pictures of pants and 5 pictures of socks, and the model predicted that every single picture is a picture of pants, then the model would have a 50% accuracy rate. 

### Unsupervised Learning
With unsupervised learning, the model is not given labels on its input data. Instead, it tries to infer whatever information it can by identifying patterns or groupings of data. For example, a model could group academic grading data together and/or identify outlying data points. 

### Semi-Supervised Learning 
This approach takes both labeled and unlabelled data as inputs. The model analyzes the unlabelled data and uses these learnings to classify the unlabelled data. This approach can be used to parse images for text or classify images. 

### Reinforcement Learning
With reinforcement learning, there are usually one or more rewards involved that drive the learning. The model interacts with an environment and receives these rewards as feedback. An example of this is the development of self-driving cars in which the model analyzes the driving environment and learns to prioritize decisions that yield the highest rewards (avoiding accidents, obeying laws, etc.)
</details>

<details><summary>Real World Application</summary>

## Real World Application for the <> Topic
Machine Learning is extremely helpful in the real world, as it allows computers to perform tasks that would take many minutes or hours for humans to do. The following is a non-exhaustive list of common use cases for ML. 

### Facial Recognition
ML models can detect faces which is helpful for facial authentication or grouping photos based on who appears on the photo. 

### Text Analysis
When filling out forms by hand, ML models can interpret these images of handwriting and translate them into the exact characters that are written.

### Image Classification
Taking an image and breaking it down into a specific grouping/label has many applications, such as cataloging a store's inventory or detecting unsafe/harmful images that are uploaded to a social media site.

### Self-Driving Cars
Self-driving cars operate by analyzing pictures of their environment and taking the best corresponding action.

### Spam/Phishing Filtering
Emails that are sent with the purpose of persuading you to purchase a product or give away secure information exhibit patterns that can be picked up by ML models. 

### Medical Diagnosis
ML can be used for medical diagnoses. Given symptoms or other data as input, ML models can diagnose which disease is the root cause and what treatments can be given.
</details>

<details><summary>Implementation</summary>

</details>

<details><summary>Summary</summary>

# Summary for the Machine Learning Introduction topic

- Machine Learning is a sub-field of AI that attempts to perform evaluation and calculations without explicit instructions. 
- Machine Learning can be split into
    - Supervised - given labelled data
    - Unsupervised - given unlabelled data
    - Semi-Supervised - given some labeled and some unlabelled data
    - Reinforcement - responds to "rewards" in the environment
- Applications of ML
    - Facial Recognition
    - Medical Diagnoses
    - Self-Driving Cars
    - Text Recognition
</details>

