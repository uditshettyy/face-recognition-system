import cv2
from mtcnn import MTCNN

# Initialize detector only once
detector = MTCNN()

def detect_face(frame):
    """
    Detects the largest face in the frame.

    Returns:
        cropped_face (RGB image or None)
        bbox (x, y, w, h or None)
    """

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = detector.detect_faces(rgb)

    if len(results) == 0:
        return None, None

    # Take the largest detected face
    face = max(
        results,
        key=lambda x: x["box"][2] * x["box"][3]
    )

    x, y, w, h = face["box"]

    # Prevent negative coordinates
    x = max(0, x)
    y = max(0, y)

    cropped_face = rgb[y:y+h, x:x+w]

    if cropped_face.size == 0:
        return None, None

    return cropped_face, (x, y, w, h)