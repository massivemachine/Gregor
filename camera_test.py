from picamera2 import Picamera2, Preview
from time import sleep

cam = Picamera2()
cam.configure("video")
cam.start_preview(Preview.QTGL)
cam.start()

try:
    while True:
        sleep(2)
        cam.capture_file("img.jpg")
finally:
    cam.stop()

