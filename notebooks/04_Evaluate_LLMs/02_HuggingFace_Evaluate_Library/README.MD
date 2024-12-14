
[Let's talk about LLM evaluation by HuggingFace](https://huggingface.co/blog/clefourrier/llm-evaluation)

[Huggngface Evaluator tutorial]: https://huggingface.co/docs/evaluate/en/base_evaluator

## Using the evaluator

According to [Huggngface](https://huggingface.co/docs/evaluate/en/base_evaluator):

>The Evaluator classes allow to evaluate a triplet of model, dataset, and metric. The models wrapped in a pipeline, responsible for handling all preprocessing and post-processing and out-of-the-box, Evaluators support transformers pipelines for the supported tasks, but custom pipelines can be passed, as showcased in the section Using the evaluator with custom pipelines.

>Currently supported tasks are:
>- "text-classification": will use the TextClassificationEvaluator.
>- "token-classification": will use the TokenClassificationEvaluator.
>- "question-answering": will use the QuestionAnsweringEvaluator.
>- "image-classification": will use the ImageClassificationEvaluator.
>- "text-generation": will use the TextGenerationEvaluator.
>- "text2text-generation": will use the Text2TextGenerationEvaluator.
>- "summarization": will use the SummarizationEvaluator.
>- "translation": will use the TranslationEvaluator.
>- "automatic-speech-recognition": will use the - AutomaticSpeechRecognitionEvaluator.

## Evaluate question answering


[Evaluate question answering](https://huggingface.co/docs/transformers/en/tasks/question_answering):

`Question answering` tasks return an answer given a question. If you’ve ever asked a virtual assistant like Alexa, Siri or Google what the weather is, then you’ve used a question answering model before. There are two common types of question answering tasks:
- `Extractive`: extract the answer from the given context.
- `Abstractive`: generate an answer from the context that correctly answers the question.


[Evaluate LLMs and RAG a practical example using Langchain and Hugging Face](https://www.philschmid.de/evaluate-llm):

Academic benchmarks can no longer always be applied to generative models since the correct or most helpful answer can be formulated in different ways, which would give limited insight into real-world performance.

Two main approaches show promising results for evaluating LLMs: 
1. leveraging human evaluations :
   - provides the `most natural measure of qualit`y but `does not scale well`.
   - Crowdsourcing services can be used to collect human assessments on dimensions like relevance, fluency, and harmfulness. However, this process is relatively slow and costly.
2. using LLMs themselves as judges.
   - approach called [LLM-as-a-judge](https://arxiv.org/abs/2306.05685) demonstrates that large LLMs like GPT-4 can match human preferences with over 80% agreement when evaluating conversational chatbots.
  

The  colab notebook included here show evaluate model using huggingface evaluate and sklearn.