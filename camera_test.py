from picamera2 import Picamera2, Preview
from time import sleep

cam = Picamera2()
cam.configure("video")
cam.start_preview(Preview.QTGL)
cam.start()

def take_photo(camera):
    camera.capture_file("img.jpg")
    sleep(1)


try:
    while True:
        take_photo(cam)
finally:
    cam.stop()

