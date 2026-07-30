import json


def save_memory(key, value):
    with open("data/memory.json", "r") as file:
        memory = json.load(file)

    memory[key] = value

    with open("data/memory.json", "w") as file:
        json.dump(memory, file, indent=4)


def load_memory():
    with open("data/memory.json", "r") as file:
        return json.load(file)