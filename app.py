import streamlit as st

# 🎶 장르 목록 (확장 포함)
genres = [
    "Rock", "Ballad", "Pop", "HipHop", "Jazz", "Trot", "EDM",
    "Classical", "R&B", "Blues", "CountryFolk", "Reggae", "Disco",
    "Electronic", "House", "Trance", "Ambient", "TripHop",
    "Punk", "Grunge", "NewAge", "Gospel", "WorldMusic"
]

# 🎹 Suno 프롬프트 (예시 텍스트)
suno_prompts = {g: f"{g} 1시간 프롬프트 텍스트..." for g in genres}

# 📺 설명문 (예시 텍스트)
descriptions = {g: f"{g} 유튜브 설명문..." for g in genres}

# 🖼️ 이미지 프롬프트 (예시 텍스트)
image_prompts = {g: f"Nanobanana style realistic {g} scene..." for g in genres}

# 🎶 Streamlit UI
st.title("🎶 AI 음악 자동화 워크플로우 (Streamlit UI)")
genre = st.selectbox("장르 선택", genres, index=6)  # 기본값 EDM

st.subheader("🎹 Suno 프롬프트")
st.text_area("Suno 프롬프트", suno_prompts[genre], height=150)

st.subheader("📺 유튜브 설명문")
st.text_area("유튜브 설명문", descriptions[genre], height=150)

st.subheader("🎨 이미지 프롬프트")
st.text_area("이미지 프롬프트", image_prompts[genre], height=100)
