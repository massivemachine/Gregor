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
    playsound("assets/audio/bebe_high.mp3")


def bebe_low():
    playsound("assets/audio/bebe_low.mp3")


def chime():
    subprocess.run(["pw-play","assets/audio/chime.mp3"])


def milestone_chime():
    playsound("assets/audio/milestone_chime.mp3")


def rare_chime():
    subprocess.run(["pw-play","assets/audio/rare_chime.mp3"])


def startup():
    engine.say("Hello My name is Gregor")
    engine.runAndWait()
    bebe_high()
