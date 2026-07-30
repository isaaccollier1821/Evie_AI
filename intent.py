def detect_intent(message):

    message = message.lower()

    if any(word in message for word in [
        "battery",
        "charge",
        "power"
    ]):
        return "battery"

    if any(word in message for word in [
        "screenshot",
        "screen capture"
    ]):
        return "screenshot"

    if "open" in message:
        return "open_app"

    return "chat"