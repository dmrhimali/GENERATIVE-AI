Evaluating a fine-tuned conversational AI model (such as a text generation or response generation model) involves multiple steps, including generating responses, comparing them to human-provided ground truth responses, and using appropriate evaluation metrics. Here's a step-by-step guide for evaluating your fine-tuned conversational AI model (e.g., GPT-2, DialoGPT, or a BART-based model) using Google Colab.

### Step 1: Set Up the Environment in Colab

First, make sure you install the necessary libraries. In Google Colab, run the following:

```python
!pip install transformers datasets
```

This installs:
- **transformers**: To use Hugging Face models and tokenizers.
- **datasets**: To load evaluation datasets.

### Step 2: Import Required Libraries

Import the libraries needed to load your model and evaluate it.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
```

### Step 3: Load Your Fine-Tuned Model and Tokenizer

Load your fine-tuned conversational AI model. If you’ve fine-tuned the model locally, you can load it using the path to the fine-tuned model. If it's uploaded to the Hugging Face Hub, you can load it directly by specifying the model name.

```python
# Load your fine-tuned conversational model (replace with your model's path or name)
model_name = "path_to_your_finetuned_model"  # e.g., "DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

For example, if you're using **DialoGPT** as a base model, you would use `"microsoft/DialoGPT-medium"`.

### Step 4: Load an Evaluation Dataset

Load a conversational dataset to evaluate the chatbot’s performance. For conversational AI, datasets like **DailyDialog** or **Cornell Movie Dialogues** are commonly used.

You can load a dataset from Hugging Face Datasets like **DailyDialog**:

```python
# Load a conversational dataset for evaluation (DailyDialog as an example)
dataset = load_dataset("daily_dialog", split="validation[:10]")  # Taking a small sample
```

Alternatively, you can load your custom dataset if you have one. Ensure that your dataset has two fields: the **input** (e.g., the user's message) and **output** (e.g., the chatbot's response).

### Step 5: Tokenize and Prepare Data

Next, preprocess the input by tokenizing the text. This step is necessary to convert the text data into the format the model expects.

```python
def preprocess_data(examples):
    # Tokenize inputs and outputs for the conversational model
    input_encodings = tokenizer(examples['utterance'], truncation=True, padding=True, return_tensors="pt")
    return input_encodings

dataset = dataset.map(preprocess_data, batched=True)
```

In this case, we're tokenizing the `utterance` field from the DailyDialog dataset, which contains the user's messages.

### Step 6: Generate Responses with the Fine-Tuned Model

You can now generate responses using your fine-tuned model. Here, we will loop over the dataset and generate responses based on the user's input.

```python
def generate_response(example):
    # Prepare the input for the model
    input_ids = example['input_ids']
    attention_mask = example['attention_mask']

    # Generate a response from the model
    generated_ids = model.generate(input_ids=input_ids, attention_mask=attention_mask, num_beams=5, max_length=50)

    # Decode the generated response
    generated_response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    return {"generated_response": generated_response}

# Apply the function to generate responses
generated_responses = dataset.map(  , batched=False)

# Display some results
for i in range(3):
    print(f"Input: {dataset[i]['utterance']}")
    print(f"Generated Response: {generated_responses[i]['generated_response']}\n")
```

This will generate responses for the first 3 examples in the validation set. You can modify this code to generate responses for more examples.

### Step 7: Evaluate Generated Responses Using Metrics

Now, let's evaluate the quality of the generated responses. Common metrics for conversational AI evaluation include **BLEU**, **ROUGE**, and **METEOR**.

You can use **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) to measure the overlap between the generated responses and the ground truth responses. This is a popular metric for text generation tasks.

#### 7.1: Evaluate Using ROUGE Score

```python
from datasets import load_metric

# Load ROUGE metric
rouge = load_metric("rouge")

# Define function to compute ROUGE score
def compute_rouge(example):
    predictions = example['generated_response']
    references = example['response']  # Assuming 'response' is the ground truth response in the dataset
    return rouge.compute(predictions=[predictions], references=[references])

# Apply ROUGE computation to the dataset
rouge_scores = generated_responses.map(compute_rouge, batched=False)

# Print out the ROUGE scores for the first few samples
print(rouge_scores[:3])  # Display the ROUGE scores for the first three examples
```

