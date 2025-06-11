import sqlite3

def connect_db():
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                flight_number TEXT,
                departure TEXT,
                destination TEXT,
                date TEXT,
                seat_number TEXT)''')
    conn.commit()
    conn.close()
