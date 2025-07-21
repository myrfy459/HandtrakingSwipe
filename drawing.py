import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, max_num_hands=1)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)
prev_x, prev_y = 0, 0

def jari_telunjuk_terangkat(landmarks):
    return landmarks.landmark[8].y < landmarks.landmark[6].y

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if jari_telunjuk_terangkat(hand_landmarks):
                h, w, _ = frame.shape
                x = int(hand_landmarks.landmark[8].x * w)
                y = int(hand_landmarks.landmark[8].y * h)

                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y

                cv2.line(canvas, (prev_x, prev_y), (x, y), (255, 0, 255), 5)
                prev_x, prev_y = x, y
            else:
                prev_x, prev_y = 0, 0

    combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow("Air Drawing", combined)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('c'):
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)

cap.release()
cv2.destroyAllWindows()
