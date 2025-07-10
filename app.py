import gradio as gr
import openai
import tempfile
import numpy as np
import scipy.io.wavfile

openai.api_key = "SUA_CHAVE_AQUI"  # Substitua por sua chave da OpenAI

def transcrever(audio):
    if audio is None:
        return "Nenhum áudio enviado."

    try:
        sample_rate, audio_data = audio
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            scipy.io.wavfile.write(tmp.name, sample_rate, (audio_data * 32767).astype(np.int16))
            tmp.flush()
            with open(tmp.name, "rb") as f:
                result = openai.Audio.transcribe("whisper-1", f, language="pt")
                return result["text"]
    except Exception as e:
        return f"Erro ao transcrever: {e}"

gr.Interface(
    fn=transcrever,
    inputs=gr.Audio(source="upload", type="numpy"),
    outputs="text",
    title="Transcritor OpenAI Whisper",
    description="Transcreve áudio em português com a API oficial da OpenAI (modelo Whisper)."
).launch()