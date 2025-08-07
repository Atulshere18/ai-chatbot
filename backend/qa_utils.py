# backend/qa_utils.py
import requests
import os

API_URL = os.getenv("HF_API_URL")  # Keep secret in .env
HF_TOKEN = os.getenv("HF_TOKEN")   # Keep token secret

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_answer(context, question):
    payload = {
        "inputs": {
            "question": question,
            "context": context
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()['answer']
    except Exception as e:
        return f"Error: {e}\nRaw response: {response.text}"
