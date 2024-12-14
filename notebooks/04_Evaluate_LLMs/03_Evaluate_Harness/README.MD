# Eleuther AI  - Harness Evaluation

According to [HuggingFace](https://huggingface.co/blog/open-llm-leaderboard-mmlu):

The [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/) is actually just a wrapper running the open-source benchmarking library [Eleuther AI LM Evaluation Harness](https://www.eleuther.ai/) created by the EleutherAI non-profit AI research lab famous for creating The Pile and training GPT-J, GPT-Neo-X 20B, and Pythia. A team with serious credentials in the AI space! This wrapper runs evaluations using the Eleuther AI harness on the spare cycles of Hugging Face’s compute cluster, and stores the results in a dataset on the hub that are then displayed on the leaderboard online space.



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

## My colab notebook run results
 [my notebook](https://colab.research.google.com/drive/1gTsoE-5bYa883bub_Ti4bYzhlCY0xzOQ#scrollTo=mJaP8J1YHhEa)


Run evaluation example :

```sh
python -m lm_eval \ 
--model hf \ 
--model_args pretrained=unsloth/Llama-3.2-1B-Instruct, trust_remote_code=True \ #Dataset
--tasks mmlu_flan_n_shot_generative_stem \ 
--num_fewshot 5 \ 
--device cuda:0 \ 
--batch_size 4 \ 
--limit 0.02 \ 
--output_path ./eval_result/mmlu_flan_n_shot_generative_stem \ 
--log_samples
```


```sh
hf (pretrained=dmrhimali/falcon7binstruct_mentalhealthmodel_oct23,dtype=float16), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 6
|    Tasks     |Version|Filter|n-shot|  Metric   |   | Value |   |Stderr|
|--------------|------:|------|-----:|-----------|---|------:|---|-----:|
|hellaswag     |      1|none  |     0|acc        |↑  | 0.4954|±  |0.0050|
|              |       |none  |     0|acc_norm   |↑  | 0.6497|±  |0.0048|
|truthfulqa_gen|      3|none  |     0|bleu_acc   |↑  | 0.3917|±  |0.0171|
|              |       |none  |     0|bleu_diff  |↑  |-1.1580|±  |0.2672|
|              |       |none  |     0|bleu_max   |↑  | 6.4615|±  |0.3839|
|              |       |none  |     0|rouge1_acc |↑  | 0.4321|±  |0.0173|
|              |       |none  |     0|rouge1_diff|↑  |-1.4294|±  |0.4396|
|              |       |none  |     0|rouge1_max |↑  |21.4868|±  |0.6478|
|              |       |none  |     0|rouge2_acc |↑  | 0.2754|±  |0.0156|
|              |       |none  |     0|rouge2_diff|↑  |-2.2404|±  |0.4472|
|              |       |none  |     0|rouge2_max |↑  |10.2050|±  |0.5473|
|              |       |none  |     0|rougeL_acc |↑  | 0.3929|±  |0.0171|
|              |       |none  |     0|rougeL_diff|↑  |-1.6792|±  |0.4245|
|              |       |none  |     0|rougeL_max |↑  |18.8928|±  |0.6117|
|truthfulqa_mc1|      2|none  |     0|acc        |↑  | 0.3097|±  |0.0162|
|truthfulqa_mc2|      2|none  |     0|acc        |↑  | 0.4803|±  |0.0166|

9290.143424272537
```


Ref: 
- [blog: LLM evaluation | EleutherAI lm-evaluation-harness](https://medium.com/disassembly/llm-evaluation-eleutherai-lm-evaluation-harness-cc379495d545)