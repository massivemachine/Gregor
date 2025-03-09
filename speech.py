from playsound import playsound
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')

'''counter = 0
for voice in voices:
    print(voice)
    print(counter)
    counter += 1
    
engine.setProperty('voice', voices[1].id)
'''
engine.setProperty('voice', voices[1].id)


def play(text):
    engine.say(text)
    engine.runAndWait()


def bebe_high():
    playsound("assets/audio/bebe_high.mp3")


def bebe_low():
    playsound("assets/audio/bebe_low.mp3")


def chime():
    playsound("assets/audio/chime.mp3")


def milestone_chime():
    playsound("assets/audio/milestone_chime.mp3")


def rare_chime():
    playsound("assets/audio/rare_chime.mp3")


def quiz_intro():
    playsound("assets/audio/quiz_intro.mp3")


def correct_answer():
    playsound("assets/audio/correct_answer.mp3")


def wrong_answer():
    playsound("assets/audio/wrong_answer.mp")


def startup():
    engine.say("Hello!! My name is Gregor")
    engine.runAndWait()
    bebe_high()
