import subprocess


apps = {
    "calculator": "calc",
    "notepad": "notepad",
    "files": "explorer",
    "chrome": "chrome",
    "vscode": "code",
}


def run_command(message):

    message = message.lower()

    for app, command in apps.items():

        if app in message:

            subprocess.Popen(command)

            return f"Opening {app}."

    return None