import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🌸 파스텔 톤 한국군 사령관 시나리오 시스템", layout="wide")

# CSS 커스터마이징 (파스텔 톤)
st.markdown("""
    <style>
    body { background-color: #fdf6f6; }
    .stButton>button { background-color: #a8dadc; color: #1d3557; border-radius: 8px; }
    .stTextInput>div>input, .stTextArea>div>textarea, .stSelectbox>div>div>select {
        background-color: #f1faee; border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# 시나리오 저장용
if "scenes" not in st.session_state:
    st.session_state["scenes"] = []

# 사이드바 메뉴
st.sidebar.title("📂 메뉴")
menu = st.sidebar.radio("기능 선택", [
    "시나리오 입력",
    "영상 생성 (6:4)",
    "이미지 생성 (한국군 사령관)",
    "SEO 패키지",
    "결과 다운로드"
])

# 시나리오 입력
if menu == "시나리오 입력":
    scene_num = st.number_input("장면 번호", min_value=1, max_value=100, value=1)
    situation = st.text_input("상황 요약", value="적의 기습에 대응하는 지휘관")
    dialogue = st.text_input("대사", value="전군, 사격하라!")
    asset = st.selectbox("화력 자산", [
        "K2 Black Panther", "Apache", "K9 Thunder", "Drone Swarm", "천무", "전투기", "이즈스함"
    ])
    if st.button("장면 추가"):
        st.session_state["scenes"].append({
            "scene_num": scene_num,
            "situation": situation,
            "dialogue": dialogue,
            "asset": asset
        })
        st.success(f"Scene {scene_num} 추가 완료!")
    st.json(st.session_state["scenes"])

# 영상 생성
elif menu == "영상 생성 (6:4)":
    st.write("🎬 6:4 시나리오 자동 생성")
    for scene in st.session_state["scenes"]:
        st.write(f"**Scene {scene['scene_num']}**")
        st.write(f"- 상황: {scene['situation']}")
        st.write("**VIDEO & AUDIO PROMPT:**")
        st.write("- [마스터 고정값: Seedance 2.0 캐릭터 일관성 유지]")
        st.write("- (6초: 입술 은폐 구도 및 안면 연기, 시네마틱 톤)")
        st.write(f"- [오디오: 한국군 사령관의 목소리로 \"{scene['dialogue']}\" 비장하게 발화]")
        st.write("- (대사 리듬에 맞춘 격렬한 하얀 입김 묘사)")
        st.write(f"- (4초: {scene['asset']}의 하이퍼 리얼리즘 액션)")
        st.write("- [배경음: 엔진음 및 폭발음]")

# 이미지 생성
elif menu == "이미지 생성 (한국군 사령관)":
    st.write("🎨 한국군 사령관 실사화 프롬프트")
    prompt = """실사풍 인물 사진, 한국군 사령관,
영화적 조명, 일관된 얼굴 특징,
전투 상황에 어울리는 표정,
시네마틱 톤, 하이퍼 리얼리즘 디테일,
강렬한 감정 표현과 드라마틱 배경"""
    st.text_area("영상 제작용 프롬프트", prompt, height=200)
    st.success("✅ 한국군 사령관 실사화 프롬프트 준비 완료!")

# SEO 패키지
elif menu == "SEO 패키지":
    st.write("📊 유튜브 최적화 패키지")
    st.write("제목: AI 타임슬립 대서사시 🎬")
    st.write("썸네일 문구: '사격하라!'")
    st.write("""설명문: 한국군 사령관이 적의 기습에 맞서 전군을 지휘하는 장엄한 순간을 담아낸 AI 타임슬립 대서사시입니다.
실사풍 전투 장면과 하이퍼 리얼리즘 액션, 비장한 대사와 격렬한 입김 묘사,
K2 전차·Apache 헬기·K9 자주포·드론 스웜·천무·전투기·이즈스함 등 다양한 무기 자산의 등장으로 긴장감과 웅장함을 전달합니다.
SEO 최적화를 통해 더 많은 시청자들이 이 작품을 발견할 수 있도록 구성되었습니다.""")
    st.write("해시태그: #AI영상 #타임슬립 #국군서사시 #자동화 #유튜브성공")
    st.write("검색 태그: 국군, 타임슬립, AI영상, 전투, 서사시")

# 결과 다운로드
elif menu == "결과 다운로드":
    if st.session_state["scenes"]:
        content = "=== 시나리오 ===\n"
        for scene in st.session_state["scenes"]:
            content += f"Scene {scene['scene_num']} - 상황: {scene['situation']} - 대사: {scene['dialogue']} - 자산: {scene['asset']}\n"
        content += "\n=== 이미지 프롬프트 ===\n"
        content += """실사풍 인물 사진, 한국군 사령관,
영화적 조명, 일관된 얼굴 특징,
전투 상황에 어울리는 표정,
시네마틱 톤, 하이퍼 리얼리즘 디테일,
강렬한 감정 표현과 드라마틱 배경"""
        content += "\n\n=== SEO 설명문 ===\n"
        content += """한국군 사령관이 적의 기습에 맞서 전군을 지휘하는 장엄한 순간을 담아낸 AI 타임슬립 대서사시입니다.
실사풍 전투 장면과 하이퍼 리얼리즘 액션, 비장한 대사와 격렬한 입김 묘사,
K2 전차·Apache 헬기·K9 자주포·드론 스웜·천무·전투기·이즈스함 등 다양한 무기 자산의 등장으로 긴장감과 웅장함을 전달합니다."""

        st.download_button(
            label="📥 결과 다운로드",
            data=content,
            file_name="output.txt",
            mime="text/plain"
        )
    else:
        st.warning("⚠️ 먼저 시나리오를 입력해 주세요!")
