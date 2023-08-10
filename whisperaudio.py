# whisper audio 
import requests

with open("keys.txt", "r") as f:
    key = f.read()

API_URL = "https://p0oi0gtn7iyhoioj.us-east-1.aws.endpoints.huggingface.cloud/"
API_TOKEN = key
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "audio/mpeg"}

def get_text(file: str) -> str:
    return requests.post(API_URL, headers=headers, data = file).json()