from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import ChatUpstage
from retriever import retriever

llm = ChatUpstage()

keyword = "pants"

prompt_template = PromptTemplate.from_template(
    """
    날씨와 패션 트랜드에 맞춰 옷을 정해주세요.
    user가 자신이 가지고 있는 옷 중 하나 input으로 준다면, 그 옷에 어울리는 다른 옷들을 정해주세요.
    user가 자신이 옷을 정하지 않을 수 있습니다. 그렇다면, 모든 옷을 정해주세요.
    존댓말로 답변해주세요.
    예를 들어 일교차가 크지 않고, 비가 오지 않으며, 구름이 조금 있고 온도가 온건하므로, user가 {keyword}을 골랐습니다. 
    Q. 오늘은 어떤 상의와 하의를 입을까?
    A. 날씨와 요즘 패션트랜드를 고려해서 고른신 {keyword}와 함께 short_sleeve_T-Shirt을 추천 합니다.
    ---
    Question: {question}
    ---
    Context: {Context}
    """
)
chain = prompt_template | llm | StrOutputParser()

# print(chain.invoke("오늘은 어떤 상의와 하의를 입을까?"))

query = "오늘은 어떤 상의와 하의를 입을까?"
context_docs = retriever.invoke("옷")
print(chain.invoke({"question": query, "Context": context_docs, "keyword": keyword}))