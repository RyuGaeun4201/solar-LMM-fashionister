from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import ChatUpstage
from retriever import retriever

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

query = "Choose the clothes to wear today?"
context_docs = retriever.invoke("clothes")
print(chain.invoke({"question": query, "Context": context_docs}))