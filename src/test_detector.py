import cv2
from detector import detect_face

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    face, bbox = detect_face(frame)

    if bbox:

        x, y, w, h = bbox

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    if face is not None:
        cv2.imshow("Face", cv2.cvtColor(face, cv2.COLOR_RGB2BGR))

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()