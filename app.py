import streamlit as st
import random

# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800;900&display=swap');

* {
    font-family: 'Noto Sans KR', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 107, 107, 0.12), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(108, 92, 231, 0.12), transparent 30%),
        #f8f9fc;
}

/* 전체 컨테이너 */

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* 제목 */

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    margin-bottom: 8px;
    color: #202124;
}

.sub-title {
    text-align: center;
    color: #777;
    font-size: 17px;
    margin-bottom: 35px;
}

/* 카테고리 */

.category-title {
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 15px;
}

/* 카드 */

.balance-card {
    min-height: 330px;
    border-radius: 28px;
    padding: 35px 25px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    transition: all 0.2s ease;
    margin-bottom: 10px;
}

.card-left {
    background: linear-gradient(145deg, #fff1f2, #ffe4e6);
    border: 2px solid #fecdd3;
}

.card-right {
    background: linear-gradient(145deg, #eef2ff, #e0e7ff);
    border: 2px solid #c7d2fe;
}

.card-label {
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 18px;
    color: #777;
}

.card-emoji {
    font-size: 65px;
    margin-bottom: 20px;
}

.card-text {
    font-size: 27px;
    font-weight: 800;
    line-height: 1.4;
    color: #222;
}

/* VS */

.vs-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 330px;
}

.vs {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: #202124;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    font-size: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.18);
}

/* 결과 */

.result-box {
    padding: 30px;
    background: white;
    border-radius: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    text-align: center;
    margin-top: 30px;
}

.result-title {
    font-size: 28px;
    font-weight: 900;
    margin-bottom: 10px;
}

.result-text {
    color: #666;
}

/* 버튼 */

.stButton > button {
    border-radius: 15px;
    height: 52px;
    font-size: 16px;
    font-weight: 800;
    border: none;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* 선택 버튼 */

.choice-left button {
    background: #ff6b81 !important;
    color: white !important;
}

.choice-right button {
    background: #6c5ce7 !important;
    color: white !important;
}

/* 진행률 */

.progress-text {
    text-align: center;
    color: #888;
    margin-bottom: 8px;
}

.footer {
    text-align: center;
    color: #999;
    margin-top: 60px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 게임 데이터
# --------------------------------------------------

GAME_DATA = {

    "🍔 음식": [
        {
            "left": {
                "emoji": "🍗",
                "text": "평생 치킨만 먹기"
            },
            "right": {
                "emoji": "🍕",
                "text": "평생 피자만 먹기"
            }
        },
        {
            "left": {
                "emoji": "🍜",
                "text": "매일 라면 먹기"
            },
            "right": {
                "emoji": "🍔",
                "text": "매일 햄버거 먹기"
            }
        },
        {
            "left": {
                "emoji": "🍣",
                "text": "초밥만 먹기"
            },
            "right": {
                "emoji": "🥩",
                "text": "고기만 먹기"
            }
        },
        {
            "left": {
                "emoji": "🍰",
                "text": "디저트 없이 살기"
            },
            "right": {
                "emoji": "🍚",
                "text": "밥 없이 살기"
            }
        },
        {
            "left": {
                "emoji": "🌶️",
                "text": "평생 매운 음식"
            },
            "right": {
                "emoji": "🍯",
                "text": "평생 단 음식"
            }
        },
    ],

    "🎉 주말": [
        {
            "left": {
                "emoji": "🏠",
                "text": "집에서 하루 종일 누워있기"
            },
            "right": {
                "emoji": "🚗",
                "text": "즉흥적으로 드라이브 떠나기"
            }
        },
        {
            "left": {
                "emoji": "🎬",
                "text": "집에서 영화 3편 보기"
            },
            "right": {
                "emoji": "🎤",
                "text": "친구들과 노래방 가기"
            }
        },
        {
            "left": {
                "emoji": "🏕️",
                "text": "캠핑 떠나기"
            },
            "right": {
                "emoji": "🏨",
                "text": "호텔에서 호캉스"
            }
        },
        {
            "left": {
                "emoji": "⚽",
                "text": "친구들과 운동하기"
            },
            "right": {
                "emoji": "🎮",
                "text": "하루 종일 게임하기"
            }
        },
        {
            "left": {
                "emoji": "☕",
                "text": "카페 투어하기"
            },
            "right": {
                "emoji": "🍻",
                "text": "맛집 투어하기"
            }
        },
    ],

    "✈️ 여행": [
        {
            "left": {
                "emoji": "🇯🇵",
                "text": "일본에서 일주일 여행"
            },
            "right": {
                "emoji": "🇹🇭",
                "text": "태국에서 일주일 여행"
            }
        },
        {
            "left": {
                "emoji": "🏖️",
                "text": "몰디브에서 휴양"
            },
            "right": {
                "emoji": "🏔️",
                "text": "스위스에서 자연 여행"
            }
        },
        {
            "left": {
                "emoji": "🇫🇷",
                "text": "파리에서 한 달 살기"
            },
            "right": {
                "emoji": "🇺🇸",
                "text": "뉴욕에서 한 달 살기"
            }
        },
        {
            "left": {
                "emoji": "🌊",
                "text": "바다 여행"
            },
            "right": {
                "emoji": "⛰️",
                "text": "산 여행"
            }
        },
        {
            "left": {
                "emoji": "🚆",
                "text": "기차 타고 유럽 여행"
            },
            "right": {
                "emoji": "🚗",
                "text": "렌터카로 미국 여행"
            }
        },
    ]
}


# --------------------------------------------------
# Session State 초기화
# --------------------------------------------------

if "category" not in st.session_state:
    st.session_state.category = "🍔 음식"

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "left_score" not in st.session_state:
    st.session_state.left_score = 0

if "right_score" not in st.session_state:
    st.session_state.right_score = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "game_finished" not in st.session_state:
    st.session_state.game_finished = False


# --------------------------------------------------
# 게임 초기화
# --------------------------------------------------

def reset_game(category=None):

    if category:
        st.session_state.category = category

    st.session_state.question_index = 0
    st.session_state.left_score = 0
    st.session_state.right_score = 0
    st.session_state.history = []
    st.session_state.game_finished = False


# --------------------------------------------------
# 선택 처리
# --------------------------------------------------

def choose(side):

    question = GAME_DATA[
        st.session_state.category
    ][st.session_state.question_index]

    if side == "left":

        st.session_state.left_score += 1

        selected = question["left"]
        other = question["right"]

    else:

        st.session_state.right_score += 1

        selected = question["right"]
        other = question["left"]

    st.session_state.history.append({
        "question": f"{question['left']['text']} VS {question['right']['text']}",
        "selected": selected["text"]
    })

    st.session_state.question_index += 1

    if st.session_state.question_index >= len(
        GAME_DATA[st.session_state.category]
    ):
        st.session_state.game_finished = True


# --------------------------------------------------
# 헤더
# --------------------------------------------------

st.markdown(
    '<div class="main-title">⚖️ 밸런스 게임</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">둘 중 하나만 선택해야 한다면?</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# 카테고리 선택
# --------------------------------------------------

st.markdown(
    '<div class="category-title">게임 카테고리</div>',
    unsafe_allow_html=True
)

categories = list(GAME_DATA.keys())

category_cols = st.columns(len(categories))

for i, category in enumerate(categories):

    with category_cols[i]:

        if st.button(
            category,
            key=f"category_{i}",
            use_container_width=True
        ):
            reset_game(category)
            st.rerun()


# --------------------------------------------------
# 현재 게임
# --------------------------------------------------

questions = GAME_DATA[st.session_state.category]

total_questions = len(questions)

current_index = st.session_state.question_index


# --------------------------------------------------
# 결과 화면
# --------------------------------------------------

if st.session_state.game_finished:

    st.markdown(
        '<div class="result-box">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="result-title">🎉 게임 종료!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="result-text">당신의 선택 결과입니다.</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        st.metric(
            "🔴 왼쪽 선택",
            f"{st.session_state.left_score}회"
        )

    with result_col2:

        st.metric(
            "🔵 오른쪽 선택",
            f"{st.session_state.right_score}회"
        )

    # 결과 메시지

    if st.session_state.left_score > st.session_state.right_score:

        st.success(
            f"🔴 당신은 **왼쪽 선택을 더 좋아하는 타입**이에요!"
        )

    elif st.session_state.right_score > st.session_state.left_score:

        st.info(
            f"🔵 당신은 **오른쪽 선택을 더 좋아하는 타입**이에요!"
        )

    else:

        st.warning(
            "⚖️ 왼쪽과 오른쪽 선택이 정확히 반반이에요!"
        )

    st.write("")

    st.subheader("📋 나의 선택 기록")

    for i, item in enumerate(
        st.session_state.history,
        start=1
    ):

        st.write(
            f"**{i}.** {item['question']}  \n"
            f"👉 선택: **{item['selected']}**"
        )

    st.write("")

    if st.button(
        "🔄 다시 플레이",
        use_container_width=True
    ):

        reset_game()
        st.rerun()


# --------------------------------------------------
# 게임 진행
# --------------------------------------------------

else:

    progress = current_index / total_questions

    st.markdown(
        f'<div class="progress-text">'
        f'Question {current_index + 1} / {total_questions}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.progress(progress)

    st.write("")

    question = questions[current_index]

    left = question["left"]
    right = question["right"]

    # 카드 영역

    col_left, col_vs, col_right = st.columns(
        [5, 1, 5]
    )

    with col_left:

        st.markdown(
            f"""
            <div class="balance-card card-left">

                <div class="card-label">
                    OPTION A
                </div>

                <div class="card-emoji">
                    {left["emoji"]}
                </div>

                <div class="card-text">
                    {left["text"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col_vs:

        st.markdown(
            """
            <div class="vs-container">
                <div class="vs">
                    VS
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_right:

        st.markdown(
            f"""
            <div class="balance-card card-right">

                <div class="card-label">
                    OPTION B
                </div>

                <div class="card-emoji">
                    {right["emoji"]}
                </div>

                <div class="card-text">
                    {right["text"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # 선택 버튼

    button_left, button_right = st.columns(2)

    with button_left:

        st.markdown(
            '<div class="choice-left">',
            unsafe_allow_html=True
        )

        if st.button(
            f"🔴 {left['text']}",
            key=f"left_{current_index}",
            use_container_width=True
        ):

            choose("left")
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with button_right:

        st.markdown(
            '<div class="choice-right">',
            unsafe_allow_html=True
        )

        if st.button(
            f"🔵 {right['text']}",
            key=f"right_{current_index}",
            use_container_width=True
        ):

            choose("right")
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        ⚖️ Balance Game · Made with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
