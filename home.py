import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("600x400")
        self.home_page()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def home_page(self):
        self.clear_frame()
        tk.Label(self.root, text="Flight Reservation System", font=("Arial", 18)).pack(pady=20)
        tk.Button(self.root, text="Book Flight", command=self.open_booking).pack(pady=10)
        tk.Button(self.root, text="View Reservations", command=self.open_reservations).pack(pady=10)

    def open_booking(self):
        BookingPage(self.root, self)

    def open_reservations(self):
        ReservationsPage(self.root, self)
