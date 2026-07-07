import cv2
print("Camera Started ...")

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to capture frame.")
        break

    cv2.imshow("Face Recognition System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Camera Stopped Successfully..")
        break

cap.release()
cv2.destroyAllWindows()