import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import numpy as np


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():

    recognizer = sr.Recognizer()

    print("Listening...")

    sample_rate = 16000
    duration = 5

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    audio_data = sr.AudioData(
        audio.tobytes(),
        sample_rate,
        2
    )

    try:
        text = recognizer.recognize_google(audio_data)
        print("You:", text)
        return text

    except:
        return ""