This computes ROUGE scores for the generated responses and compares them to the ground truth. ROUGE scores are available for:
- **ROUGE-1** (unigram overlap),
- **ROUGE-2** (bigram overlap),
- **ROUGE-L** (longest common subsequence).

You can analyze the ROUGE results to understand how well the generated responses align with the ground truth responses.

#### 7.2: Evaluate Using BLEU Score (Optional)

BLEU is another popular metric, primarily used for machine translation but also applicable for evaluating text generation tasks like this. You can compute BLEU scores using **NLTK** or the Hugging Face `datasets` library.

```python
from nltk.translate.bleu_score import sentence_bleu

# Define function to compute BLEU score
def compute_bleu(example):
    predictions = example['generated_response']
    references = example['response'].split()  # Tokenize the ground truth response
    prediction_tokens = predictions.split()
    score = sentence_bleu([references], prediction_tokens)
    return {"bleu_score": score}

# Apply BLEU score computation
bleu_scores = generated_responses.map(compute_bleu, batched=False)

# Display BLEU scores for the first few samples
print(bleu_scores[:3])  # Display the BLEU scores for the first three examples
```

#### 7.3: Evaluate Using METEOR (Optional)

The **METEOR** metric accounts for synonymy, stemming, and word order, which can be useful for text generation tasks.

```python
from nltk.translate.meteor_score import meteor_score

# Define function to compute METEOR score
def compute_meteor(example):
    prediction = example['generated_response']
    reference = example['response']
    score = meteor_score([reference], prediction)
    return {"meteor_score": score}

# Apply METEOR score computation
meteor_scores = generated_responses.map(compute_meteor, batched=False)

# Display METEOR scores for the first few samples
print(meteor_scores[:3])  # Display the METEOR scores for the first three examples
```

### Step 8: Summarize and Analyze Results

Once you've computed the evaluation metrics (e.g., ROUGE, BLEU, METEOR), you can summarize and analyze them to see how well your fine-tuned model performs. Look for patterns:
- High ROUGE or BLEU scores suggest your model is generating relevant, coherent responses.
- Low scores may indicate that the model struggles to generate responses that are similar to the ground truth.

#### Example Evaluation Output:
```python
# Example output format for evaluation results:
print("ROUGE Scores:", rouge_scores)
print("BLEU Scores:", bleu_scores)
print("METEOR Scores:", meteor_scores)
```

### Optional: User Evaluation (Human Evaluation)
For conversational AI, **manual evaluation** or **user evaluation** is also highly recommended. This involves asking human evaluators to rate the generated responses on:
- **Fluency** (Is the response grammatically correct?),
- **Relevance** (Is the response relevant to the input?),
- **Engagement** (Does the response encourage further conversation?),
- **Empathy** (If applicable, does the response express empathy or emotional intelligence?).

### Conclusion

You’ve successfully learned how to:
1. Load your fine-tuned conversational AI model and tokenizer.
2. Prepare and tokenize an evaluation dataset.
3. Generate responses from your fine-tuned model.
4. Evaluate the generated responses using metrics like **ROUGE**, **BLEU**, and **METEOR**.
5. Optionally, conduct **user evaluation** for further qualitative analysis.

By evaluating your fine-tuned conversational AI model using both automated metrics and human feedback, you can get a well-rounded view of its performance and identify areas for improvement.





# Prepare a new dataset with a single text field with Amod/mental_health_counseling_conversations dataet original fields to match fine tuned dataset heliosbrahma/mental_health_chatbot_dataset fields
# def process_example(example):
#   example["text"] = "<HUMAN>: "+example["Context"] + "<ASSISTANT>: "example["Response"]
#   return example

# dataset = dataset.map(process_example)
# new_dataset = []
# for example in dataset:
#     processed_example = function(example)
#     example.update(processed_example)
#     new_dataset.append(example)
# return new_dataset
