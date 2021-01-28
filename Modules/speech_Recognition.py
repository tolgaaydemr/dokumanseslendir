import speech_recognition as sr
from gtts import gTTS
import os


def speak(audioString):
    tts = gTTS(text=audioString, lang="tr")
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")


def speech_R():
    # Text to Speech Method
    r = sr.Recognizer()
    with sr.Microphone() as source:  # use the default microphone as the audio source
        # print("Ortam dinleniyor...")
        # listen for 5 seconds and create the ambient noise energy level
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("Şimdi Konuşabilirsin")
        audio = r.listen(source)  # listen for the first phrase and extract it into audio data
    try:
        print("Söylediklerin: " + r.recognize_google(audio, language='tr-tr'))
        # recognize speech using Google Speech Recognition
        reco_Text = r.recognize_google(audio, language='tr-tr')
    except LookupError:  # speech is unintelligible
        print("Üzgünüm. Seni anlayamadım.")
    return reco_Text
