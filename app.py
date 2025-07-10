import streamlit as st
import requests

st.set_page_config(page_title="Transcritor da Equipe Eduardo, Jane e Luana")

st.title("🎙️ Transcritor de Áudio e Vídeo")
st.write("Envie um áudio ou vídeo em português e receba a transcrição exata com Whisper (via Gooey AI).")

uploaded_file = st.file_uploader("Escolha um arquivo de áudio ou vídeo (.mp3, .mp4, .wav)", type=["mp3", "mp4", "wav"])

if uploaded_file is not None:
    with st.spinner("Transcrevendo... isso pode levar um momento."):
        API_URL = "https://whisper.gooey.ai/api/v1/transcribe/"
        API_KEY = "demo"  # Você pode obter uma gratuita em https://whisper.gooey.ai

        files = {"file": uploaded_file}
        headers = {"Authorization": f"Bearer {API_KEY}"}
        data = {"diarize": "false"}

        response = requests.post(API_URL, headers=headers, files=files, data=data)

        if response.ok:
            result = response.json()
            st.success("✅ Transcrição concluída!")
            st.text_area("📝 Transcrição:", result["text"], height=300)
        else:
            st.error(f"Erro na transcrição: {response.text}")