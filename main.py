import tkinter as tk
from tkinter import messagebox

# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("Desktop Countdown Timer")
root.geometry("500x350")
root.resizable(False, False)

# =========================
# VARIABLES
# =========================

time_left = 0
running = False

# =========================
# HELPER FUNCTIONS
# =========================

def format_time(seconds):
    """Convert total seconds to HH:MM:SS"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"


def parse_time(time_string):
    """
    Convert HH:MM:SS input into total seconds.
    Example:
    01:30:15 -> 5415
    """

    parts = time_string.split(":")

    if len(parts) != 3:
        raise ValueError

    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])

    if hours < 0:
        raise ValueError

    if minutes < 0 or minutes > 59:
        raise ValueError

    if seconds < 0 or seconds > 59:
        raise ValueError

    return hours * 3600 + minutes * 60 + seconds


# =========================
# PLACEHOLDER FUNCTIONS
# =========================

def clear_placeholder(event):
    if time_entry.get() == "HH:MM:SS":
        time_entry.delete(0, tk.END)
        time_entry.config(fg="black")


def add_placeholder(event):
    if time_entry.get().strip() == "":
        time_entry.insert(0, "HH:MM:SS")
        time_entry.config(fg="gray")


# =========================
# TIMER FUNCTIONS
# =========================

def update_timer():
    global time_left, running

    timer_label.config(text=format_time(time_left))

    if running and time_left > 0:

        time_left -= 1

        root.after(1000, update_timer)

    elif running and time_left == 0:

        running = False

        pause_button.config(text="Pause")

        messagebox.showinfo(
            "Time's Up!",
            "Countdown finished!"
        )


def start_timer():
    global time_left, running

    if not running:

        if time_left == 0:

            try:
                value = time_entry.get().strip()

                if value == "" or value == "HH:MM:SS":
                    raise ValueError

                time_left = parse_time(value)

                if time_left <= 0:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Invalid Input",
                    "Please enter time in HH:MM:SS format.\n\nExample:\n01:30:00"
                )

                return

        running = True

        pause_button.config(text="Pause")

        update_timer()


def pause_timer():
    global running

    if running:

        running = False

        pause_button.config(text="Resume")

    else:

        if time_left > 0:

            running = True

            pause_button.config(text="Pause")

            update_timer()


def reset_timer():
    global running, time_left

    running = False
    time_left = 0

    timer_label.config(text="00:00:00")

    pause_button.config(text="Pause")

    time_entry.delete(0, tk.END)
    time_entry.insert(0, "HH:MM:SS")
    time_entry.config(fg="gray")


# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="Countdown Timer",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=15)

# =========================
# TIMER DISPLAY
# =========================

timer_label = tk.Label(
    root,
    text="00:00:00",
    font=("Consolas", 42, "bold")
)

timer_label.pack(pady=20)

# =========================
# INPUT LABEL
# =========================

input_label = tk.Label(
    root,
    text="Enter Time (HH:MM:SS)",
    font=("Arial", 11)
)

input_label.pack()

# =========================
# INPUT FIELD
# =========================

time_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    width=15,
    fg="gray"
)

time_entry.pack(pady=10)

time_entry.insert(0, "HH:MM:SS")

time_entry.bind("<FocusIn>", clear_placeholder)
time_entry.bind("<FocusOut>", add_placeholder)

# =========================
# BUTTON FRAME
# =========================

button_frame = tk.Frame(root)

button_frame.pack(pady=25)

# =========================
# START BUTTON
# =========================

start_button = tk.Button(
    button_frame,
    text="Start",
    width=12,
    command=start_timer
)

start_button.grid(row=0, column=0, padx=5)

# =========================
# PAUSE / RESUME BUTTON
# =========================

pause_button = tk.Button(
    button_frame,
    text="Pause",
    width=12,
    command=pause_timer
)

pause_button.grid(row=0, column=1, padx=5)

# =========================
# RESET BUTTON
# =========================

reset_button = tk.Button(
    button_frame,
    text="Reset",
    width=12,
    command=reset_timer
)

reset_button.grid(row=0, column=2, padx=5)

# =========================
# START APPLICATION
# =========================

root.mainloop()