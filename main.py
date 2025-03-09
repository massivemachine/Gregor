from plant_detection import *
import hand_detection
import subprocess
from time import sleep

plantScan = False

startup()
while True:
	subprocess.run(["libcamera-still","-o","assets/gregors_view.png"])

	if plantScan:
		identify_plant("assets/gregors_view.png")
		plantScan = False
	else:
		action = hand_detection.detect_action_reduced("assets/gregors_view.png")
		print(action)
		if action == "thumbs up":
			play("scanning for plants")
			plantScan = True
		elif action == "hello":
			play("hello friend")
			bebe_low()

