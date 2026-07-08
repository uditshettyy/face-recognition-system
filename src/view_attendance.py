import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

DB_NAME = "attendance.db"


# -----------------------------
# Load Records
# -----------------------------
def load_data():

    for row in table.get_children():
        table.delete(row)

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, date, time
        FROM attendance
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    for record in records:
        table.insert("", tk.END, values=record)


# -----------------------------
# Delete Selected Row
# -----------------------------
def delete_record():

    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a record."
        )
        return

    item = table.item(selected)

    record_id = item["values"][0]

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM attendance WHERE id=?",
        (record_id,)
    )

    connection.commit()
    connection.close()

    load_data()

    messagebox.showinfo(
        "Success",
        "Attendance record deleted."
    )


# -----------------------------
# Window
# -----------------------------
root = tk.Tk()

root.title("Attendance Records")
root.geometry("750x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Attendance Records",
    font=("Segoe UI", 20, "bold")
)

title.pack(pady=15)


# -----------------------------
# Table
# -----------------------------
columns = ("ID", "Name", "Date", "Time")

table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

for col in columns:
    table.heading(col, text=col)

table.column("ID", width=70, anchor="center")
table.column("Name", width=180, anchor="center")
table.column("Date", width=180, anchor="center")
table.column("Time", width=180, anchor="center")

table.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)


# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(root)

button_frame.pack(pady=15)


refresh_btn = tk.Button(
    button_frame,
    text="Refresh",
    width=15,
    command=load_data
)

refresh_btn.grid(row=0, column=0, padx=10)


delete_btn = tk.Button(
    button_frame,
    text="Delete Selected",
    width=15,
    command=delete_record
)

delete_btn.grid(row=0, column=1, padx=10)


close_btn = tk.Button(
    button_frame,
    text="Close",
    width=15,
    command=root.destroy
)

close_btn.grid(row=0, column=2, padx=10)


# -----------------------------
# Initial Load
# -----------------------------
load_data()

root.mainloop()