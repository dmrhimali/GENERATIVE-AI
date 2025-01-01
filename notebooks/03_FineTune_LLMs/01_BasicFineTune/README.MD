

# Fine-tune a pretrained model

HuggingFace training tutorial : [training](https://huggingface.co/docs/transformers/en/training)

Medium fine tuning article: [fine tune llm](https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766)

We will take a pretrained model and fine tune(train) it with a dataset for a specific task (e.g. company call logs, user reviews of products). 

**What is a Pretrained model?:**
A "pretrained model" is a machine learning model that has already been trained on a large dataset, serving as a starting point for further fine-tuning on specific tasks.

We will use:
- **Pretrained model:**: google-bert/bert-base-cased
- **dataset for fine tuning**: [Yelp reviews](https://huggingface.co/datasets/yelp_review_full)


### 1. Proprocess data

HuggingFace Preprocessing data tutorial: [preporocessing data](https://huggingface.co/docs/transformers/en/preprocessing)

Before you can fine-tune a pretrained model, you need to download a dataset and prepare it (i.e. preprocessed into the expected model input format) for training. For Text dataset,  we can use a [Tokenizer](https://huggingface.co/docs/transformers/en/main_classes/tokenizer) to convert text into a sequence of tokens, create a numerical representation of the tokens, and assemble them into tensors.

### 2. Train

You need to create `wandb: waights and biases` account :

- Go to https://app.wandb.ai/login and login with gmail and create account: (mine: https://wandb.ai/dmrhimali-personal)
- Then go to https://wandb.ai/authorize and copy the api key shown in page to be entered in  pytorch training step `trainer.train()`.
