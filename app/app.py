from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

with open("guide1.txt") as f:
    hitchhikersguide = f.read()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator = "\n")
texts = text_splitter.split_text(hitchhikersguide)

embeddings = OpenAIEmbeddings()

docsearch = Chroma.from_texts(texts, embeddings, metadatas=[{"source": str(i)} for i in range(len(texts))]).as_retriever()

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")

def make_inference(query):
    docs = docsearch.get_relevant_documents(query)
    return(chain.run(input_documents=docs, question=query))

if __name__ == "__main__":
    # make a gradio interface
    import gradio as gr

    gr.Interface(
        make_inference,
        [
            gr.inputs.Textbox(lines=2, label="Query"),
        ],
        gr.outputs.Textbox(label="Response"),
        title="🗣️TalkToMyDoc📄",
        description="🗣️TalkToMyDoc📄 is a tool that allows you to ask questions about a document. In this case - Hitch Hitchhiker's Guide to the Galaxy.",
    ).launch()