import tkinter as tk
from tkinter import messagebox

# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("Desktop Countdown Timer")
root.geometry("450x320")
root.resizable(False, False)

# =========================
# VARIABLES
# =========================

time_left = 0
running = False

# =========================
# FUNCTIONS
# =========================

def format_time(seconds):
    """Convert seconds into HH:MM:SS format"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"



def update_timer():
    """Update timer every second"""
    global time_left, running

    timer_label.config(text=format_time(time_left))

    if running and time_left > 0:
        time_left -= 1
        root.after(1000, update_timer)

    elif running and time_left == 0:
        running = False

        messagebox.showinfo(
            "Time's Up!",
            "Countdown finished!"
        )


def start_timer():
    """Start or resume timer"""
    global time_left, running

    if not running:

        if time_left == 0:
            try:
                time_left = int(time_entry.get())

                if time_left < 0:
                    raise ValueError

            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter a valid positive number."
                )
                return

        running = True
        update_timer()


def pause_timer():
    global running

    if running:
        running = False
        pause_button.config(text="Resume")

    else:
        running = True
        pause_button.config(text="Pause")
        update_timer()


def reset_timer():
    """Reset timer"""
    global running, time_left

    running = False
    time_left = 0

    timer_label.config(text="00:00:00")

    time_entry.delete(0, tk.END)


# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="Countdown Timer",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

# =========================
# TIMER DISPLAY
# =========================

timer_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 42, "bold")
)
timer_label.pack(pady=20)

# =========================
# INPUT FIELD
# =========================

time_entry = tk.Entry(
    root,
    font=("Arial", 16),
    justify="center",
    width=15
)
time_entry.pack()

# =========================
# BUTTONS
# =========================

button_frame = tk.Frame(root)
button_frame.pack(pady=25)

start_button = tk.Button(
    button_frame,
    text="Start",
    width=10,
    command=start_timer
)
start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(
    button_frame,
    text="Pause",
    width=10,
    command=pause_timer
)
pause_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(
    button_frame,
    text="Reset",
    width=10,
    command=reset_timer
)
reset_button.grid(row=0, column=2, padx=5)

# =========================
# RUN APPLICATION
# =========================

root.mainloop()