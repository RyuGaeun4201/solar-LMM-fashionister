import gradio as gr

def recommend_clothing(height, weight, age, nationality):
    # 더미 데이터를 사용한 추천 옷 텍스트 생성
    recommended_outfit = f"당신의 키: {height} cm, 체중: {weight} kg, 나이: {age}세, 국적: {nationality}에 기반하여, 우리는 가벼운 자켓, 청바지, 스니커즈가 포함된 캐주얼한 옷차림을 추천합니다."
    
    # 더미 이미지 URL
    dummy_image_url = "https://via.placeholder.com/1024"
    
    return recommended_outfit, dummy_image_url

# OECD 주요국 리스트
oecd_countries = [
    "대한민국 🇰🇷",
    "미국 🇺🇸",
    "일본 🇯🇵",
    "독일 🇩🇪",
    "프랑스 🇫🇷",
    "영국 🇬🇧",
    "캐나다 🇨🇦",
    "이탈리아 🇮🇹",
    "호주 🇦🇺",
    "스페인 🇪🇸",
    "네덜란드 🇳🇱",
    "스위스 🇨🇭",
    "스웨덴 🇸🇪",
    "노르웨이 🇳🇴",
    "덴마크 🇩🇰",
    "핀란드 🇫🇮"
]
# Gradio 인터페이스 설정
with gr.Blocks() as ui:
    gr.Markdown("# 👗 Solar-LMM-Fashminator 옷 추천 시스템 👔")
    
    gr.Markdown("[📖 GitHub README](https://github.com/RyuGaeun4201/solar-LMM-fashionister/blob/main/README.md)")
    
    with gr.Row():
        height = gr.Slider(minimum=100, maximum=250, value=176, label="📏 키 (cm)")
        weight = gr.Slider(minimum=30, maximum=200, value=78, label="⚖️ 몸무게 (kg)")
        age = gr.Slider(minimum=1, maximum=100, value=42, label="🎂 나이(한국나이)")
        nationality = gr.Dropdown(choices=oecd_countries, value="대한민국", label="🌍 국적")
        
    recommend_button = gr.Button("물어보기 🛒")
    
    with gr.Row():
        recommended_outfit = gr.Textbox(label="👗 추천된 옷차림")
        outfit_image = gr.Image(label="📸 이런 옷을 입고 나가봐! 이미지")
    
    recommend_button.click(
        fn=recommend_clothing, 
        inputs=[height, weight, age, nationality], 
        outputs=[recommended_outfit, outfit_image]
    )

    gr.Markdown("## 간단한 사용법 📝")
    gr.Markdown("""
    1. 📏 키, ⚖️ 몸무게, 🎂 나이, 🌍 국적을 입력하세요.
    2. 🛒 '물어보기' 버튼을 클릭하세요.
    3. 👗 추천된 옷차림 텍스트와 📸 이미지를 확인하세요.
    4. 다른 입력값으로 반복하여 다양한 추천을 받아보세요.
    """)

# 인터페이스 실행
ui.launch()