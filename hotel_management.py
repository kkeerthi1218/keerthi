import tkinter as tk
from tkinter import messagebox

class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title(" Hotel Management System")
        self.root.geometry("500x600")
        self.root.config(bg="lightblue")

        self.guests = []

        # Title
        tk.Label(root, text="Hotel Check-In System", font=("Arial", 18, "bold"), bg="skyblue").pack(pady=10)

        # Guest Info
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.room_var = tk.StringVar()

        tk.Label(root, text="Guest Name:", font=("Arial", 12), bg="lightblue").pack(pady=5)
        tk.Entry(root, textvariable=self.name_var, font=("Arial", 12)).pack()

        tk.Label(root, text="Phone Number:", font=("Arial", 12), bg="lightblue").pack(pady=5)
        tk.Entry(root, textvariable=self.phone_var, font=("Arial", 12)).pack()

        tk.Label(root, text="Room Type:", font=("Arial", 12), bg="lightblue").pack(pady=5)
        self.room_menu = tk.OptionMenu(root, self.room_var, "Single", "Double", "Deluxe", "Suite")
        self.room_menu.config(font=("Arial", 12))
        self.room_var.set("Single")
        self.room_menu.pack()

        # Buttons
        tk.Button(root, text="Check-In", command=self.check_in, bg="green", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(root, text="Show All Guests", command=self.show_guests, bg="blue", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Check-Out Guest", command=self.check_out, bg="red", fg="white", font=("Arial", 12)).pack(pady=5)

        self.output = tk.Text(root, height=12, width=60)
        self.output.pack(pady=10)

    def check_in(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        room = self.room_var.get()

        if name and phone:
            guest = {"Name": name, "Phone": phone, "Room": room}
            self.guests.append(guest)
            messagebox.showinfo("Success", f"{name} checked into {room} room.")
            self.name_var.set("")
            self.phone_var.set("")
            self.room_var.set("Single")
        else:
            messagebox.showwarning("Missing Info", "Please fill all fields.")

    def show_guests(self):
        self.output.delete(1.0, tk.END)
        if not self.guests:
            self.output.insert(tk.END, "No guests currently.\n")
        else:
            for i, g in enumerate(self.guests, 1):
                self.output.insert(tk.END, f"{i}. {g['Name']} | {g['Phone']} | {g['Room']}\n")

    def check_out(self):
        name = self.name_var.get()
        for g in self.guests:
            if g["Name"].lower() == name.lower():
                self.guests.remove(g)
                messagebox.showinfo("Checked Out", f"{name} has been checked out.")
                return
        messagebox.showwarning("Not Found", f"{name} not found in guest list.")

# Run the App
root = tk.Tk()
app = HotelManagement(root)
root.mainloop()