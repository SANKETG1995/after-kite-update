import webbrowser
import tkinter as tk

def open_chart():
    symbol = entry.get()
    url = f"https://www.tradingview.com/chart/?symbol={symbol}"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

# Create GUI
root = tk.Tk()
root.title("Open TradingView Chart")
label = tk.Label(root, text="Enter symbol:")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Open Chart", command=open_chart)
button.pack()
root.mainloop()

