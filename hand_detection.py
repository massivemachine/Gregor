import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


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

def get_pos(hand):
    lmList = []
    handLandmarks = hand.hand_landmarks
    # for every landmark in hand extract x, y
    for lm in handLandmarks[0]:
        lmList.append((lm.x, lm.y))
    # return list
    return lmList

def handedness(hand):
    return hand.handedness[0][0].category_name

def raised_fingers(pos, hand):
    fingers = [pos[4][1] < pos[3][1] and ((pos[4][0] > pos[5][0] and
            handedness(hand) == "Right") or (pos[4][0] < pos[5][0] and
            handedness(hand) == "Left")), pos[8][1] < pos[7][1] < pos[6][1],
            pos[12][1] < pos[11][1] < pos[10][1], pos[16][1] < pos[15][1] < pos[14][1],
            pos[20][1] < pos[19][1] < pos[18][1]]
    return fingers

def detect_hello(pos, hand):
    if raised_fingers(pos, hand) == [True, True, True, True, True]:
        return True
    return False

def detect_one(pos, hand):
    if raised_fingers(pos, hand) == [False, True, False, False, False]:
        return True
    return False

def detect_two(pos, hand):
    if raised_fingers(pos, hand) == [False, True, True, False, False]:
        return True
    return False

def detect_three(pos, hand):
    if raised_fingers(pos, hand) == [False, True, True, True, False]:
        return True
    return False

def detect_curled_fingers(pos, hand):
    if (handedness(hand) == "Right" and pos[8][0] < pos[6][0]
            and pos[12][0] < pos[10][0] and pos[16][0] < pos[14][0]
            and pos[20][0] < pos[18][0]) or (handedness(hand) == "Left"
            and pos[8][0] > pos[6][0] and pos[12][0] > pos[10][0]
            and pos[16][0] > pos[14][0] and pos[20][0] > pos[18][0]):
        return True
    return False

def detect_thumbs_up(pos, hand):
    if pos[4][1] < pos[3][1] and detect_curled_fingers(pos, hand):
        return True
    return False

def detect_thumbs_down(pos, hand):
    if pos[4][1] > pos[3][1] and detect_curled_fingers(pos, hand):
        return True
    return False

# main function to detect any valid hand actions
def detect_action_reduced(imgPath):
    hand = detect_hand(imgPath)
    pos = get_pos(hand)

    if not detect_hand(imgPath).hand_landmarks: return ""
    if detect_hello(pos, hand): return "hello"
    if detect_thumbs_up(pos, hand): return "thumbs up"
    return "unknown gesture"

# main function to detect any valid hand actions
def detect_action(imgPath):
    hand = detect_hand(imgPath)
    pos = get_pos(hand)

    if not hand.hand_landmarks: return ""
    if detect_hello(pos, hand): return "hello"
    if detect_one(pos, hand): return "option one"
    if detect_two(pos, hand): return "option two"
    if detect_three(pos, hand): return "option three"

    if detect_thumbs_up(pos, hand): return "thumbs up"
    if detect_thumbs_down(pos, hand): return "thumbs down"
    return "unknown gesture"