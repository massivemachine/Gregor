from plant_detection import *
import hand_detection
import subprocess
from time import sleep

plantScan = False
quizTime = False
solution = ""

startup()

while True:
	subprocess.run(["libcamera-still","-o","assets/gregors_view.png"])

	if plantScan:
		num = identify_plant("assets/gregors_view.png")
		if num == 1:
			quizTime = True
			solution = ask_question()
		elif num == 2:
			play("Unable to detect plant")
		plantScan = False

	elif quizTime:
		action = hand_detection.detect_action_quiz("assets/gregors_view.png")

		if (solution == "true" and action == "thumbs up") or (solution == "false" and action == "thumbs down"):
			correct_answer()
			play("Great work! You got it right!")
			quizTime = False
		elif action == "thumbs up" or action == "thumbs down":
			wrong_answer()
			play("Not quite, it was actually " + solution + ", you'll get it next time!")
			quizTime = False

	else:
		action = hand_detection.detect_action_main("assets/gregors_view.png")
		print(action)

		if action == "thumbs up":
			play("scanning for plants")
			plantScan = True
		elif action == "hello":
			play("hello friend")
			bebe_low()