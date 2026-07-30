from battery import get_battery_status
import pyautogui


def run_system_command(message):

    battery_response = get_battery_status(message)

    if battery_response:
        return battery_response


    if "screenshot" in message.lower():

        screenshot = pyautogui.screenshot()

        screenshot.save("evie_screenshot.png")

        return "Screenshot saved."

    return None