import streamlit as st
import requests

st.set_page_config(page_title="Transcritor da Equipe Eduardo, Jane e Luana")
st.title("🎙️ Transcritor de Áudio e Vídeo")

st.write("Envie um áudio ou vídeo curto (máx. 25 MB) e receba a transcrição em português.")

uploaded_file = st.file_uploader("Escolha o arquivo (.mp3, .wav, .mp4)", type=["mp3", "wav", "mp4"])

if uploaded_file is not None:
    if uploaded_file.size > 25 * 1024 * 1024:
        st.error("❌ O arquivo é muito grande. Envie um arquivo de até 25 MB.")
    else:
        with st.spinner("Transcrevendo..."):
            API_URL = "https://whisper.gooey.ai/api/v1/transcribe/"
            API_KEY = "demo"  # Substitua pela sua chave

            try:
                files = {"file": uploaded_file}
                headers = {"Authorization": f"Bearer {API_KEY}"}
                data = {"diarize": "false"}

                response = requests.post(API_URL, headers=headers, files=files, data=data, timeout=120)

                if response.ok:
                    result = response.json()
                    st.success("✅ Transcrição completa!")
                    st.text_area("📝 Texto:", result["text"], height=300)
                else:
                    st.error(f"Erro da API: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Erro de conexão: {str(e)}")
