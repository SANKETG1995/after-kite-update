import tkinter as tk
import subprocess

def run_script():
    try:
        # Replace 'your_script.py' with the actual name of your main script
        subprocess.run(['python', 'main2.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")

def restart_script():
    run_script()

def main():
    root = tk.Tk()
    root.title("Script Restart")

    banner_label = tk.Label(root, text="Stop with 5% Profit now 500", font=("Arial", 16, "bold"))
    banner_label.pack(pady=10)

    restart_button = tk.Button(root, text="Restart Script", command=restart_script)
    restart_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
