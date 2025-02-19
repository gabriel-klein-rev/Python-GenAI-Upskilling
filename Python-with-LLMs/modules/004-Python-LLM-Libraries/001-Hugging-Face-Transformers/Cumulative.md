# Guide to Using Hugging Face Transformers
<details><summary>Learning Objectives</summary>

After completing this activity, participants should be able to:
- Understand Hugging Face Transformers.
- Use pre-trained models for various NLP tasks.
- Understand the main concepts like tokenization, model architectures, and pipelines.
- Apply Transformers to specific tasks like text classification, language modeling, and more.

</details>
<details><summary>Description</summary>

Transformers is a library that provides pre-trained models for a wide range of NLP tasks, including language translation, text generation, and sentiment analysis. It is built on top of PyTorch and TensorFlow and is known for its user-friendly API.

#### Key Features:
1. **Ease of Use**: The library is designed to be user-friendly, making advanced models accessible to both beginners and experienced practitioners.
2. **Wide Range of Models**: Supports many architectures for tasks like text classification, information extraction, and more.
3. **Flexibility**: Easily switch between models and tasks, allowing for experimentation and fine-tuning.
4. **Costs**: Reduced compute costs.
5. **Integration**: Easy integration with popular deep learning frameworks.


#### Installation:
To install Transformers, use pip:
```bash
pip install transformers
```

You’ll also need to install your preferred machine learning framework:

Pytorch

```bash
pip install torch
```

or TensorFlow

```bash
pip install tensorflow
```


#### Quick Start:
Here's a simple example of using a pre-trained model:
```python
from transformers import pipeline

# Using a pipeline for sentiment analysis
classifier = pipeline('sentiment-analysis')
print(classifier('Transformers library is amazing!')) 
# Expected Output: [{'label': 'POSITIVE', 'score': 0.9998774528503418}]
```

</details>
<details><summary>Implementation</summary> 

### Basic Usage

#### Tokenization and Models
Before feeding text to a model, it needs to be appropriately tokenized. The Transformers library provides a tokenizer for each model.

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Tokenizing text
inputs = tokenizer("Hello, world!", return_tensors="pt")
outputs = model(**inputs)
```
Note that the tokenizer's output prepares the input text for processing by a transformer model by converting it into a numerical format `input_ids`, indicating sentence boundaries or segments `token_type_ids`, and distinguishing real tokens from padding `attention_mask`. This format allows the transformer models to understand and process the input text effectively. BERT model can now process the input. 
#### Pipelines
Pipelines simplify the use of models for specific tasks.


1. **Text Classification (Sentiment Analysis)**
   ```python
   from transformers import pipeline

   classifier = pipeline("sentiment-analysis")
   result = classifier("I love using Transformers for my NLP tasks!")
   print(result)
   # Expected Output: [{'label': 'POSITIVE', 'score': 0.9998}]
   ```

2. **Text Generation**
   ```python
   from transformers import pipeline

   text_generator = pipeline("text-generation")
   generated_text = text_generator("In a world dominated by AI,")[0]['generated_text']
   print(generated_text)
   # Expected Output: In a world dominated by AI, many have long imagined a world where everyone is super rich. We've only just begun.
   ```

3. **Summarization**
   ```python
   from transformers import pipeline

   summarizer = pipeline("summarization")
   summary = summarizer("Summarization models are trained on large datasets to generate concise and relevant summaries of text. However, their behavior can be unpredictable, especially with shorter texts. The model might sometimes add contextual information it deems relevant, which can make the summary longer or appear to rephrase rather than condense the original text. Adjusting the paramaters and testing is recommended.")[0]['summary_text']
   print(summary)

   # Expected Output: Summarization models are trained on large datasets to generate concise and relevant summaries of text. However, their behavior can be unpredictable, especially with shorter texts. The model might sometimes add contextual information it deems relevant, which can make the summary longer. Adjusting the paramaters and testing is recommended.
   ```

4. **Image Classification**
   ```python
   from transformers import pipeline
   from PIL import Image

   image_classifier = pipeline("image-classification")
   image = Image.open("path/to/your/image.jpg")
   classification = image_classifier(image)
   print(classification)
   # Expected Output using an image of a person with a laptop next to a tv: [{'score': 0.28740382194519043, 'label': 'desktop computer'}, {'score': 0.2583736479282379, 'label': 'screen, CRT screen'}, {'score': 0.12644484639167786, 'label': 'television, television system'}, {'score': 0.07730545848608017, 'label': 'monitor'}, {'score': 0.055994920432567596, 'label': 'home theater, home theatre'}]
   ```
   This pipeline can recognize various objects, scenes, and activities in images. The classification results are the model's predictions about what is depicted in the image, along with confidence scores for each prediction

5. **Image Segmentation**
   ```python
   from transformers import pipeline
   from PIL import Image

   image_segmenter = pipeline("image-segmentation")
   image = Image.open("path/to/your/image.jpg")
   segmentation = image_segmenter(image)
   print(segmentation)
   # Expected Output: [{'score': 0.980521, 'label': 'laptop', 'mask': <PIL.Image.Image image mode=L size=4032x3024 at 0x2BB5511E7D0>}, {'score': 0.996581, 'label': 'LABEL_199', 'mask': <PIL.Image.Image image mode=L size=4032x3024 at 0x2BB55BCE950>}, {'score': 0.997768, 'label': 'tv', 'mask': <PIL.Image.Image image mode=L size=4032x3024 at 0x2BB55BCE590>}, {'score': 0.998046, 'label': 'LABEL_200', 'mask': <PIL.Image.Image image mode=L size=4032x3024 at 0x2BB55BCE550>}, {'score': 0.97854, 'label': 'laptop', 'mask': <PIL.Image.Image image mode=L size=4032x3024 at 0x2BB55BCD5D0>}, {'score': 0.997086, 'label': 'person', 'mask': <PIL.Image.Image image mode=L size=4032x3024 at 0x2BB55BCD690>}, {'score': 0.991061, 'label': 'cup', 'mask': <PIL.Image.Image image mode=L size=4032x3024 at 0x2BB55BCD790>}]
   ```
   Classification tells you what is present in the image as a whole, whereas segmentation tells you where specific things are in the image and differentiates between different objects and features.

### Advanced Topics

#### Fine-Tuning
You can fine-tune pre-trained models on your dataset for better performance on specific tasks.

#### Custom Models
Advanced users can create custom models or modify existing architectures to suit their needs.

</details>
 