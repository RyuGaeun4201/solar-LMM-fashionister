# %load_ext dotenv
# %dotenv

import warnings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import ChatUpstage
from langchain_upstage import UpstageLayoutAnalysisLoader
from langchain_upstage import UpstageLayoutAnalysis
warnings.filterwarnings("ignore")

file_path = "data/data1.pdf"

llm = ChatUpstage()

prompt_template = PromptTemplate.from_template(
    """
    Please provide most correct answer from the following context. 
    If the answer is not present in the context, please write "The information is not present in the context."
    ---
    Question: {question}
    ---
    Context: {Context}
    """
)
chain = prompt_template | llm | StrOutputParser()

from langchain_community.retrievers import BM25Retriever
from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)

text_splitter = RecursiveCharacterTextSplitter.from_language( # chunking
    chunk_size=1000, chunk_overlap=100, language=Language.HTML # 10%
)

layzer = UpstageLayoutAnalysisLoader(file_path, output_type="html")
docs = layzer.load()  # or layzer.lazy_load()

splits = text_splitter.split_documents(docs)

retriever = BM25Retriever.from_documents(splits) # search engine

query = "What is bug classficiation?"
context_docs = retriever.invoke("bug")
chain.invoke({"question": query, "Context": context_docs})