import os
import cv2
import numpy as np
import mediapipe as mp
from keras_facenet import FaceNet
from datetime import datetime

from database import mark_attendance

# -----------------------------
# Load FaceNet
# -----------------------------
embedder = FaceNet()

# -----------------------------
# Load Stored Embeddings
# -----------------------------
EMBEDDINGS_DIR = "embeddings"

known_faces = {}

for file in os.listdir(EMBEDDINGS_DIR):

    if file.endswith(".npy"):

        person_name = file.replace(".npy", "")

        embedding = np.load(
            os.path.join(EMBEDDINGS_DIR, file)
        )

        known_faces[person_name] = embedding

print("Known Faces:", list(known_faces.keys()))

# -----------------------------
# MediaPipe Face Detection
# -----------------------------
mp_face_detection = mp.solutions.face_detection

face_detector = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

# -----------------------------
# Attendance Memory
# -----------------------------
marked_attendance = set()

# -----------------------------
# Start Camera
# -----------------------------
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detector.process(rgb)

    if results.detections:

        detection = results.detections[0]

        bbox = detection.location_data.relative_bounding_box

        h, w, _ = frame.shape

        xmin = int(bbox.xmin * w)
        ymin = int(bbox.ymin * h)

        box_width = int(bbox.width * w)
        box_height = int(bbox.height * h)

        cv2.rectangle(
            frame,
            (xmin, ymin),
            (xmin + box_width, ymin + box_height),
            (0, 255, 0),
            2
        )

        face = frame[
            ymin:ymin + box_height,
            xmin:xmin + box_width
        ]

        if face.size != 0:

            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (160, 160))
            face = face.reshape(1, 160, 160, 3)

            live_embedding = embedder.embeddings(face)

            best_name = "Unknown"
            best_score = -1

            # -----------------------------
            # Compare Embeddings
            # -----------------------------
            for person, embeddings in known_faces.items():

                for stored_embedding in embeddings:

                    score = np.dot(
                        live_embedding[0],
                        stored_embedding
                    ) / (
                        np.linalg.norm(live_embedding[0]) *
                        np.linalg.norm(stored_embedding)
                    )

                    if score > best_score:
                        best_score = score
                        best_name = person

            # -----------------------------
            # Recognition Decision
            # -----------------------------
            THRESHOLD = 0.85

            if best_score >= THRESHOLD:

                display_name = best_name

                # Mark attendance only once
                if display_name not in marked_attendance:

                    now = datetime.now()

                    date = now.strftime("%d-%m-%Y")
                    time = now.strftime("%H:%M:%S")

                    mark_attendance(
                        display_name,
                        date,
                        time
                    )

                    marked_attendance.add(display_name)

            else:

                display_name = "Unknown"

            # -----------------------------
            # Display Result
            # -----------------------------
            cv2.putText(
                frame,
                f"{display_name} ({best_score:.2f})",
                (xmin, ymin - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    cv2.imshow("Face Recognition Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()