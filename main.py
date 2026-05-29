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


# Time Input
time_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center"
)

time_entry.pack()

# Placeholder text
time_entry.insert(0, "Enter seconds")


# Start application
root.mainloop()