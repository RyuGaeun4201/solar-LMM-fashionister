import warnings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain.docstore.document import Document
from langchain_upstage import UpstageEmbeddings
import pandas as pd

warnings.filterwarnings("ignore")
load_dotenv()

file_path = "data/data.csv"

df = pd.DataFrame(pd.read_csv(file_path))

splits = [Document(page_content=text) for text in df["article"]]

vectorstore = Chroma.from_documents(documents=splits, embedding=UpstageEmbeddings(model="solar-embedding-1-large", embed_batch_size=100))
retriever = vectorstore.as_retriever()