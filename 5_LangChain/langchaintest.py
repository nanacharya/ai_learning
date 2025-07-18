import  langchain
from   transformers import  pipeline
import dataset

print("Set up done")

knowledge_base =""" LangChain is an open-source framework for building applications around large language models (LLMs) like GPT-4, Claude, or Cohere, in a structured, composable, and reliable way. It is written mainly in Python and JavaScript/TypeScript, and it dramatically simplifies the work of connecting LLMs with data sources, tools, and user workflows.

LangChain essentially takes the raw “talk-to-an-LLM” concept and upgrades it to a full-blown reasoning engine that can interact with the world. Think of it like a smart assistant “operating system” you can plug into other data, APIs, and tools to do far more than chat.

 """
#Load the question-answering pipeline

qa_pipeline = pipeline("question-answering", model ="distilbert-base-cased-distilled-squad")

def answer_question(question, context=knowledge_base):
    response = qa_pipeline(question= question, context= context)
    answer = response['answer']
    score = response['score']

    return answer, score

question = "what is LangChain ?"

answer, confidence = answer_question(question)
print("Question : " , question)
print(f"Question : {question}")
print("Answer : " , answer)
print("confidence : " , confidence)
print("confidence : " , confidence)


