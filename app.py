import gradio as gr

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

# 🎶 실행 함수
def generate_content(genre):
    return (
        f"🎶 Suno 프롬프트:\n{suno_prompts[genre]}",
        f"📺 유튜브 설명문:\n{descriptions[genre]}",
        f"🎨 이미지 프롬프트:\n{image_prompts[genre]}"
    )

# 🌸 Gradio 인터페이스 (파스텔 톤 테마)
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🎶 AI 음악 자동화 워크플로우 (파스텔 UI)")
    genre_dropdown = gr.Dropdown(choices=genres, value="EDM", label="장르 선택")
    suno_output = gr.Textbox(label="Suno 프롬프트", lines=10)
    desc_output = gr.Textbox(label="유튜브 설명문", lines=10)
    img_output = gr.Textbox(label="이미지 프롬프트", lines=5)

    genre_dropdown.change(generate_content, inputs=genre_dropdown, outputs=[suno_output, desc_output, img_output])

demo.launch()
