import tkinter as tk

# Global variable to keep track of the remaining time

time_left = 0
running = False

# Function to format time in HH:MM:SS

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"


# Function to update the timer display every second

def update_timer():
    global time_left, running

    if running and time_left > 0:

        time_left -= 1

        timer_label.config(
            text=format_time(time_left)
        )

        root.after(1000, update_timer)

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

def start_timer():
    global time_left, running

    if not running:

        try:
            time_left = int(time_entry.get())

        except ValueError:
            print("Please enter a valid number")
            return

        running = True

        timer_label.config(
            text=format_time(time_left)
        )

        update_timer()

# Start Button
start_button = tk.Button(
    root,
    text="Start",
    font=("Arial", 14),
    command=start_timer
)

start_button.pack(pady=20)

# Start application
root.mainloop()