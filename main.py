from plant_detection import *
import subprocess
from time import sleep

startup()
subprocess.run(["libcamera-still","-o","assets/gregors_view.png"])

identify_plant("assets/gregors_view.png")
