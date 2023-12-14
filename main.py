import time
import tkinter as tk
from tkinter import messagebox

users = {}

def create_account():
    username = entry.get()
    password = entry1.get()
    if username and password:
        users[username] = password
        messagebox.showinfo("Success", f"Account created. Username: {username}")
        create_authenticate_window()
    else:
        messagebox.showerror("Error", "Username or password is empty.")

def authenticate():
    username = entry.get()
    password = entry1.get()
    if username in users and users[username] == password:
        token = generate_token()
        messagebox.showinfo("Success", f"Authenticated.")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def generate_token():
    return str(int(time.time()) // 30).zfill(10)

def create_authenticate_window():
    top = tk.Toplevel(app)
    top.title('Authenticate')
    top.geometry("500x200")

    label = tk.Label(top, text='Authenticate:')
    label.pack()

    entry = tk.Entry(top)
    entry.pack()

    entry1 = tk.Entry(top, show='*')
    entry1.pack()

    button = tk.Button(top, text='Authenticate', command=authenticate)
    button.pack()

app = tk.Tk()
app.title('Game Launcher')
app.geometry("1000x500")

frame = tk.Frame(app)
frame.pack(padx=100, pady=100)

label = tk.Label(frame, text='Create an account:')
label.pack()

entry = tk.Entry(frame)
entry.pack()

entry1 = tk.Entry(frame, show='*')
entry1.pack()

button = tk.Button(frame, text='Create', command=create_account)
button.pack()

app.mainloop()