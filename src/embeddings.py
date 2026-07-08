from keras_facenet import FaceNet
import cv2

# Load FaceNet model
embedder = FaceNet()

# Read one registered image
image = cv2.imread("registered_faces/Udit/1.jpg")

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Resize image (FaceNet expects 160x160)
image = cv2.resize(image, (160, 160))

# Add batch dimension
image = image.reshape(1, 160, 160, 3)

# Generate embedding
embedding = embedder.embeddings(image)

print("Embedding Shape:", embedding.shape)
print(embedding)