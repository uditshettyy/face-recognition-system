import os
import cv2
import numpy as np
from keras_facenet import FaceNet

embedder = FaceNet()

REGISTERED_DIR = "registered_faces"
EMBEDDINGS_DIR = "embeddings"

os.makedirs(EMBEDDINGS_DIR, exist_ok=True)

for person in os.listdir(REGISTERED_DIR):

    person_folder = os.path.join(REGISTERED_DIR, person)

    if not os.path.isdir(person_folder):
        continue

    embeddings = []

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        image = cv2.imread(image_path)

        if image is None:
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (160,160))
        image = image.reshape(1,160,160,3)

        embedding = embedder.embeddings(image)

        embeddings.append(embedding[0])

    embeddings = np.array(embeddings)

    np.save(
        os.path.join(
            EMBEDDINGS_DIR,
            f"{person}.npy"
        ),
        embeddings
    )

    print(f"Saved embeddings for {person}")

print("All embeddings generated successfully!")