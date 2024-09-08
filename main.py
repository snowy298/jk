import tkinter as tk
from tkinter import messagebox
import requests

# Server URL
SERVER_URL = 'http://localhost:5000'

# Function to handle sign-in
def signin():
    username = username_entry.get()
    password = password_entry.get()

    try:
        response = requests.post(f'{SERVER_URL}/signin', json={'username': username, 'password': password})
        data = response.json()
        
        if response.status_code == 200:
            messagebox.showinfo("Success", data['message'])
        else:
            messagebox.showerror("Error", data['message'])
    except requests.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Sign In")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password label and entry
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Sign-in button
signin_button = tk.Button(root, text="Sign In", command=signin)
signin_button.pack(pady=20)

# Run the application
root.mainloop()
