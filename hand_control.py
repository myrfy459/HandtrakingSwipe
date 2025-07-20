import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)

prev_gesture = None

def detect_fingers(hand_landmarks):
    tips_ids = [8, 12, 16, 20]
    fingers = []

    for tip_id in tips_ids:
        is_up = hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y
        fingers.append(1 if is_up else 0)

    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    current_gesture = None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingers = detect_fingers(hand_landmarks)

            if fingers == [1, 0, 0, 0]:
                current_gesture = "left"
            elif fingers == [1, 1, 0, 0]:
                current_gesture = "right"
            elif fingers == [1, 1, 1, 0]:
                current_gesture = "up"
            elif fingers == [1, 1, 1, 1]:
                current_gesture = "down"

            if current_gesture and current_gesture != prev_gesture:
                pyautogui.press(current_gesture)
                prev_gesture = current_gesture
                cv2.putText(frame, f"Swipe {current_gesture.upper()}", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        prev_gesture = None

    preview = cv2.resize(frame, (640, 350))
    cv2.imshow("Hand Swipe Control", preview)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
