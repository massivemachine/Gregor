from plant_detection import *
import hand_detection
import subprocess
from time import sleep

startup()
while True:
	subprocess.run(["libcamera-still","-o","assets/gregors_view.png"])

	play(hand_detection.detect_action("assets/gregors_view.png"))

#identify_plant("assets/gregors_view.png")
