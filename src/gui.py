import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import sys

# -----------------------------
# Functions
# -----------------------------

def start_recognition():
    subprocess.Popen([sys.executable, "src/recognizer.py"])


def register_face():

    name = simpledialog.askstring(
        "Register Face",
        "Enter your Name:"
    )

    if not name:
        return

    process = subprocess.run(
        [
            sys.executable,
            "src/register.py",
            name
        ]
    )

    if process.returncode == 0:

        messagebox.showinfo(
            "Success",
            "Face Registered Successfully!"
        )

    else:

        messagebox.showerror(
            "Error",
            "Registration Failed!"
        )


def view_attendance():
    subprocess.Popen(
        [sys.executable, "src/view_attendance.py"]
    )


def exit_program():
    root.destroy()


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()

root.title("Face Recognition Attendance System")
root.geometry("650x520")
root.resizable(False, False)
root.configure(bg="#f5f5f5")


# -----------------------------
# Heading
# -----------------------------

title = tk.Label(
    root,
    text="Face Recognition Attendance System",
    font=("Segoe UI", 22, "bold"),
    bg="#f5f5f5",
    fg="#2c3e50"
)

title.pack(pady=(35,10))


subtitle = tk.Label(
    root,
    text="AI Powered Attendance using Face Recognition",
    font=("Segoe UI",11),
    bg="#f5f5f5",
    fg="gray"
)

subtitle.pack(pady=(0,35))


# -----------------------------
# Buttons
# -----------------------------

button_font = ("Segoe UI",12,"bold")

button_style = {
    "width":28,
    "height":2,
    "font":button_font,
    "cursor":"hand2"
}


btn_start = tk.Button(
    root,
    text="▶ Start Recognition",
    command=start_recognition,
    bg="#4CAF50",
    fg="white",
    **button_style
)

btn_start.pack(pady=10)


btn_register = tk.Button(
    root,
    text="📷 Register New Face",
    command=register_face,
    bg="#2196F3",
    fg="white",
    **button_style
)

btn_register.pack(pady=10)


btn_view = tk.Button(
    root,
    text="📊 View Attendance",
    command=view_attendance,
    bg="#FF9800",
    fg="white",
    **button_style
)

btn_view.pack(pady=10)


btn_exit = tk.Button(
    root,
    text="❌ Exit",
    command=exit_program,
    bg="#F44336",
    fg="white",
    **button_style
)

btn_exit.pack(pady=10)


# -----------------------------
# Footer
# -----------------------------

footer = tk.Label(
    root,
    text="Built with Python • MediaPipe • FaceNet • SQLite",
    font=("Segoe UI",10),
    bg="#f5f5f5",
    fg="gray"
)

footer.pack(side="bottom", pady=20)


root.mainloop()