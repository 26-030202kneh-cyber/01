import streamlit as st


# ============================================
# 페이지 설정
# ============================================

st.set_page_config(
    page_title="밸런스 게임",
    page_icon="⚖️",
    layout="wide"
)


# ============================================
# 게임 데이터
# ============================================

GAME_DATA = {
    "🍔 음식": [
        {
            "a": "🍗 평생 치킨만 먹기",
            "b": "🍕 평생 피자만 먹기"
        },
        {
            "a": "🍜 평생 라면만 먹기",
            "b": "🍔 평생 햄버거만 먹기"
        },
        {
            "a": "🍣 평생 초밥만 먹기",
            "b": "🥩 평생 고기만 먹기"
        },
        {
            "a": "🍰 평생 케이크만 먹기",
            "b": "🍚 평생 밥만 먹기"
        },
        {
            "a": "🌶️ 평생 매운 음식 먹기",
            "b": "🍯 평생 단 음식 먹기"
        }
    ],

    "🎉 주말": [
        {
            "a": "🏠 집에서 하루 종일 쉬기",
            "b": "🚗 즉흥 드라이브 떠나기"
        },
        {
            "a": "🎬 집에서 영화 보기",
            "b": "🎤 친구들과 노래방 가기"
        },
        {
            "a": "🏕️ 캠핑 가기",
            "b": "🏨 호텔에서 호캉스하기"
        },
        {
            "a": "⚽ 친구들과 운동하기",
            "b": "🎮 하루 종일 게임하기"
        },
        {
            "a": "☕ 카페 투어하기",
            "b": "🍽️ 맛집 투어하기"
        }
    ],

    "✈️ 여행": [
        {
            "a": "🇯🇵 일본에서 일주일 여행",
            "b": "🇹🇭 태국에서 일주일 여행"
        },
        {
            "a": "🏖️ 몰디브에서 휴양하기",
            "b": "🏔️ 스위스 여행하기"
        },
        {
            "a": "🇫🇷 파리에서 한 달 살기",
            "b": "🇺🇸 뉴욕에서 한 달 살기"
        },
        {
            "a": "🌊 바다 여행하기",
            "b": "⛰️ 산 여행하기"
        },
        {
            "a": "🚆 기차로 유럽 여행하기",
            "b": "🚗 렌터카로 미국 여행하기"
        }
    ]
}


# ============================================
# 세션 상태
# ============================================

if "category" not in st.session_state:
    st.session_state.category = "🍔 음식"

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "score_a" not in st.session_state:
    st.session_state.score_a = 0

if "score_b" not in st.session_state:
    st.session_state.score_b = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "finished" not in st.session_state:
    st.session_state.finished = False


# ============================================
# 게임 초기화
# ============================================

def reset_game(category):

    st.session_state.category = category

    st.session_state.question_index = 0

    st.session_state.score_a = 0

    st.session_state.score_b = 0

    st.session_state.history = []

    st.session_state.finished = False


# ============================================
# A 선택
# ============================================

def select_a():

    category = st.session_state.category

    index = st.session_state.question_index

    question = GAME_DATA[category][index]

    st.session_state.score_a += 1

    st.session_state.history.append(
        {
            "question": question,
            "answer": question["a"]
        }
    )

    st.session_state.question_index += 1

    if (
        st.session_state.question_index
        >= len(GAME_DATA[category])
    ):
        st.session_state.finished = True


# ============================================
# B 선택
# ============================================

def select_b():

    category = st.session_state.category

    index = st.session_state.question_index

    question = GAME_DATA[category][index]

    st.session_state.score_b += 1

    st.session_state.history.append(
        {
            "question": question,
            "answer": question["b"]
        }
    )

    st.session_state.question_index += 1

    if (
        st.session_state.question_index
        >= len(GAME_DATA[category])
    ):
        st.session_state.finished = True


# ============================================
# 메인 제목
# ============================================

st.title("⚖️ 밸런스 게임")

st.write(
    "둘 중 하나만 선택할 수 있다면 무엇을 선택하시겠어요?"
)

st.divider()


# ============================================
# 카테고리
# ============================================

st.subheader("게임 종류")

categories = list(GAME_DATA.keys())

category_columns = st.columns(3)

for i, category in enumerate(categories):

    with category_columns[i]:

        st.button(
            category,
            key="category_button_" + str(i),
            use_container_width=True,
            on_click=reset_game,
            args=(category,)
        )


st.divider()


# ============================================
# 현재 게임 가져오기
# ============================================

category = st.session_state.category

questions = GAME_DATA[category]

index = st.session_state.question_index

total = len(questions)


# ============================================
# 결과 화면
# ============================================

if st.session_state.finished:

    st.success("🎉 게임이 끝났습니다!")

    st.header("🏆 나의 결과")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🔴 A 선택",
            st.session_state.score_a
        )

    with col2:

        st.metric(
            "🔵 B 선택",
            st.session_state.score_b
        )

    st.divider()

    if (
        st.session_state.score_a
        > st.session_state.score_b
    ):

        st.success(
            "🔴 A를 더 많이 선택했습니다!"
        )

    elif (
        st.session_state.score_b
        > st.session_state.score_a
    ):

        st.info(
            "🔵 B를 더 많이 선택했습니다!"
        )

    else:

        st.warning(
            "⚖️ A와 B를 똑같이 선택했습니다!"
        )

    st.subheader("📋 나의 선택 기록")

    for i, item in enumerate(
        st.session_state.history
    ):

        st.write(
            str(i + 1)
            + ". "
            + item["question"]["a"]
            + "  VS  "
            + item["question"]["b"]
        )

        st.write(
            "👉 내가 선택: "
            + item["answer"]
        )

    st.divider()

    if st.button(
        "🔄 다시 하기",
        use_container_width=True
    ):

        reset_game(category)


# ============================================
# 게임 화면
# ============================================

else:

    question = questions[index]

    st.subheader(
        "Question "
        + str(index + 1)
        + " / "
        + str(total)
    )

    # 진행률
    progress = index / total

    st.progress(progress)

    st.write("")

    # ========================================
    # 선택 카드
    # ========================================

    left, middle, right = st.columns(
        [5, 1, 5]
    )

    with left:

        st.markdown("## 🔴 OPTION A")

        st.markdown(
            "# " + question["a"]
        )

    with middle:

        st.markdown("# VS")

    with right:

        st.markdown("## 🔵 OPTION B")

        st.markdown(
            "# " + question["b"]
        )

    st.write("")

    # ========================================
    # 선택 버튼
    # ========================================

    button_a, button_b = st.columns(2)

    with button_a:

        st.button(
            "🔴 A 선택",
            key="select_a_" + str(index),
            use_container_width=True,
            on_click=select_a
        )

    with button_b:

        st.button(
            "🔵 B 선택",
            key="select_b_" + str(index),
            use_container_width=True,
            on_click=select_b
        )


# ============================================
# 하단
# ============================================

st.divider()

st.caption(
    "⚖️ Balance Game"
)
