import cv2
import dlib
import numpy as np
from collections import deque

# ---------------- CONFIG ---------------- #

PREDICTOR_PATH = "./models/shape_predictor_68_face_landmarks.dat"

LEFT_EYE_IDX  = [36, 37, 38, 39, 40, 41]
RIGHT_EYE_IDX = [42, 43, 44, 45, 46, 47]

SMOOTHING_WINDOW = 5
LEFT_THRESHOLD   = 0.75
RIGHT_THRESHOLD  = 1.25

FONT = cv2.FONT_HERSHEY_SIMPLEX

# ---------------------------------------- #


class GazeTracker:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(PREDICTOR_PATH)
        self.ratio_history = deque(maxlen=SMOOTHING_WINDOW)
        self.last_ratio = None

    def process(self, frame, debug=False):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)

        if not faces:
            return None, None

        face = faces[0]
        landmarks = self.predictor(gray, face)

        left_ratio  = self._eye_ratio(LEFT_EYE_IDX, landmarks, gray, frame, debug)
        right_ratio = self._eye_ratio(RIGHT_EYE_IDX, landmarks, gray, frame, debug)

        if left_ratio is None or right_ratio is None:
            return "closed", None

        gaze_ratio = (left_ratio + right_ratio) / 2.0
        self.last_ratio = gaze_ratio
        self.ratio_history.append(gaze_ratio)

        avg_ratio = np.mean(self.ratio_history)
        return self._classify(avg_ratio), avg_ratio

    def _classify(self, ratio):
        if ratio < LEFT_THRESHOLD:
            return "left"
        elif ratio > RIGHT_THRESHOLD:
            return "right"
        else:
            return "center"

    def _eye_ratio(self, eye_idx, landmarks, gray, frame, debug):
        pts = np.array(
            [(landmarks.part(i).x, landmarks.part(i).y) for i in eye_idx],
            dtype=np.int32
        )

        mask = np.zeros_like(gray)
        cv2.fillPoly(mask, [pts], 255)
        eye = cv2.bitwise_and(gray, gray, mask=mask)

        x0, x1 = np.min(pts[:, 0]), np.max(pts[:, 0])
        y0, y1 = np.min(pts[:, 1]), np.max(pts[:, 1])

        if x1 <= x0 or y1 <= y0:
            return None

        crop = eye[y0:y1, x0:x1]
        _, thresh = cv2.threshold(crop, 70, 255, cv2.THRESH_BINARY)

        h, w = thresh.shape
        left_white  = cv2.countNonZero(thresh[:, :w // 2])
        right_white = cv2.countNonZero(thresh[:, w // 2:])

        ratio = left_white / (right_white + 1e-6)

        if debug:
            self._draw_debug(frame, pts, x0, x1, y0, y1, left_white, right_white)

        return ratio

    def _draw_debug(self, frame, pts, x0, x1, y0, y1, lw, rw):
        cv2.polylines(frame, [pts], True, (0, 255, 255), 1)
        cx = (x0 + x1) // 2
        cv2.line(frame, (cx, y0), (cx, y1), (255, 0, 0), 1)
        cv2.putText(frame, f"L:{lw}", (x0, y0 - 5), FONT, 0.4, (255, 0, 0), 1)
        cv2.putText(frame, f"R:{rw}", (x1 - 40, y0 - 5), FONT, 0.4, (0, 255, 0), 1)


# ---------------- UI LAYOUT ---------------- #

def build_canvas(raw, annotated, state, ratio):
    h, w = raw.shape[:2]
    canvas = np.zeros((h * 2 + 50, w + 300, 3), dtype=np.uint8)

    # Frames
    canvas[0:h, 0:w] = annotated
    canvas[h:h*2, 0:w] = raw

    # Labels
    cv2.putText(canvas, "ANNOTATED", (10, 30), FONT, 1, (255, 255, 255), 2)
    cv2.putText(canvas, "ORIGINAL", (10, h + 30), FONT, 1, (255, 255, 255), 2)

    # Status panel
    panel_x = w
    canvas[:, panel_x:] = (50, 50, 50)
    cv2.putText(canvas, "STATUS", (panel_x + 10, 30), FONT, 1, (255, 255, 255), 2)

    state_text = state if state else "detecting"
    ratio_text = f"{ratio:.2f}" if ratio is not None else "--"

    color = {
        "left":   (255, 0, 0),
        "center": (0, 255, 0),
        "right":  (0, 165, 255),
        "closed": (0, 0, 255)
    }.get(state, (200, 200, 200))

    cv2.putText(canvas, f"Gaze: {state_text}", (panel_x + 10, 100),
                FONT, 1.2, color, 2)

    cv2.putText(canvas, f"Ratio: {ratio_text}", (panel_x + 10, 160),
                FONT, 1, (255, 255, 255), 2)

    return canvas


# ---------------- MAIN LOOP ---------------- #

def main():
    cap = cv2.VideoCapture(0)
    tracker = GazeTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        annotated = frame.copy()
        state, ratio = tracker.process(annotated, debug=True)

        canvas = build_canvas(frame, annotated, state, ratio)
        cv2.imshow("Eye Gaze System", canvas)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
