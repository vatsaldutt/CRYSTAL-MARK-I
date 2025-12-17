import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

prev_x, prev_y = None, None


def detect_hand_gestures(frame):
    global prev_x, prev_y

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if not results.multi_hand_landmarks:
        prev_x, prev_y = None, None
        return None

    hand = results.multi_hand_landmarks[0]
    mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    tip = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    x, y = tip.x, tip.y

    gesture = None

    if prev_x is not None:
        dx = x - prev_x
        dy = y - prev_y

        threshold = 0.02  # normalized coords

        if abs(dx) > abs(dy):
            if dx > threshold:
                gesture = "Swipe Right"
            elif dx < -threshold:
                gesture = "Swipe Left"
        else:
            if dy > threshold:
                gesture = "Swipe Down"
            elif dy < -threshold:
                gesture = "Swipe Up"

    prev_x, prev_y = x, y
    return gesture


# ---------------- MAIN ---------------- #

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gesture = detect_hand_gestures(frame)

    if gesture:
        cv2.putText(frame, gesture, (40, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
