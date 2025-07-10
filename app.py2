import gradio as gr
import requests

API_URL = "https://whisper.gooey.ai/api/v1/transcribe/"
API_KEY = "demo"  # Para uso mais intensivo, crie sua chave em https://whisper.gooey.ai

def transcribe_with_whisper(audio_file):
    if audio_file is None:
        return "Nenhum arquivo enviado."

    files = {'file': audio_file}
    headers = {'Authorization': f'Bearer {API_KEY}'}
    data = {'diarize': 'false'}

    response = requests.post(API_URL, headers=headers, files=files, data=data)
    if response.ok:
        return response.json()["text"]
    else:
        return f"Erro: {response.text}"

gr.Interface(
    fn=transcribe_with_whisper,
    inputs=gr.Audio(source="upload", type="file"),  # <<< ALTERADO aqui!
    outputs="text",
    title="Transcritor Inteligente",
    description="WebApp da equipe Eduardo, Jane e Luana. Envie um vídeo ou áudio em português e receba a transcrição exata."
).launch()
