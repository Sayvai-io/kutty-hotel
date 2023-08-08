import gradio as gr
import numpy as np
from scipy.io.wavfile import write
import assemblyai as aai


# def get_text(path: str) -> str:
#     with open("keys.txt") as f:
#       key = f.read()
#     aai.settings.api_key = key
#     transcriber = aai.Transcriber()
#     transcript = transcriber.transcribe(path)
#     return transcript.text

def get_text(path: str) -> str:
    return "Hello World"

gr.Interface(
    fn=get_text, 
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs="text").launch()