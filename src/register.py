import cv2
import mediapipe as mp
import os
import time
import subprocess
import sys


mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Enter your name: ").strip()
save_folder = os.path.join("registered_faces", name)
os.makedirs(save_folder, exist_ok=True)

image_count = 0
last_capture_time = time.time()
capture_interval = 0.5

cap = cv2.VideoCapture(0)

cropped_face = None

while True:

    success, frame = cap.read()

    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detection.process(rgb)

    if results.detections:

        for detection in results.detections:

            bbox = detection.location_data.relative_bounding_box

            h, w, c = frame.shape

            xmin = int(bbox.xmin * w)
            ymin = int(bbox.ymin * h)

            box_width = int(bbox.width * w)
            box_height = int(bbox.height * h)

            cv2.rectangle(
                frame,
                (xmin, ymin),
                (xmin + box_width, ymin + box_height),
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"Images : {image_count}/20",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

            cropped_face = frame[
                ymin:ymin+box_height,
                xmin:xmin+box_width
            ]

            if cropped_face.size != 0:

                cv2.imshow("Cropped Face", cropped_face)

                current_time = time.time()

                if current_time - last_capture_time >= capture_interval:

                    image_count += 1

                    filename = os.path.join(
                        save_folder,
                        f"{image_count}.jpg"
                    )

                    cv2.imwrite(filename, cropped_face)

                    print(f"Saved Image {image_count}")

                    last_capture_time = current_time

    cv2.imshow("Registration", frame)

    key = cv2.waitKey(1) & 0xFF

    if image_count >= 20:
        print("\nRegistration Completed!")

        break

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("\nGenerating Face Embeddings...")

subprocess.run(
    [sys.executable, "src/generate_embeddings.py"]
)

print("\nRegistration Successful!")