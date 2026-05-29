import tkinter as tk

# Create the main window
root = tk.Tk()

# Window title
root.title("Desktop Countdown Timer")

# Window size
root.geometry("400x300")

# Timer Display
timer_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 40)
)

timer_label.pack(pady=50)

# Start application
root.mainloop()