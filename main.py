import tkinter as tk
from database import connect_db
from home import HomePage

if __name__ == "__main__":
    connect_db()
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
