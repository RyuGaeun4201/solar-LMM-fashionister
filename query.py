from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import ChatUpstage
from retriever import retriever

llm = ChatUpstage()

prompt_template = PromptTemplate.from_template(
    """
    Please provide most correct answer from the following context. Answer simplely.
    ---
    Question: {question}
    ---
    Context: {Context}
    """
)
chain = prompt_template | llm | StrOutputParser()

query = "오늘은 어떤 상의와 하의를 입을까?"
# context_docs = retriever.invoke("옷")
print(retriever.invoke({"question": query})) #, "Context": context_docs}))