import gradio as gr
import openai
import tempfile
import numpy as np
import scipy.io.wavfile

openai.api_key = "SUA_CHAVE_AQUI"  # ou use openai.api_key = os.getenv("OPENAI_API_KEY")

def transcrever(audio_np_tuple):
    if audio_np_tuple is None:
        return "Nenhum áudio enviado."

    sample_rate, audio_data = audio_np_tuple
    try:
        # Criar um arquivo temporário WAV
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            scipy.io.wavfile.write(tmp.name, sample_rate, audio_data.astype(np.int16))
            tmp.flush()

            with open(tmp.name, "rb") as f:
                response = openai.Audio.transcribe("whisper-1", f, language="pt")
                return response["text"]
    except Exception as e:
        return f"Erro: {e}"

gr.Interface(
    fn=transcrever,
    inputs=gr.Audio(source="upload", type="numpy"),
    outputs="text",
    title="Transcritor OpenAI Whisper",
    description="Envie um áudio (MP3, WAV) e veja a transcrição."
).launch()
