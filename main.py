import tkinter as tk
from tkinter import messagebox

# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("Desktop Countdown Timer")
root.geometry("550x380")
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
    """Convert seconds to HH:MM:SS"""

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"


def move_to_next(event, next_widget=None):
    """Automatically move cursor after 2 digits"""

    widget = event.widget

    value = widget.get()

    if len(value) >= 2 and next_widget:
        next_widget.focus()
        next_widget.select_range(0, tk.END)


def select_all(event):
    """Select text when field gets focus"""

    event.widget.select_range(0, tk.END)

    return "break"


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

                hours = int(hours_entry.get().strip())
                minutes = int(minutes_entry.get().strip())
                seconds = int(seconds_entry.get().strip())

                if hours < 0:
                    raise ValueError

                if minutes < 0 or minutes > 59:
                    raise ValueError

                if seconds < 0 or seconds > 59:
                    raise ValueError

                time_left = (
                    hours * 3600
                    + minutes * 60
                    + seconds
                )

                if time_left <= 0:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Invalid Input",
                    "Please enter valid time values.\n\nMinutes and seconds must be between 00 and 59."
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

    hours_entry.delete(0, tk.END)
    minutes_entry.delete(0, tk.END)
    seconds_entry.delete(0, tk.END)

    hours_entry.insert(0, "00")
    minutes_entry.insert(0, "00")
    seconds_entry.insert(0, "00")


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
# DISPLAY
# =========================

timer_label = tk.Label(
    root,
    text="00:00:00",
    font=("Consolas", 42, "bold")
)

timer_label.pack(pady=20)

# =========================
# INPUT SECTION
# =========================

input_label = tk.Label(
    root,
    text="Set Countdown Time",
    font=("Arial", 12)
)

input_label.pack()

time_frame = tk.Frame(root)
time_frame.pack(pady=10)

# Hours

hours_entry = tk.Entry(
    time_frame,
    width=4,
    font=("Arial", 18),
    justify="center"
)

hours_entry.insert(0, "00")

hours_entry.grid(row=0, column=0)

# :

tk.Label(
    time_frame,
    text=":",
    font=("Arial", 18, "bold")
).grid(row=0, column=1)

# Minutes

minutes_entry = tk.Entry(
    time_frame,
    width=4,
    font=("Arial", 18),
    justify="center"
)

minutes_entry.insert(0, "00")

minutes_entry.grid(row=0, column=2)

# :

tk.Label(
    time_frame,
    text=":",
    font=("Arial", 18, "bold")
).grid(row=0, column=3)

# Seconds

seconds_entry = tk.Entry(
    time_frame,
    width=4,
    font=("Arial", 18),
    justify="center"
)

seconds_entry.insert(0, "00")

seconds_entry.grid(row=0, column=4)

# =========================
# AUTO-JUMP BINDINGS
# =========================

hours_entry.bind(
    "<KeyRelease>",
    lambda e: move_to_next(e, minutes_entry)
)

minutes_entry.bind(
    "<KeyRelease>",
    lambda e: move_to_next(e, seconds_entry)
)

hours_entry.bind("<FocusIn>", select_all)
minutes_entry.bind("<FocusIn>", select_all)
seconds_entry.bind("<FocusIn>", select_all)

# =========================
# FIELD LABELS
# =========================

label_frame = tk.Frame(root)
label_frame.pack()

tk.Label(
    label_frame,
    text="Hours",
    width=8
).grid(row=0, column=0)

tk.Label(
    label_frame,
    text="Minutes",
    width=8
).grid(row=0, column=1)

tk.Label(
    label_frame,
    text="Seconds",
    width=8
).grid(row=0, column=2)

# =========================
# BUTTONS
# =========================

button_frame = tk.Frame(root)
button_frame.pack(pady=30)

start_button = tk.Button(
    button_frame,
    text="Start",
    width=12,
    command=start_timer
)

start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(
    button_frame,
    text="Pause",
    width=12,
    command=pause_timer
)

pause_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(
    button_frame,
    text="Reset",
    width=12,
    command=reset_timer
)

reset_button.grid(row=0, column=2, padx=5)

# =========================
# START APP
# =========================

root.mainloop()