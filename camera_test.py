import subprocess
from time import sleep

input("this script takes photos, press enter to continue")

def take_photo():
    subprocess.run(["libcamera-still","-o","img.jpg"])

while True:
    take_photo()
    sleep(1)

