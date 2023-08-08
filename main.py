import gradio as gr
import numpy as np
from scipy.io.wavfile import write
import assemblyai as aai


def get_text(path: str) -> str:
    return "Hello World"

gr.Interface(
    fn=get_text, 
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs="text").launch()