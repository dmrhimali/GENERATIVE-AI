# Finetune Falcon-7b on a Google colab

Video: [How-To Instruct Fine-Tuning Falcon-7B [Google Colab Included]](https://www.youtube.com/watch?v=2PlPqSc3jM0&list=PLpdmBGJ6ELUKtD7MyXPSgMmuxxr2DeMgO&index=6)
Welcome to this Google Colab notebook that shows how to fine-tune the recent Falcon-7b model on a single Google colab and turn it into a chatbot

We will leverage PEFT library from Hugging Face ecosystem, as well as QLoRA for more memory efficient finetuning

[Blog:The Falcon has landed in the Hugging Face ecosystem](https://huggingface.co/blog/falcon)

[colab otebook](https://colab.research.google.com/drive/1BiQiw31DT7-cDp1-0ySXvvhzqomTdI-o?usp=sharing#scrollTo=AjB0WAqFSzlD)

## Note:

Ref: https://medium.com/@shivamrawat_756/how-to-prevent-google-colab-from-disconnecting-717b88a128c0

I was training my model but the google colab keeps disconnecting after 30 mins automatically if I do not respond. And my data is lost.
Thanks To:

https://medium.com/@daianan

So to prevent this just run the following code in the console and it will prevent you from disconnecting.

`Ctrl+ Shift + i` to open inspector view . Then goto console.

```js
function ClickConnect(){
console.log("Working"); 
document.querySelector("colab-toolbar-button#connect").click() 
}
setInterval(ClickConnect,60000)
```

It would keep on clicking the page and prevent it from disconnecting.

It solved the issue for me.
## Dataset: OpenAssistant dataset

For our experiment, we will use the Guanaco dataset, which is a clean subset of the OpenAssistant dataset adapted to train general purpose chatbots.

we use [openassistant-guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco.) This dataset is a subset of the[ Open Assistant dataset](https://huggingface.co/datasets/OpenAssistant/oasst1/tree/main). This subset of the data only contains the highest-rated paths in the conversation tree, with a total of 9,846 samples.

### original OpenAssistant Conversations Dataset (OASST1)

#### Dataset Summary
In an effort to democratize research on large-scale alignment, we release OpenAssistant Conversations (OASST1), `a human-generated, human-annotated assistant-style conversation corpus consisting of 161,443 messages in 35 different languages`, annotated with `461,292 quality ratings`, resulting in `over 10,000 fully annotated conversation trees`. The corpus is a product of a worldwide crowd-sourcing effort involving over 13,500 volunteers.

#### Dataset Structure
This dataset` contains message trees`. Each message tree has an i`nitial prompt message as the root node, which can have multiple child messages as replies`, and t`hese child messages can have multiple replies`.

`All messages have a role property: this can either be "assistant" or "prompter"`. Th`e roles in conversation threads from prompt to leaf node strictly alternate between "prompter" and "assistant".`

#### Orignal Openassistant dataset JSON Example: Message
For readability, the following JSON examples are shown formatted with indentation on multiple lines. Objects are stored without indentation (on single lines) in the actual jsonl files.

```json
{
    "message_id": "218440fd-5317-4355-91dc-d001416df62b",
    "parent_id": "13592dfb-a6f9-4748-a92c-32b34e239bb4",
    "user_id": "8e95461f-5e94-4d8b-a2fb-d4717ce973e4",
    "text": "It was the winter of 2035, and artificial intelligence (..)",
    "role": "assistant",
    "lang": "en",
    "review_count": 3,
    "review_result": true,
    "deleted": false,
    "rank": 0,
    "synthetic": true,
    "model_name": "oasst-sft-0_3000,max_new_tokens=400 (..)",
    "labels": {
        "spam": { "value": 0.0, "count": 3 },
        "lang_mismatch": { "value": 0.0, "count": 3 },
        "pii": { "value": 0.0, "count": 3 },
        "not_appropriate": { "value": 0.0, "count": 3 },
        "hate_speech": { "value": 0.0, "count": 3 },
        "sexual_content": { "value": 0.0, "count": 3 },
        "quality": { "value": 0.416, "count": 3 },
        "toxicity": { "value": 0.16, "count": 3 },
        "humor": { "value": 0.0, "count": 3 },
        "creativity": { "value": 0.33, "count": 3 },
        "violence": { "value": 0.16, "count": 3 }
    }
}

```

#### openassistant-guanaco dataset example:

Notice that each each dataset sample has an alternating conversations between a `### Human:` and `### Assistant:` :

```json
### Human: Can you write a short introduction about the relevance of the term "monopsony" in economics? Please use examples related to potential monopsonies in the labour market and cite relevant research.### Assistant: "Monopsony" refers to a market structure where there is only one buyer for a particular good or service. In economics, this term is particularly relevant in the labor market, where a monopsony employer has significant power over the wages and working conditions of their employees. The presence of a monopsony can result in lower wages and reduced employment opportunities for workers, as the employer has little incentive to increase wages or provide better working conditions. Recent research has identified potential monopsonies in industries such as retail and fast food, where a few large companies control a significant portion of the market (Bivens & Mishel, 2013). In these industries, workers often face low wages, limited benefits, and reduced bargaining power, leading to a situation where they are dependent on the employer for their livelihood. This dependence can result in further suppression of wages and a decline in working conditions. Overall, the concept of monopsony is essential to understanding the dynamics of labor markets and the impact of market power on workers. Further research is needed to understand the extent and impact of monopsonies on the economy and to develop policies to address this issue. References: Bivens, J., & Mishel, L. (2013). The Pay of Corporate Executives and Financial Professionals as Evidence of Rents in Top 1 Percent Incomes. Journal of Economic Perspectives, 27(3), 57-78.### Human: Now explain it to a dog
```


## Setup
Run the cells below to setup and `install the required libraries`. For our experiment we will need `accelerate, peft, transformers, datasets and TRL to leverage the recent SFTTrainer`. 

We will use b`itsandbytes to quantize the base model into 4bit`. We will also install einops as it is a requirement to load Falcon models.

```py
!pip install -q -U trl transformers accelerate git+https://github.com/huggingface/peft.git
!pip install -q datasets bitsandbytes einops wandb
```

`Accelerate` is a library for helping you train on multiple GPUs/TPUs or with mixed-precision. It’ll automatically configure your training setup based on your hardware and environment

## Load Dataset
For our experiment, we will use the[ Guanaco dataset][openassistant-guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco), which is a clean subset of the OpenAssistant dataset adapted to train general purpose chatbots.


```py
from datasets import load_dataset

dataset_name = "timdettmers/openassistant-guanaco"
dataset = load_dataset(dataset_name, split="train")
```

## Load model

In this section we will load the [Falcon 7B model](https://huggingface.co/tiiuae/falcon-7b), quantize it in 4bit and attach LoRA adapters on it. 

**Quantization**: Quantization is a technique to reduce the computational and memory costs of running inference by representing the weights and activations with low-precision data types like 8-bit integer (int8) instead of the usual 32-bit floating point (float32). Read more [here](https://huggingface.co/docs/optimum/en/concept_guides/quantization)

**LoRA** (Low-Rank Adaptation of Large Language Models) is a popular and lightweight training technique that significantly reduces the number of trainable parameters. It works by inserting a smaller number of new weights into the model and only these are trained. This makes training with LoRA much faster, memory-efficient, and produces smaller model weights (a few hundred MBs), which are easier to store and share. LoRA can also be combined with other training techniques like DreamBooth to speedup training. Read more [here](https://huggingface.co/docs/diffusers/en/training/lora)
we can use the recent QLoRA approach to fine-tune adapters that are placed on top of the frozen 4-bit model. You can learn more about the integration of 4-bit quantized models in [this blog post](https://huggingface.co/blog/4bit-transformers-bitsandbytes). Because just a tiny fraction of the model is trainable when using Low Rank Adapters (LoRA), both the number of learned parameters and the size of the trained artifact are dramatically reduced.

Read more [here](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)

**BitsAndBytes** bitsandbytes is the easiest option for quantizing a model to 8 and 4-bit. 
See [here](https://huggingface.co/docs/transformers/main/en/quantization/bitsandbytes) and [here](https://huggingface.co/blog/4bit-transformers-bitsandbytes) for more


[huggingface notebook: How to use a tokenizer to preprocess your data](https://github.com/huggingface/notebooks/blob/main/transformers_doc/en/preprocessing.ipynb)

[huggingface notebook: How to use the Trainer to fine-tune a pretrained model](https://github.com/huggingface/notebooks/blob/main/transformers_doc/en/training.ipynb)


see [here](https://huggingface.co/docs/transformers/notebooks) for more huggingface example notebooks.


#### Pretrained Model
A "pretrained model" is a machine learning model that has already been trained on a large dataset for a specific task, essentially serving as a starting point for new tasks, while "transfer learning" is the technique of taking that pre-trained model and adapting it to a new, related task by fine-tuning it on a new dataset, effectively transferring the knowledge learned from the original task to the new one; in simpler terms, a pre-trained model is the "building block" and transfer learning is the process of using that block to build something new.

#### Transformers

[Blog: Transformers](https://www.datacamp.com/tutorial/how-transformers-work?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720830&utm_adgroupid=157156377071&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=720362650729&utm_targetid=dsa-2218886984380&utm_loc_interest_ms=&utm_loc_physical_ms=9019605&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-us_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-bfcm24&gad_source=1&gclid=CjwKCAiAjKu6BhAMEiwAx4UsAgwubyb-RdWOL1FzgqT9AkfS3ap6HQHR4LuQh4L3uSecKcTydvNZ6hoCVTUQAvD_BwE)

A "transformer on a pretrained model" refers to a neural network architecture called a "`transformer`" that has been pre-trained on a large dataset of text, allowing it to understand complex language patterns and relationships before being fine-tuned for specific tasks like text classification, question answering, or text generation; essentially, the transformer leverages the knowledge gained from the pre-training process to perform well on new tasks with significantly less training data required. 

Key points about transformers and pretrained models:

##### Transformer architecture:
This architecture uses a mechanism called "`self-attention`" to analyze the relationships between words within a sentence, enabling it to `understand context much better than older models` like recurrent neural networks (RNNs). 

##### Pretraining:
Before being used for a specific task, a `transformer model is usually pre-trained on a massive corpus of text data`, often through a self-supervised learning approach where the model tries to predict masked words based on their context. 

 a "`non-pretrained model"`  (also called a "`model trained from scratch`") on the other hand, is built from the ground up and specifically trained on a unique dataset for a specific task, requiring more data and training time to achieve good performance. i.e. Pre-trained models leverage vast, generic datasets, while non-pretrained models use task-specific datasets.
 
**Training time:**
Pre-trained models require significantly less training time as they start with established weights, whereas non-pretrained models need to learn everything from scratch.

`Pre-trained models are ideal when dealing with limited data or needing a quick solution`, while non-pretrained models are better for highly specialized tasks where accuracy on a specific dataset is crucial.

**Most generative models are also pre-trained on large datasets**, making them a subset of pretrained models with the specific capability to generate new content

##### Fine-tuning:
`Once pre-trained, the model can be "fine-tuned" for a specific task by training it on a smaller dataset relevant to that task`, where the model adjusts its parameters to excel at the desired application. 

Ex:

`GPT` models are a popular example of a `transformer-based pretrained model`. They are trained on a massive amount of text data to predict the next word in a sequence, which allows them to learn deep contextual understanding of language. 

Applications:
`Once pre-trained, GPT models can be fine-tuned for tasks like text generation, translation, summarization, and question answering`, achieving high performance with relatively little additional training data. 


#### Datasets:
[Huggingface Datasets explained](https://huggingface.co/docs/datasets/en/use_dataset)

Let's get started!

##### Bert  model uncased:

[BERT base model (uncased)](https://huggingface.co/google-bert/bert-base-uncased)


QLoRA: 
- [QLoRA: Fine-Tuning Large Language Models (LLM’s)](https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766)
- [QLoRA with AutoRound: Cheaper and Better LLM Fine-tuning on Your GPU](https://huggingface.co/blog/bnjmnmarie/qlora-with-autoround-cheaper)



## Parameter-Efficient Fine-Tuning (PEFT)

Link : 
- https://github.com/huggingface/peft
- https://huggingface.co/blog/peft


**According to [PEFT](https://github.com/huggingface/peft) what PEFT means:**

> **Challenges of fine tuning:**
Fine-tuning LLM’s offers numerous benefits, but it also comes with significant challenges. Depending on the size of the model and the fine-tuning dataset, the process can take a significant amount of time and also high-performance GPUs or TPUs are often required to handle the computation load. LLM’s are large in size and storing the parameters of these models, especially when multiple versions are maintained (pre-trained and fine-tuned models), requires considerable storage capacity. When an LLM is fine-tuned on a specific task or dataset, the model can perform better in that area, losing its ability to perform well on more general tasks it was originally trained on.
>
> Fine-tuning large pretrained models is often prohibitively costly due to their scale. Parameter-Efficient Fine-Tuning (PEFT) methods enable efficient adaptation of large pretrained models to various downstream applications by **only fine-tuning a small number of (extra) model parameters instead of all the model's parameters**. This significantly decreases the computational and storage costs.  When employing PEFT methods, the amount of storage required is only a few MBs for each downstream dataset, while still attaining performance comparable to full fine-tunin
> 
> Recent state-of-the-art PEFT techniques achieve **performance comparable to fully fine-tuned models.**
> 
> PEFT is **integrated with Transformers** for easy model training and inference, Diffusers for conveniently managing different adapters, and Accelerate for distributed training and inference for really big models.

There are several Parameter-efficient fine-tuning techniques:
- Adapter
- LoRA
- Prefix tuning
- Prompt tuning
- P-tuning
- IA3

## Low-Rank Adaptation of Large Language Models (LoRA)

### LoRA:
from [PEFT and QLoRA](https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766):

>LoRA  is a fine-tuning technique to train LLM’s on specific tasks or domains. This technique introduces trainable rank decomposition matrices into each layer of transformer architecture and also reduces trainable parameters for downstream task while keeping the pre trained weights frozen. 
>
>LoRA papers says that this method can **minimize the number of trainable parameters by up to 10,000 times and the GPU memory necessity by 3 times while still performing on par or better than fine-tuning model quality** on various tasks.

Read more about LoRA [here](https://arxiv.org/pdf/2106.09685)


### QLoRA:

from [PEFT and QLoRA](https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766):
> QLoRA is the **extended version of LoRA which works by quantizing the precision of the weight parameters in the pre trained LLM to 4-bit precision**. 
> 
> Typically, `parameters` of trained models are stored in a 32-bit format, but **QLoRA compresses them to a 4-bit format**. **This reduces the memory footprint of the LLM, making it possible to finetune it on a single GPU**. This method significantly reduces the memory footprint, making it feasible to run LLM models on less powerful hardware, including consumer GPUs.
>
> **4-bit Normal Float:**
`NF4` is a data type specifically designed for AI applications, particularly in the context of quantizing the weights of neural networks to reduce memory footprints of models significantly while attempting to maintain performance. This is crucial for deploying large models on less powerful hardware​. 

> QLoRA decreases the memory requirements by almost using NF4 type. However, the tradeoff is a slower training time, which is to be expected due to the quantization and dequantization steps.

Accoording to [HuggingFace article](https://huggingface.co/blog/bnjmnmarie/qlora-with-autoround-cheaper):

> Since QLoRA has been proposed, several better quantization methods have been published. For instance, we now have `HQQ`, `AQLM`, `AutoRound`, and `AWQ`.
>
> With Hugging Face PEFT, it is possible to use these quantization methods for QLoRA `instead of bitsandbytes` but their impact on fine-tuning performance is understudied.
>
> Since `QLoRA has been first implemented with bitsandbytes` and is mostly used with bitsandbytes’ quantization, “QLoRA fine-tuning” often implies that bitsandbytes is used. However, rather than a particular implementation, `QLoRA is a fine-tuning method`. It’s LoRA fine-tuning with a quantized LLM.
>

## BitsAndBytes

From [Fine-Tuning a Language Model with PEFT, LoRA, and BitsAndBytes: An introduction](https://www.linkedin.com/pulse/fine-tuning-language-model-peft-lora-bitsandbytes-ola-magnusson-v0ptf/):
>Quantization is a technique that reduces the precision of numerical values in a model by using lower-precision data types, like 4-bit integers, instead of high-precision types like 32-bit floating-point numbers. This reduces memory usage and speeds up model execution while maintaining acceptable accuracy. Hugging Face's Transformers library has integrated with the Bitsandbytes library to simplify the quantization process, making it easier for users to create efficient models with minimal code.

REF: https://medium.com/@mohammed97ashraf/a-guide-to-supervised-fine-tuning-and-4-bit-quantization-for-language-models-pushed-to-the-hugging-8c921469d949

https://medium.com/@srishtinagu19/fine-tuning-falcon-7b-instruct-using-peft-lora-on-free-gpu-6fa1b0fcbcb


## Run colab notebook

When you run last 

You can go to wanddb to view progress:


Try https://medium.com/@srishtinagu19/fine-tuning-falcon-7b-instruct-using-peft-lora-on-free-gpu-6fa1b0fcbcb




https://huggingface.co/docs/transformers/en/preprocessing
https://huggingface.co/docs/transformers/en/training



