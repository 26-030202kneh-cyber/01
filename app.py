import streamlit as st

# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(255, 107, 129, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(108, 92, 231, 0.12),
                transparent 30%
            ),
            #f7f7fb;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 40px;
        padding-bottom: 60px;
    }

    /* 제목 */

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 900;
        color: #202124;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        font-size: 17px;
        color: #777;
        margin-bottom: 35px;
    }

    /* 카테고리 */

    .section-title {
        font-size: 18px;
        font-weight: 800;
        color: #333;
        margin: 25px 0 12px 0;
    }

    /* 카드 */

    .game-card {
        min-height: 300px;
        border-radius: 28px;
        padding: 35px 25px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
        margin-top: 10px;
    }

    .left-card {
        background: linear-gradient(
            145deg,
            #fff1f2,
            #ffe4e6
        );
        border: 2px solid #fecdd3;
        box-shadow: 0 15px 35px rgba(255, 107, 129, 0.12);
    }

    .right-card {
        background: linear-gradient(
            145deg,
            #eef2ff,
            #e0e7ff
        );
        border: 2px solid #c7d2fe;
        box-shadow: 0 15px 35px rgba(108, 92, 231, 0.12);
    }

    .option-label {
        font-size: 13px;
        font-weight: 800;
        color: #888;
        margin-bottom: 18px;
    }

    .emoji {
        font-size: 65px;
        margin-bottom: 15px;
    }

    .option-text {
        font-size: 25px;
        font-weight: 800;
        line-height: 1.45;
        color: #222;
        word-break: keep-all;
    }

    /* VS */

    .vs-wrapper {
        height: 320px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .vs {
        width: 65px;
        height: 65px;
        border-radius: 50%;
        background: #202124;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        font-weight: 900;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    }

    /* 진행률 */

    .question-number {
        text-align: center;
        font-size: 14px;
        font-weight: 700;
        color: #888;
        margin-top: 20px;
    }

    /* 버튼 */

    .stButton > button {
        width: 100%;
        min-height: 52px;
        border-radius: 15px;
        border: none;
        font-size: 16px;
        font-weight: 800;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }

    /* 결과 */

    .result-card {
        background: white;
        border-radius: 25px;
        padding: 40px 25px;
        text-align: center;
        box-shadow: 0 12px 35px rgba(0,0,0,0.08);
        margin-top: 30px;
    }

    .result-title {
        font-size: 32px;
        font-weight: 900;
        margin-bottom: 10px;
    }

    .result-description {
        color: #777;
        font-size: 16px;
    }

    /* Footer */

    .footer {
        text-align: center;
        color: #999;
        font-size: 13px;
        margin-top: 60px;
    }

    /* 모바일 */

    @media (max-width: 768px) {

        .main-title {
            font-size: 34px;
        }

        .option-text {
            font-size: 20px;
        }

        .emoji {
            font-size: 50px;
        }

        .game-card {
            min-height: 240px;
        }

        .vs-wrapper {
            height: 70px;
        }

        .vs {
            width: 55px;
            height: 55px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 게임 데이터
# =========================================================

GAME_DATA = {
    "🍔 음식": [
        {
            "left": {"emoji": "🍗", "text": "평생 치킨만 먹기"},
            "right": {"emoji": "🍕", "text": "평생 피자만 먹기"},
        },
        {
            "left": {"emoji": "🍜", "text": "매일 라면 먹기"},
            "right": {"emoji": "🍔", "text": "매일 햄버거 먹기"},
        },
        {
            "left": {"emoji": "🍣", "text": "초밥만 먹기"},
            "right": {"emoji": "🥩", "text": "고기만 먹기"},
        },
        {
            "left": {"emoji": "🍰", "text": "디저트 없이 살기"},
            "right": {"emoji": "🍚", "text": "밥 없이 살기"},
        },
        {
            "left": {"emoji": "🌶️", "text": "평생 매운 음식"},
            "right": {"emoji": "🍯", "text": "평생 단 음식"},
        },
    ],

    "🎉 주말": [
        {
            "left": {"emoji": "🏠", "text": "집에서 하루 종일 누워있기"},
            "right": {"emoji": "🚗", "text": "즉흥적으로 드라이브 떠나기"},
        },
        {
            "left": {"emoji": "🎬", "text": "집에서 영화 3편 보기"},
            "right": {"emoji": "🎤", "text": "친구들과 노래방 가기"},
        },
        {
            "left": {"emoji": "🏕️", "text": "캠핑 떠나기"},
            "right": {"emoji": "🏨", "text": "호텔에서 호캉스"},
        },
        {
            "left": {"emoji": "⚽", "text": "친구들과 운동하기"},
            "right": {"emoji": "🎮", "text": "하루 종일 게임하기"},
        },
        {
            "left": {"emoji": "☕", "text": "카페 투어하기"},
            "right": {"emoji": "🍽️", "text": "맛집 투어하기"},
        },
    ],

    "✈️ 여행": [
        {
