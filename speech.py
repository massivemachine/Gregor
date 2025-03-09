import pyttsx3
import subprocess
from time import sleep

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
    sleep(1)
    subprocess.run(["pw-play","assets/audio/bebe_high.mp3"])


def bebe_low():
    #sleep(1)
    subprocess.run(["pw-play","assets/audio/bebe_low.mp3"])


def chime():
    sleep(1)
    subprocess.run(["pw-play","assets/audio/chime.mp3"])


def milestone_chime():
    sleep(1)
    subprocess.run(["pw-play","assets/audio/milestone_chime.mp3"])


def rare_chime():
    sleep(1)
    subprocess.run(["pw-play","assets/audio/rare_chime.mp3"])


def quiz_intro():
    subprocess.run("assets/audio/quiz_intro.mp3")


def correct_answer():
    subprocess.run("assets/audio/correct_answer.mp3")


def wrong_answer():
    subprocess.run("assets/audio/wrong_answer.mp")


def startup():
    engine.say("Hello My name is Gregor")
    engine.runAndWait()
    sleep(1)
    bebe_high()
