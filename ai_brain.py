import requests
from personality import personality


def ask_evie(message):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1",
            "prompt": personality + "\nUser: " + message,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]

