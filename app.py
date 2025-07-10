import gradio as gr
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # ou substitua diretamente: openai.api_key = "sua-chave-aqui"

def transcrever(audio_path):
    if audio_path is None:
        return "Nenhum arquivo enviado."

    try:
        with open(audio_path, "rb") as f:
            response = openai.Audio.transcribe("whisper-1", f, language="pt")
            return response["text"]
    except Exception as e:
        return f"Erro: {e}"

gr.Interface(
    fn=transcrever,
    inputs=gr.Audio(source="upload", type="filepath"),
    outputs="text",
    title="Transcritor com OpenAI Whisper",
    description="Transcreve áudios e vídeos usando a API oficial da OpenAI (Whisper)"
).launch()

