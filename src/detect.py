import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

print("Face Detection Started...")

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to capture frame.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detection.process(rgb_frame)

    if results.detections:
        print("Face Detected!!")
        for detection in results.detections:
           # mp_draw.draw_detection(frame, detection)
           bbox = detection.location_data.relative_bounding_box
           h, w, c = frame.shape
           xmin = int(bbox.xmin * w)
           ymin = int(bbox.ymin * h)
           box_width = int(bbox.width * w)
           box_height = int(bbox.height * h)


    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Face Detection Stopped.")
        break

cap.release()
cv2.destroyAllWindows()