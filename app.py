import streamlit as st

# -----------------------------
# 기본 설정
# -----------------------------

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="wide"
)

# -----------------------------
# 게임 데이터
# -----------------------------

games = {
    "🍔 음식": [
        ("🍗", "평생 치킨만 먹기", "🍕", "평생 피자만 먹기"),
        ("🍜", "평생 라면만 먹기", "🍔", "평생 햄버거만 먹기"),
        ("🍣", "평생 초밥만 먹기", "🥩", "평생 고기만 먹기"),
        ("🍰", "평생 디저트만 먹기", "🍚", "평생 밥만 먹기"),
        ("🌶️", "평생 매운 음식 먹기", "🍯", "평생 단 음식 먹기"),
    ],

    "🎉 주말": [
        ("🏠", "집에서 하루 종일 쉬기", "🚗", "즉흥 드라이브 떠나기"),
        ("🎬", "집에서 영화 보기", "🎤", "친구들과 노래방 가기"),
        ("🏕️", "캠핑 가기", "🏨", "호텔에서 호캉스하기"),
        ("⚽", "친구들과 운동하기", "🎮", "하루 종일 게임하기"),
        ("☕", "카페 투어하기", "🍽️", "맛집 투어하기"),
    ],

    "✈️ 여행": [
        ("🇯🇵", "일본 일주일 여행", "🇹🇭", "태국 일주일 여행"),
        ("🏖️", "몰디브에서 휴양", "🏔️", "스위스 여행"),
        ("🇫🇷", "파리 한 달 살기", "🇺🇸", "뉴욕 한 달 살기"),
        ("🌊", "바다 여행", "⛰️", "산 여행"),
        ("🚆", "유럽 기차 여행", "🚗", "미국 렌터카 여행"),
    ],
}


# -----------------------------
# 세션 상태
# -----------------------------

if "category" not in st.session_state:
    st.session_state.category = "🍔 음식"

if "question" not in st.session_state:
    st.session_state.question = 0

if "score_a" not in st.session_state:
    st.session_state.score_a = 0

if "score_b" not in st.session_state:
    st.session_state.score_b = 0

if "finished" not in st.session_state:
    st.session_state.finished = False

if "history" not in st.session_state:
    st.session_state.history = []


# -----------------------------
# 게임 초기화 함수
# -----------------------------

def restart_game(category=None):

    if category is not None:
        st.session_state.category = category

    st.session_state.question = 0
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.finished = False
    st.session_state.history = []


# -----------------------------
# 선택 함수
# -----------------------------

def answer(side):

    current_game = games[st.session_state.category]
    current_question = current_game[st.session_state.question]

    emoji_a = current_question[0]
    text_a = current_question[1]

    emoji_b = current_question[2]
    text_b = current_question[3]

    if side == "A":
        st.session_state.score_a += 1
        selected = f"{emoji_a} {text_a}"

    else:
        st.session_state.score_b += 1
        selected = f"{emoji_b} {text_b}"

    st.session_state.history.append({
        "question": f"{text_a} VS {text_b}",
        "answer": selected
    })

    st.session_state.question += 1

    if st.session_state.question >= len(current_game):
        st.session_state.finished = True


# -----------------------------
# 제목
# -----------------------------

st.title("⚖️ 밸런스 게임")

st.write(
    "둘 중 하나만 선택해야 한다면? "
    "당신의 선택은 무엇인가요?"
)

st.divider()


# -----------------------------
# 카테고리 선택
# -----------------------------

st.subheader("🎮 게임 선택")

category_list = list(games.keys())

columns = st.columns(len(category_list))

for i, category in enumerate(category_list):

    with columns[i]:

        if st.button(
            category,
            key=f"category_{i}",
            use_container_width=True
       
