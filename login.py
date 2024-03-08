import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password match
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        # Add code here to proceed after successful login
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login")

# Create username label and entry widget
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Create password label and entry widget
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
