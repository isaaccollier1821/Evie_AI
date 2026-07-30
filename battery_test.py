import psutil

def get_battery_status(message):
    if "battery" in message or "power" in message or "charge" in message:
        battery = psutil.sensors_battery()

        if battery:
            status = "charging" if battery.power_plugged else "not charging"
            return f"Your battery is at {battery.percent}% and it is {status}."

        return "I can't access your battery information."

    return None