import sounddevice as sd
import speech_recognition as sr


def wait_for_wake_word():

    recognizer = sr.Recognizer()

    while True:
        print("Waiting for 'Hey Evie'...")

        sample_rate = 16000
        duration = 5

        audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16",
    device=1
)

        sd.wait()

        audio_data = sr.AudioData(
            audio.tobytes(),
            sample_rate,
            2
        )

        try:
            text = recognizer.recognize_google(audio_data).lower()

            print("Heard:", text)

            if (
                "hey evie" in text
                or "hey eevee" in text
                or "evie" in text
                or "eevee" in text
            ):
                return True

        except Exception:
            pass