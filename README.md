# Face Recognition Attendance System

An AI-powered desktop application that automatically marks attendance using real-time face recognition.

## Features

- Real-time Face Detection using MediaPipe
- Face Registration
- Face Embedding Generation using FaceNet
- Face Recognition using Cosine Similarity
- Unknown Face Detection
- Attendance Management
- SQLite Database Integration
- Desktop GUI using Tkinter
- Attendance Viewer

---

## Tech Stack

- Python
- OpenCV
- MediaPipe
- FaceNet (keras-facenet)
- TensorFlow
- SQLite
- Tkinter
- NumPy

---

## Project Structure

```text
face-recognition-system/

├── embeddings/
├── registered_faces/
├── src/
├── attendance.db
├── requirements.txt
├── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/face-recognition-system.git
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python src/gui.py
```

---

## How It Works

1. Register a new face.
2. Generate face embeddings.
3. Start recognition.
4. FaceNet creates a 512-dimensional embedding.
5. Cosine Similarity compares it with registered embeddings.
6. If similarity exceeds the threshold, attendance is stored in SQLite.

---

## Future Improvements

- Multi-face recognition
- Face anti-spoofing
- Web dashboard
- Cloud database
- User authentication

---

## Author

**Udit Shetty**

Information Science & Engineering Student

Python | Machine Learning | AI