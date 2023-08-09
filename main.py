# gradio app 
# import requests
# import gradio as gr
# from llm import Server


# API_URL = "https://api-inference.huggingface.co/models/openai/whisper-medium"
# API_TOKEN = ""
# headers = {"Authorization": f"Bearer {API_TOKEN}"}


# def get_text(file: str) -> str:
#     response = requests.post(API_URL, headers=headers, json={"inputs": file})
#     return response.json()
    


# # server = Server()
# # server.load_pinecone()
# gr.Interface(
# fn=get_text, 
# inputs=gr.Audio(source="microphone", type="filepath"),
# outputs="text").launch()
