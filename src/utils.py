import numpy as np

def cosine_similarity(a, b):
    """
    Computes cosine similarity between two vectors.
    """
    a = a.flatten()
    b = b.flatten()

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )