import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from speech import *

def detect_hand(imgPath):
    # assign settings to hand detector
    base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
    options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)

    # create detector
    detector = vision.HandLandmarker.create_from_options(options)

    #open image
    image = mp.Image.create_from_file(imgPath)
    # run detector on image
    detection_result = detector.detect(image)

    return detection_result

def get_pos(imgPath):
    lmList = []
    handLandmarks = detect_hand(imgPath).hand_landmarks
    # for every landmark in hand extract x, y
    for lm in handLandmarks[0]:
        lmList.append((lm.x, lm.y))
    # return list
    return lmList

def handedness(imgPath):
    return detect_hand(imgPath).handedness[0][0].category_name

def raised_fingers(imgPath):
    fingers = []
    pos = get_pos(imgPath)

    fingers.append(pos[4][1] < pos[3][1] and ((pos[4][0] > pos[5][0] and handedness(imgPath) == "Right") or
        (pos[4][0] < pos[5][0] and handedness(imgPath) == "Left")))
    fingers.append(pos[8][1] < pos[7][1] < pos[6][1])
    fingers.append(pos[12][1] < pos[11][1] < pos[10][1])
    fingers.append(pos[16][1] < pos[15][1] < pos[14][1])
    fingers.append(pos[20][1] < pos[19][1] < pos[18][1])

    return fingers

def detect_hello(imgPath):
    pos = get_pos(imgPath)
    if raised_fingers(imgPath) == [True, True, True, True, True]:
        return True
    return False

def detect_one(imgPath):
    if raised_fingers(imgPath) == [False, True, False, False, False]:
        return True
    return False

def detect_two(imgPath):
    if raised_fingers(imgPath) == [False, True, True, False, False]:
        return True
    return False

def detect_three(imgPath):
    if raised_fingers(imgPath) == [False, True, True, True, False]:
        return True
    return False

def detect_curled_fingers(imgPath):
    pos = get_pos(imgPath)
    if (handedness(imgPath) == "Right" and pos[8][0] < pos[5][0]
            and pos[12][0] < pos[9][0] and pos[16][0] < pos[13][0]
            and pos[20][0] < pos[17][0]) or (handedness(imgPath) == "Left"
            and pos[8][0] > pos[5][0] and pos[12][0] > pos[9][0]
            and pos[16][0] > pos[13][0] and pos[20][0] > pos[17][0]):
        return True
    return False

def detect_thumbs_up(imgPath):
    pos = get_pos(imgPath)
    if pos[4][1] < pos[3][1] and detect_curled_fingers(imgPath):
        return True
    return False

def detect_thumbs_down(imgPath):
    pos = get_pos(imgPath)
    if pos[4][1] > pos[3][1] and detect_curled_fingers(imgPath):
        return True
    return False

# main function to detect any valid hand actions
def detect_action(imgPath):
    if detect_hello(imgPath): return "hello"
    if detect_one(imgPath): return "one"
    if detect_two(imgPath): return "two"
    if detect_three(imgPath): return "three"
    if detect_thumbs_up(imgPath): return "thumbs_up"
    if detect_thumbs_down(imgPath): return "thumbs_down"
    return "unknown"