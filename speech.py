from playsound import playsound
import pyttsx3
import subprocess

engine = pyttsx3.init()
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')

'''counter = 0
for voice in voices:
    print(voice)
    print(counter)
    counter += 1
    
engine.setProperty('voice', voices[1].id)
'''
engine.setProperty('voice', voices[2].id)


def play(text):
    engine.say(text)
    engine.runAndWait()


def bebe_high():
    playsound("assets/audio/bebe_high.m4a")


def bebe_low():
    playsound("assets/audio/bebe_low.m4a")


def chime():
    subprocess.run(["pw-play","assets/audio/chime.mp3"])


def rare_chime():
    subprocess.run(["pw-play","assets/audio/rare_chime.mp3"])


def startup():
    engine.say("Hello My name is Gregor")
    engine.runAndWait()
    bebe_high()
