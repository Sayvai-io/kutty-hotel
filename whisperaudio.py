# whisper audio 
import requests

with open("keys.txt", "r") as f:
    key = f.read()

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-medium"
API_TOKEN = key
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def get_text(file: str) -> str:
    return requests.post(API_URL, headers=headers, data = file).json()