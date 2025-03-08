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
    path_to_play = "/Users/panda/Documents/Uni/Computer Science/Competitions/Gregor/assets/audio/bebe_high.m4a"
    path_to_play = path_to_play.replace(" ", "%20")
    playsound(path_to_play)


def bebe_low():
    path_to_play = "/Users/panda/Documents/Uni/Computer Science/Competitions/Gregor/assets/audio/bebe_low.m4a"
    path_to_play = path_to_play.replace(" ", "%20")
    playsound(path_to_play)


def startup():
    engine.say("Hello!! My name is Gregor")
    engine.runAndWait()
    bebe_high()
