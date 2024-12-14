# Eleuther AI  - Harness Evaluation
[Evaluate LLMs with Language Model Evaluation Harness : AI Anytime](https://www.youtube.com/watch?v=p-gzfS1JgEE)

[notebook I followed](https://github.com/AIAnytime/Eval-LLMs/blob/main/LLM_Eval.ipynb)


Other references:
- [Evaluating Language Models with the LM Evaluation Harness: Linkedin](https://www.linkedin.com/pulse/evaluating-language-models-lm-evaluation-harness-gabriele-monti-tmgtf/)
- [Evaluating Large Language Models (LLMs) with Eleuther AI: wandb.ai](https://wandb.ai/wandb_gen/llm-evaluation/reports/Evaluating-Large-Language-Models-LLMs-with-Eleuther-AI--VmlldzoyOTI0MDQ3)
- [LLM evaluation | EleutherAI lm-evaluation-harness : medium](https://medium.com/disassembly/llm-evaluation-eleutherai-lm-evaluation-harness-cc379495d545)


## Open notebook
Open the Github notebook that you want to work with in Google Colab. Change the domain from '`github.com`' to '`githubtocolab.com`'. The notebook will open in Colab.(or add https://colab.research.google.com/github/ before the repository name in the notebook's URL. i.e. https://colab.research.google.com/github/AIAnytime/Eval-LLMs/blob/main/LLM_Eval.ipynb) > File > Save a copy to drive

## Change runtime environment
`Connect to colab notebook runtime:` Python3, T4 GPU

## My changes to notebook
I used my own fine tuned model `dmrhimali/falcon7binstruct_mentalhealthmodel_oct23` to evaluate


## Evaluation:

## Providers/Backends:
Lm-evaluation-harness supports many providers/backends:
* hf (hf-auto) (huggingface) 
* openai-completions 
* local-completions 
* openai-chat-completions 
* local-chat-completions 
* anthropic 
* gguf (ggml) 
* vllm 
etc.

#### Usage:

```sh
python -m lm_eval \ 
--model hf \  #uses huggingface provider
....
```

## Select Task:
the config task is the major way to select the pre-config evaluation task which decides the dataset, group, types of measurements , post-process setting, etc

#### Usage:

```sh
python -m lm_eval \ 
    --tasks mmlu_flan_n_shot_generative \ 
    ...
```

## Select Dataset:
lm-evaluation-harness/lm_eval/tasks lists all currently supported datasets.
Here are a few data sets commonly used by open_llm_leaderboard:
-MMLU
-Hellaswag
-TruthfulQA

List the tasks to see more

Ref: 
- [blog: LLM evaluation | EleutherAI lm-evaluation-harness](https://medium.com/disassembly/llm-evaluation-eleutherai-lm-evaluation-harness-cc379495d545)