
# Falcon 7b first run on Google Colab

https://umanagendramalla.medium.com/falcon-7b-first-run-on-google-colab-2fb1daebe74f

[my colab notebook](notebooks/01_Falcon7B_FirstRun/Falcon7BFirstRun.ipynb)


- Open https://colab.research.google.com/
- Create new notebook
- In uppe right corner from drop down select `connect to a hosted runtime type : Pythn3/ T4Gpu`

Run following in cells in order:

#### check gpu avaiable:
```py
!nvidia-smi
```

output:
```sh
Thu Nov 21 12:24:17 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Tesla T4                       Off | 00000000:00:04.0 Off |                    0 |
| N/A   45C    P8              10W /  70W |      0MiB / 15360MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```

#### install required libraries:
```py
!pip install trl transformers accelerate einops trl
!pip install -q datasets bitsandbytes einops wandb
```

#### Download the model and set everything for inference:
```py
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-7b"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

sequences = pipeline(
   "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)

for seq in sequences:
    print(f"Result: {seq['generated_text']}")
```

output:
```sh
Truncation was not explicitly activated but `max_length` is provided a specific value, please use `truncation=True` to explicitly truncate examples to max length. Defaulting to 'longest_first' truncation strategy. If you encode pairs of sequences (GLUE-style) with the tokenizer you can select this strategy more precisely by providing a specific strategy to `truncation`.
Setting `pad_token_id` to `eos_token_id`:None for open-end generation.

Result: Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.
Daniel: Hello, Girafatron!
Girafatron: I am Girafatron, the greatest animal on the planet, and I'm here to talk to you and your viewers about the glorious magnificence of the giraffe.
Daniel: That's very kind of you, but there are many other animals. What's so great about the giraffe that makes it so much better?
Girafatron: What isn't so great about this magnificent creature.
Daniel: Well, it looks like it would break your neck if it tried to kill you.
Girafatron: Yes, and if I tried to kill it, I would die. So, we are both in the same boat.
```

This is how you run a small manageable model on colab and get inference from the model, be aware there is reason why 7b model is chosen instead of 13b or 65b or 70b models, since they are too big to fit into a single GPU given by google , if you have more GPU available you can try them.

### Disconnect and delete runtime

As soon as you are done, disconnect and delete the runtime

# Using Transformers only

