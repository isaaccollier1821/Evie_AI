import psutil

def get_battery_status(message):
    if "battery" in message.lower() or "power" in message.lower() or "charge" in message.lower():
        battery = psutil.sensors_battery()

        if battery:
            status = "charging" if battery.power_plugged else "not charging"
            return f"Your battery is at {battery.percent}% and it is {status}."

        return "I can't access your battery information."

    return None