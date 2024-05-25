import tkinter as tk
from tkinter import Entry, Button

def on_submit():
    user_input = entry_var.get()

    # Pass user input to the second script using subprocess
    import subprocess
    subprocess.run(["python", "calculate_shares.py", user_input])

# Create the main window
root = tk.Tk()
root.title("User Input GUI")

# Create and place widgets in the window
tk.Label(root, text="Enter current price:").pack(pady=5)
entry_var = tk.StringVar()
entry = Entry(root, textvariable=entry_var)
entry.pack(pady=5)

submit_button = Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Start the main loop
root.mainloop()
