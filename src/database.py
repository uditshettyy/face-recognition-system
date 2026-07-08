import sqlite3


def create_database():

    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            date TEXT NOT NULL,

            time TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def mark_attendance(name, date, time):

    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO attendance(name, date, time)
        VALUES(?,?,?)
        """,
        (name, date, time)
    )

    connection.commit()
    connection.close()


create_database()
mark_attendance(
    "Test User",
    "08-07-2026",
    "19:00:00"
)

print("Database Ready!")
