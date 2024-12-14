import chainlit as cl
#from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from chainlit.types import ThreadDict
from chainlit.cli import run_chainlit
from langchain_ollama.llms import OllamaLLM

@cl.on_chat_start
async def on_chat_start():
    # # model_id = "tiiuae/falcon-7b-instruct"  # this model is too large to run on Nvidia 4090 with 16G ram
    print("staring chat")
    model = OllamaLLM(model="phi3", base_url="http://localhost:11434")
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a AI chatbot with an extensive expert knowledge.",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser() #llm chain
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable
    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()

@cl.on_stop
def on_stop():
    print("The user wants to stop the task!")

@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")

@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    print("The user resumed a previous chat session!")
    
if __name__ == "__main__":
    print("initiating")
    run_chainlit(__file__)