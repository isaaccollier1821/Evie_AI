from memory import save_memory


def detect_memory(message):

    message = message.lower()

    if "my favourite game is" in message:
        value = message.replace("my favourite game is", "").strip()
        save_memory("favourite_game", value)
        return f"I'll remember that your favourite game is {value}."

    elif "i like" in message:
        value = message.replace("i like", "").strip()
        save_memory("likes", value)
        return f"I'll remember that you like {value}."

    elif "i am learning" in message:
        value = message.replace("i am learning", "").strip()
        save_memory("learning", value)
        return f"I'll remember that you are learning {value}."

    elif "my project is" in message:
        value = message.replace("my project is", "").strip()
        save_memory("project", value)
        return f"I'll remember that your project is {value}."

    return None