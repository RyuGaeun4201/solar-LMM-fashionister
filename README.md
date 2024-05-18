# Solar-LMM-Fashminator

## 개요

**Fashminator**는 사용자가 키, 체중, 나이, 성별, 국적를 입력하면 날씨, 일정, 모임 목적에 맞춰 최신 패션 트렌드를 학습하여 최적의 옷을 추천해주는 시스템입니다. 추천 알고리즘을 향상시키기 위해 Solar LLM과 Diffusion LLM을 활용하며, Gradio를 사용하여 사용자 인터페이스를 제공합니다.

## 발표 자료 
[발표자료](https://docs.google.com/presentation/d/1uyAoUuMgXxiS-XoT_PCK_eb-_G8-RIJ_SeiYupHaJLI/edit?usp=sharing)

## 데모
![데모시연](./text.png)

## 기능

- 사용자가 입력한 키와 체중, 나이, 국가 에 맞추어 입력
- 현재 날씨 정보를 기반으로 옷 추천
- 일정 및 모임 목적에 맞춘 옷 추천
- 최신 패션 트렌드를 반영한 옷 추천
- Solar LLM을 통한 추천 텍스트 생성
- Diffusion LLM을 통한 추천 이미지 생성
- Gradio를 통한 사용자 친화적인 인터페이스 제공

## 아키텍처 

서비스는 다음과 같은 구성 요소로 이루어져 있습니다:
1. **User Interface (UI)**: Gradio를 사용하여 사용자 입력을 받습니다.
2. **Weather API**: 날씨 정보를 제공합니다.
3. **Schedule & Event API**: 일정 및 모임 목적 정보를 제공합니다.
4. **Fashion Trends API**: 최신 패션 트렌드 데이터를 제공합니다.
5. **Solar LLM**: 텍스트 기반의 추천을 제공합니다.
6. **Diffusion LLM**: 이미지 기반의 추천을 제공합니다.
7. **Recommendation Engine**: Solar LLM과 Diffusion LLM을 통합하여 최적의 옷을 추천합니다.
9. **Backend Server**: 각 구성 요소를 연결하고 데이터를 처리합니다.


## 개발과정 문서
[의논중인 문서](https://docs.google.com/document/d/132_GdweLA4OVlep6Rywna2vfH2TXkhGr_9l2hu02ILo/edit?usp=sharing)


## 수집데이터
[학습데이터 소스](./data/data.csv)

## 구성도 
![구성도](./assets/solar_LLM_fachionitor_architecture.png)


## 유저 흐름

```
사용자 -------------------------
     | (웹 브라우저 접속)
     V
Gradio UI ----------------------
     | (키, 체중, 나이, 국적 입력)
     V
"제출" 버튼 클릭 ---------------
     | (정보 전달)
     V
solar_lmm_fashminator 실행 -----
     | (추천 옷 텍스트 생성)
     V
generate_outfit_image 실행 -----
     | (DALL·E API 호출)
     V
Gradio UI ----------------------
     | (추천 옷 텍스트와 이미지 표시)
     V
사용자 -------------------------
     | (결과 확인 및 추가 입력)
     V
(반복)
```

## 설치 및 실행

1. **클론 저장소**:
   ```bash
   git clone https://github.com/username/fashminator.git
   cd fashminator


## 실행 방법

1. 아래의 스크립트를 실행하여 웹 애플리케이션을 시작합니다.
    ```bash
    python app.py
    ```

2. 웹 브라우저에서 `http://localhost:7860`을 열어 애플리케이션에 접속합니다.


## 사용법

1. **신체 정보와 국적 입력**: 키, 몸무게, 나이, 국적을 입력합니다.
2. **물어보기 버튼 클릭**: '물어보기' 버튼을 클릭하여 추천된 옷차림을 확인합니다.
3. **다크모드 전환**: 상단의 '다크모드' 버튼을 클릭하여 다크모드와 라이트모드를 전환합니다.
4. **리셋 버튼 클릭**: '리셋' 버튼을 클릭하여 입력 필드를 초기화합니다.

## 실행 예시

스크립트를 실행한 후 웹 브라우저에서 다음 주소로 접속하여 애플리케이션을 사용하세요:
