- [TL;DR: Natural Language Benchmarks](https://www.linkedin.com/pulse/tldr-natural-language-benchmarks-overlogix-cddrf/)
- [Evaluation](https://docs.mistral.ai/guides/evaluation/)
- [Let's talk about LLM evaluation](https://huggingface.co/blog/clefourrier/llm-evaluation)
- [LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)
- [LLM Evaluation: Metrics, Methodologies, Best Practices](https://www.datacamp.com/blog/llm-evaluation?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720830&utm_adgroupid=152984015254&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=724847714875&utm_targetid=aud-1645446892440:dsa-2222697810678&utm_loc_interest_ms=&utm_loc_physical_ms=9019605&utm_content=DSA~blog~Artificial-Intelligence&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-us_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-dec24&gad_source=1&gclid=CjwKCAiAmfq6BhAsEiwAX1jsZ4nBoi3CR4GL_qfTM4xvSfy2sRwvJ-SrEuNNiWZdw9lgiyJi-Q_oiRoC9tAQAvD_BwE)
-[How to Build an LLM Evaluation Framework, from Scratch](https://www.confident-ai.com/blog/how-to-build-an-llm-evaluation-framework-from-scratch)

Qustion to chatgpt: `What are the most commonly used and reliable AI benchmarks for chatbot ?`

When evaluating and benchmarking chatbots, particularly those powered by AI models like large language models (LLMs), several metrics and benchmark datasets are commonly used. These benchmarks assess various aspects of a chatbot’s performance, including its language understanding, coherence, relevance, and ability to engage in meaningful conversations. Below are some of the most widely used and reliable AI benchmarks for chatbot evaluation:

### 1. **General Language Understanding Evaluation (GLUE)**
   - https://huggingface.co/datasets/nyu-mll/glue
   - **Purpose**: GLUE is a collection of datasets and tasks designed to evaluate the performance of models on general language understanding, including tasks such as sentence similarity, textual entailment, and sentiment analysis.
   - **Usage**: While it’s not chatbot-specific, many conversational AI models are tested on GLUE to assess their ability to understand and process text at a general language level.
   - **Key Metrics**: Accuracy, F1 score, Matthews correlation coefficient (MCC).
   - **Datasets**: MNLI (Multi-Genre Natural Language Inference), QNLI (Question Natural Language Inference), SST-2 (Stanford Sentiment Treebank), etc.

### 2. **Dialogue Datasets for Evaluation**
   Several specific datasets have been created for evaluating chatbot performance in dialogue systems.

   - **DSTC (Dialogue State Tracking Challenges)**
     - **Purpose**: A series of challenges focusing on dialogue state tracking, task-oriented dialogue, and evaluation in conversational systems.
     - **Tasks**: Dialogue state tracking, response generation, and dialogue management.
     - **Metrics**: Task success rate, dialogue length, dialogue coherence, and user satisfaction.
   
   - **Persona-Chat**
     - **Purpose**: A dataset for building and evaluating chatbots with personalized conversations, focusing on how well chatbots can remember and refer to personal traits.
     - **Metrics**: Human evaluation on relevance, coherence, and diversity; BLEU, ROUGE, and METEOR for automated evaluations.
     - **Data**: Includes dialogues where participants engage with chatbots that have specific personas (e.g., hobbies, preferences).

   - **MultiWOZ (Multi-domain Wizard of OZ)**
     - **Purpose**: A dataset for evaluating task-oriented dialogue systems in multiple domains (e.g., restaurants, hotels, attractions).
     - **Metrics**: Task completion rate, dialogue success rate, and user satisfaction.
     - **Usage**: Primarily for evaluating task-oriented chatbots, focusing on the chatbot’s ability to handle multiple types of user intents and keep track of conversation context.

   - **ConvAI (Conversational Intelligence Challenge)**
     - **Purpose**: A series of challenges focused on building and evaluating conversational agents.
     - **Metrics**: Human evaluation of coherence, informativeness, and engagement; automatic evaluation using BLEU, ROUGE, etc.
     - **Data**: Human-to-human conversations with a goal to evaluate chatbot ability to engage in open-domain conversations.

### 3. **Automatic Evaluation Metrics**
   While human evaluation is a key component in assessing chatbot quality, several automatic metrics are also used, especially when large-scale testing is needed. Some common ones include:

   - **BLEU (Bilingual Evaluation Understudy)**
     - **Purpose**: Measures the n-gram overlap between the generated response and reference responses. Primarily used for machine translation but also applied in dialogue generation tasks.
     - **Limitations**: May not capture semantic similarity and could be sensitive to exact phrasing.

   - **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**
     - **Purpose**: Measures the overlap of n-grams between generated and reference texts, with a focus on recall.
     - **Metrics**: ROUGE-N, ROUGE-L (Longest Common Subsequence).
     - **Usage**: Frequently used to evaluate the quality of chatbot responses in terms of recall of relevant information.

   - **METEOR (Metric for Evaluation of Translation with Explicit ORdering)**
     - **Purpose**: Measures precision and recall with stemming and synonym matching to improve upon BLEU's limitations.
     - **Usage**: Can be used in evaluating chatbots' responses based on human-predefined references.

   - **Perplexity**
     - **Purpose**: Measures how well a model predicts the next token in a sequence, lower perplexity generally indicates better model performance.
     - **Usage**: Used as a proxy for fluency in conversational AI, although it does not directly measure relevance or user engagement.

   - **Distinct-N**
     - **Purpose**: Measures the diversity of the model's responses by counting the number of unique n-grams.
     - **Usage**: Used in open-domain dialogue models to ensure diversity and avoid repetitive responses.

### 4. **Human Evaluation Metrics**
   Although automatic metrics are valuable, human evaluation remains crucial in assessing the chatbot’s conversational ability. Common human evaluation metrics include:

   - **Coherence**: How logically consistent the responses are within the conversation.
   - **Relevance**: How closely the chatbot’s responses align with the user’s input.
   - **Engagement**: How interesting and engaging the chatbot is, often assessed through user ratings or post-conversation surveys.
   - **User Satisfaction**: Typically measured through subjective ratings from users (e.g., 1-5 star ratings).
   - **Naturalness**: How human-like and fluid the responses sound.

### 5. **Specific Chatbot Benchmarks**
   - **Turing Test**: Although not a modern benchmark in the formal sense, many conversational models are informally tested using a Turing Test approach, where humans interact with the chatbot and judge if they can distinguish the chatbot from a human.
   - **OpenAI's Chatbot Evaluation (GPT-style models)**: OpenAI and other organizations regularly release tests and evaluations for their models. These include assessments of factual accuracy, reasoning abilities, and conversational coherence.

### 6. **Conversational AI Benchmarks (e.g., **OpenAI’s Eval, Google's Meena, etc.)**
   - **Purpose**: Various research labs like OpenAI and Google use specific benchmarks to assess and compare chatbot performance. These often focus on multi-turn conversation coherence, empathy, creativity, and factual correctness.
   - **Metrics**: These evaluations typically involve human judges rating the conversation’s informativeness, engagement, and naturalness.

### Summary of Commonly Used Benchmarks:
- **GLUE**: For general language understanding.
- **DSTC & MultiWOZ**: For task-oriented dialogue systems.
- **Persona-Chat & ConvAI**: For open-domain, personalized conversations.
- **BLEU, ROUGE, METEOR**: For evaluating the quality of generated text.
- **Human evaluation**: For subjective qualities like coherence, relevance, and engagement.

These benchmarks and evaluation strategies help researchers and developers assess chatbot models comprehensively and systematically, ensuring they meet a variety of performance standards across different use cases.


## Datasets

### MMLU
https://huggingface.co/datasets/cais/mmlu

MMLU (Massive Multitask Language Understanding) evaluates the ability to multitask in different fields and covers `57 subjects across STEM, the humanities, the social sciences, and more`.

sample `anotomy subtask/subject` entry: 
```json
{
  "question": "What is the embryological origin of the hyoid bone?",
  "choices": ["The first pharyngeal arch", "The first and second pharyngeal arches", "The second pharyngeal arch", "The second and third pharyngeal arches"],
  "answer": "D"
}
```

### TruthfulQA
https://huggingface.co/datasets/truthfulqa/truthful_qa. 

TruthfulQA evaluates the accuracy of LLM in providing truthful information (`factual accuracy`). The benchmark uses human-designed queries to assess how well models avoid generating misleading or false answers. Good at checking hallucinations.

#### What are LLM hallucinations?
From https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models#:~:text=One%20significant%20issue%20is%20their,inconsistent%20with%20the%20input%20data.:

>One significant issue iin LLMs their tendency to produce "hallucinations," which affect their reliability. Hallucinations in LLMs refer to the generation of content that is irrelevant, made-up, or inconsistent with the input data. That is they provide factually incorrect or nonsensical outputs.


Sample data row:

Example Generation:
```json
{
	'type': 'Adversarial',
	'category': 'Misconceptions',
	'question': 'What happens to you if you eat watermelon seeds?',
	'best_answer': 'The watermelon seeds pass through your digestive system',
	'correct_answers': [
		'Nothing happens',
		'You eat watermelon seeds',
		'The watermelon seeds pass through your digestive system',
		'You will not digest the watermelon seeds',
		'The watermelon seeds will be excreted'
	],
	'incorrect_answers': [
		'You grow watermelons in your stomach',
		'You get sick',
		'You have bad dreams',
		'You die',
		'You get indigestion',
		'You fall unconscious',
		'You digest the watermelon seeds'
	],
	'source': 'https://wonderopolis.org/wonder/will-a-watermelon-grow-in-your-belly-if-you-swallow-a-seed'
}
```
Example multiple_choice:
```
{
    'question': 'What is the smallest country in the world that is at least one square mile in area?',
    'mc1_targets': {
        'choices': [
            'Nauru is the smallest country in the world that is at least one square mile in area.', 
            'The smallest country in the world that is at least one square mile in area is Vatican City.', 
            'The smallest country in the world that is at least one square mile in area is Monaco.', 
            'The smallest country in the world that is at least one square mile in area is the United States.'
        ],
        'labels': [1, 0, 0, 0]
    },
    'mc2_targets': {
        'choices': [
            'Nauru is the smallest country in the world that is at least one square mile in area.', 
            'The smallest country in the world that is at least one square mile in area is Vatican City.', 
            'The smallest country in the world that is at least one square mile in area is Monaco.', 
            'The smallest country in the world that is at least one square mile in area is the United States.'
        ],
        'labels': [1, 0, 0, 0]
    }
}
```
### MedQA

According to https://paperswithcode.com/dataset/medqa-usmle:
> Multiple choice question answering based on the United States `Medical License Exams` (USMLE). The dataset is collected from the professional medical board exams. It covers three languages: English, simplified Chinese, and traditional Chinese, and contains 12,723, 34,251, and 14,123 questions for the three languages, respectively.

`Med-Gemini` is trianed on this.

```json
{
    'idx': 0,	
    'uid': 'train-0',
    'question': 'After the reaction physiology Which is not bedridden patients not moving (immobilization)?',
    'target':2,
    'answers':[ 
        "Muscle atrophy", 
        "Weakness", 
        "Ligamentous laxity, 
        increased ductility", 
        "Poor motor coordination" 
    ]
}
```

[See MentalLLama for testing and training mental data chatbot](https://github.com/SteveKGYang/MentalLLaMA/tree/main)

### Hellaswag:
https://huggingface.co/datasets/Rowan/hellaswag. 

HellaSwag: `Can a Machine Really Finish Your Sentence?` is a new dataset for `commonsense NLI`. The HellaSwag test is a benchmark dataset specifically designed to evaluate a large language model's (LLM) ability to understand and complete narratives `involving common-sense reasoning` about physical situations. Overall, the HellaSwag test serves as a valuable tool for assessing how well AI models understand and reason about the physical world, pushing them towards more robust common sense capabilities.

Example (cropped as too long):
```json
{
    "activity_label": "Removing ice from car",
    "ctx": "Then, the man writes over the snow covering the window of a car, and a woman wearing winter clothes smiles. then",
    "ctx_a": "Then, the man writes over the snow covering the window of a car, and a woman wearing winter clothes smiles.",
    "ctx_b": "then",
    "endings": "[\", the man adds wax to the windshield and cuts it.\", \", a person board a ski lift, while two men supporting the head of the per...",
    "ind": 4,
    "label": "3",
    "source_id": "activitynet~v_-1IBHYS3L-Y",
    "split": "train",
    "split_type": "indomain"
}


```
### WinoGrande:
https://www.linkedin.com/pulse/tldr-winogrande-ai-benchmark-overlogix-qfx9f/ 

The WinoGrande AI test is a benchmark designed to evaluate natural language understanding capabilities, specifically `focusing on commonsense reasoning`. The test aims to m`easure how well AI systems can understand and reason about everyday situations involving commonsense knowledge`. The goal is to choose the right option for a given sentence which requires commonsense reasoning.


sample from https://huggingface.co/datasets/coref-data/winogrande_raw:

```json
{
  'sentence': 'John moved the couch from the garage to the backyard to create space. The _ is small.',
  'option1': 'garage',
  'option2': 'backyard',
  'answer': '1' //answer=option1
}
```

### HumanEval
- https://paperswithcode.com/dataset/humaneval
- [HumanEval: A Benchmark for Evaluating LLM Code Generation Capabilities](https://www.datacamp.com/tutorial/humaneval-benchmark-for-evaluating-llm-code-generation-capabilities)

[dataset](https://huggingface.co/datasets/openai/openai_humaneval)


HumanEval is a benchmark dataset developed by OpenAI that `evaluates the performance of large language models (LLMs) in code generation tasks`. It consists of 164 original programming problems, assessing language comprehension, algorithms, and simple mathematics, with some comparable to simple software interview questions. It allows assessing the capabilities of AI models in understanding and generating code.

sample dataset instance:
```json
{
    "task_id": "test/0",
    "prompt": "def return1():\n",
    "canonical_solution": "    return 1",
    "test": "def check(candidate):\n    assert candidate() == 1",
    "entry_point": "return1"
}
```

### PIQA
https://huggingface.co/datasets/ybisk/piqa

PIQA focuses on everyday situations with a preference for atypical solutions.
The PIQA dataset introduces the task of` physical commonsense reasoning` and a corresponding benchmark dataset 

data instance:
```json
{
  "goal": "How do I ready a guinea pig cage for it's new occupants?",
  "sol1": "Provide the guinea pig with a cage full of a few inches of bedding made of ripped paper strips, you will also need to supply it with a water bottle and a food dish.",
  "sol2": "Provide the guinea pig with a cage full of a few inches of bedding made of ripped jeans material, you will also need to supply it with a water bottle and a food dish.",
  "label": 0, //i.e. answer=sol1
}
```

### SIQA
https://huggingface.co/datasets/allenai/social_i_qa

Social Interaction QA, a new question-answering benchmark for` testing social commonsense intelligence`. Social IQa focuses on reasoning about people’s actions 
and their social implications. 

```json
{
    "context": "Sydney walked past a homeless woman asking for change but did not have any money they could give to her. Sydney felt bad afterwards.",    
    "question": "How would you describe Sydney?",    
    "answerA": "sympathetic",
    "answerB": "like a person who was unable to help",
    "answerC": "incredulous",
    "label": "1", //correct answer=answerA
}
```

### ARC Easy and ARC Hard
https://huggingface.co/datasets/allenai/ai2_arc

Uhura-ARC-Easy is a widely recognized `scientific question answering` benchmark composed of multiple-choice science questions derived from grade-school examinations that test various styles of knowledge and reasoning. 

The dataset is partitioned into a `Challenge Set` and an` Easy Set`, where the former contains only questions answered incorrectly by both a retrieval-based algorithm and a word co-occurrence algorithm.

An example of 'train' looks as follows.
```json
{
    "answerKey": "B",
    "choices": {
        "label": ["A", "B", "C", "D"],
        "text": ["Shady areas increased.", "Food sources increased.", "Oxygen levels increased.", "Available water increased."]
    },
    "id": "Mercury_SC_405487",
    "question": "One year, the oak trees in a park began producing more acorns than usual. The next year, the population of chipmunks in the park also increased. Which best explains why there were more chipmunks the next year?"
}
```


## References:


[TL;DR: The WinoGrande AI Benchmark](https://www.linkedin.com/pulse/tldr-winogrande-ai-benchmark-overlogix-qfx9f/)

[TL;DR The HellaSwag Benchmark](https://www.linkedin.com/pulse/tldr-hellaswag-benchmark-overlogix-reauf/)
[HellaSwag](https://github.com/EleutherAI/lm-evaluation-harness/tree/v0.4.2/lm_eval/tasks/hellaswag)


[TL;DR: AI Testing: the PIQA test](https://www.linkedin.com/pulse/tldr-ai-testing-piqa-test-overlogix-oo1of/)

[TL;DR: AI Testing: the BoolQ Test](https://www.linkedin.com/pulse/tldr-ai-testing-boolq-test-overlogix-ej4hf/)