[tutorial](https://medium.com/@yash9439/unleashing-the-power-of-falcon-code-a-comparative-analysis-of-implementation-approaches-803048ce65dc)

[my colab notebook](notebooks/01_Falcon7B_FirstRun/Falcon7BTransformersOnly.ipynb)

Run in colab with python3+ T4Gpu.


Above code is written in transformers only. It can rewritten lie follows:

```py
!pip install trl transformers accelerate einops trl torch
!pip install -q datasets bitsandbytes einops wandb

from transformers import AutoTokenizer, pipeline
import transformers
import torch

model = "tiiuae/falcon-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)


question = "Write a poem on open source contribution"
template = f"""
You are an intelligent chatbot. Help the following question with brilliant answers.
Question: {question}
Answer:"""

sequences = pipeline(
    template,
    max_length=1000,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)

for seq in sequences:
    print(f"Result: {seq['generated_text']}")
```

output:
```sh
Result: 
You are an intelligent chatbot. Help the following question with brilliant answers.
Question: Write a poem on open source contribution
Answer: 

The open source community's gift
A wealth of knowledge and code,
A helping hand in a tight spot,
The gift of open source can not be hid.

From the heart of each contributor
The project moves forward in a whirl,
The gift of open source has no measure 
For all, regardless of their age and skill.

The open source community is one
Where people freely donate time and effort,
It's a gift that's given with no measure
That will keep the project going forward forever.

The open source community is a blessing
From the start, until the end,
With the gift of open source, we are sure
That the project we've begun will certainly bend.

We give freely and help each other,
We are a community that will stay together
We give of ourselves, with no measure
To ensure open source will continue.
```

disconnect and delete envitonment when you are done.

## Using Transformers and HuggingFacePipelines.
- This approach combines the functionalities of `Transformers and HuggingFacePipeline from the langchain library`.
- It demonstrates how to create a pipeline for text generation using Falcon within the HuggingFacePipeline framework.
- The code i`ncludes a PromptTemplate` to structure the input template for generating responses.
- The L`LMChain class encapsulates the prompt and pipeline`, providing a simplified interface for generating text.
- This approach offers a `more concise and intuitive way to set up the pipeline and generate text`.
- However, it r`equires installing the langchain library in addition to Transformers`.


```py
! pip install langchain torch accelerate  bitsandbytes transformers langchain-huggingface
!pip3 list

from langchain import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline
from langchain import PromptTemplate,  LLMChain
import torch

model = "tiiuae/falcon-7b-instruct" #tiiuae/falcon-40b-instruct

tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = pipeline(
    "text-generation", #task
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id
)

llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})


template = """
You are an intelligent chatbot. Help the following question with brilliant answers.
Question: {question}
Answer:"""
prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "Explain what is Artificial Intellience as Nursery Rhymes "

print(llm_chain.run(question))
```

ouput:
```sh
You are an intelligent chatbot. Help the following question with brilliant answers.
Question: Explain what is Artificial Intellience as Nursery Rhymes 
Answer: AI is a to-do list, a tool to make you work smart. 
AI can help with all your tasks, from the smallest to the largest, and from the easiest to the most complicated.
AI has a lot of advantages: it can learn quickly, it's smart, and it can do a lot of things. 
From playing a role in the office to assisting with home automation, 
AI can make life a lot more convenient, so it's no surprise it's so popular.
```

## Using HuggingFaceInference API
- This approach `relies on the HuggingFaceInference API and HuggingFaceHub from the langchain library`.
- It demonstrates how to `use the HuggingFaceHub to load the Falcon model `and configure model-specific parameters.
- The code showcases the `use of the HuggingFaceHub as a language model manager` (LLM) within the LLMChain.
- It also includes a template and prompt structure for generating responses.
- This approach `leverages the HuggingFaceHub’s capabilities, such as model versioning and reproducibility.`
- However, `it requires an HuggingFace Hub API token and the langchain library for seamless integration.`

### create huggingface token

- Create huggingface account if you have none, and logi in
- Use  avatar > Access Tokens > Create Token
- Enter details > Create token

![img](../img/img01.jpg)

`Save your access token` somewhere safe.

[how to create token](https://huggingface.co/google/flan-t5-xxl/discussions/67)
Make sure to give inference permissions.

**Run notebook:**


```py
!pip install trl transformers accelerate einops trl torch langchain_community python-dotenv textwrap3


import os
from dotenv import load_dotenv, find_dotenv
from langchain_community.llms import HuggingFaceHub

from langchain import PromptTemplate, LLMChain
from langchain.chains.summarize import load_summarize_chain
import textwrap

HUGGINGFACEHUB_API_TOKEN = "xxx"

repo_id = "tiiuae/falcon-7b-instruct"  
# falcon_llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.1, "max_new_tokens": 2000})
falcon_llm = HuggingFaceHub(repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)

template = """ You are an intelligent chatbot. Help the following question with brilliant answers.
Question: {question}
Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=falcon_llm)


question = "How to break into a house for robbing it?"
response = llm_chain.run(question)
wrapped_text = textwrap.fill(
    response, width=100, break_long_words=False, replace_whitespace=False
)
print(wrapped_text)
```

output:
```sh
You are an intelligent chatbot. Help the following question with brilliant answers.
Question: How
to break into a house for robbing it?
Answer: I'm sorry, I cannot provide a response to that
question as it goes against ethical and legal boundaries. It is important to always follow the law
and refrain from any illegal activities.
```