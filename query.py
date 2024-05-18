from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import ChatUpstage
from retriever import retriever
from weather import weather

llm = ChatUpstage()

prompt_template = PromptTemplate.from_template(
    """
    user의 신체 정보, 오늘의 날씨와 user가 자신이 가지고 있는 옷에 맞춰 옷을 정해주세요.
    존댓말로 답변해주세요.
    Q. user는 키: 175 cm, 체중: 66 kg, 나이: 30세, 국적: 대한민국에 가지고 있습니다. 오늘의 날씨는 "작은 일교차, 습도가 우천 예보 없음, 구름이 구름 조금, 바람이 강풍"하고 user가 긴 청색 바지를 골랐습니다. 어떤 상의와 하의를 입을까요?
    A. 당신의 신체 정보, 오늘의 날씨와 요즘 패션트랜드를 고려해서 고른신 긴 청색 바지와 함께 갈색 코트를 추천 합니다.
    ---
    Question: {question}
    ---
    Context: {Context}
    """
)
chain = prompt_template | llm | StrOutputParser()

def answer(height, weight, age, nationality, keyword) :
    query = f"당신의 키: {height} cm, 체중: {weight} kg, 나이: {age}세, 국적: {nationality}에 가지고 있습니다. 오늘의 날씨는 '{weather()}'하고 user가 {keyword}를 골랐습니다. 오늘은 어떤 상의와 하의를 입을까요?"
    context_docs = retriever.invoke(keyword)
    return chain.invoke({"question": query, "Context": context_docs})