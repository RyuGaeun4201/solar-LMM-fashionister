import warnings
from langchain_upstage import UpstageLayoutAnalysisLoader
from dotenv import load_dotenv
from IPython.display import display, HTML

warnings.filterwarnings("ignore")
load_dotenv()

file_path = "data/data1.pdf"

from langchain_community.retrievers import BM25Retriever
from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)

text_splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=1000, chunk_overlap=100, language=Language.HTML 
)

layzer = UpstageLayoutAnalysisLoader(file_path, output_type="html")
docs = layzer.load()  # or layzer.lazy_load()

splits = text_splitter.split_documents(docs)

retriever = BM25Retriever.from_documents(splits)