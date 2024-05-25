import tkinter as tk
from tkinter import messagebox

def on_submit():
    # Retrieve the variables from the entry widgets
    variable1_value = entry_var1.get()
    variable2_value = entry_var2.get()
    variable3_value = entry_var3.get()
    
    

    # Store the variables in a text file
    with open('variables.txt', 'w') as file:
        file.write(f"enc_token='{variable1_value}'\n")
        file.write(f"stock_name='NSE:{variable2_value}'\n")
        file.write(f"quantity={variable3_value}\n")
        root.destroy()  # Close the main window
       


# Create the main window
root = tk.Tk()
root.title("User Data Entry")

# Create and place widgets in the window
tk.Label(root, text="ENC TOKEN PLEASE...").pack(pady=5)
entry_var1 = tk.StringVar()
entry1 = tk.Entry(root, textvariable=entry_var1)
entry1.pack(pady=5)

tk.Label(root, text="WHICH STOCK").pack(pady=5)
entry_var2 = tk.StringVar()
entry2 = tk.Entry(root, textvariable=entry_var2)
entry2.pack(pady=5)

tk.Label(root, text="QUANTITY PLEASE..").pack(pady=5)
entry_var3 = tk.StringVar()
entry3 = tk.Entry(root, textvariable=entry_var3)
entry3.pack(pady=5)



submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Start the main loop
root.mainloop()
