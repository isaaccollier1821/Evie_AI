from personality import evie_name
from memory import save_memory, load_memory
from ai_brain import ask_evie
from memory_manager import detect_memory
from voice import speak, listen

speak(f"Hello! I am Evie. How can I help?")

while True:
    user = listen()
    memory_response = detect_memory(user)

    if memory_response:
        print("Evie:", memory_response)
        continue

    if user.lower() == "exit":
        print("Evie: Goodbye!")
        break

    elif user.lower().startswith("remember"):
        information = user.lower().replace("remember", "", 1).strip()

        if " is " in information:
            key, value = information.split(" is ", 1)

            save_memory(key.strip(), value.strip())

            print(f"Evie: I'll remember that {key.strip()} is {value.strip()}.")

        else:
            print("Evie: Try saying 'remember my favourite game is Cyberpunk'.")

    elif "what is my name" in user.lower() or "what's my name" in user.lower():
        memory = load_memory()

        if "user_name" in memory:
            print(f"Evie: Your name is {memory['user_name']}.")
        else:
            print("Evie: I don't know your name yet.")

    elif "what do you remember" in user.lower():
        memory = load_memory()

        print("Evie: I remember:")

        for key, value in memory.items():
            print(f"- {key}: {value}")

    elif "what is my" in user.lower():
        memory = load_memory()

        found = False

        for key, value in memory.items():
            if key in user.lower():
                print(f"Evie: Your {key} is {value}.")
                found = True

        if not found:
            print("Evie: I don't remember that yet.")

    else:
     memory = load_memory()

    memory_context = "Known information about the user:\n"

    for key, value in memory.items():
        memory_context += f"- {key}: {value}\n"

    response = ask_evie(memory_context + "\nUser: " + user)

    speak(response)