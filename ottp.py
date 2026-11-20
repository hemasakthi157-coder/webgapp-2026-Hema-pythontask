import tkinter as tk
from tkinter import messagebox
import secrets
import time

otp = None
expiry_time = 0
timer_id = None

def generate_otp():
    global otp, expiry_time, timer_id

    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None

    otp = str(secrets.randbelow(9000) + 1000)
    expiry_time = time.time() + 30

    otp_label.config(text=otp, fg="green")
    status_label.config(text="OTP Generated Successfully!")

    countdown()

def countdown():
    global timer_id

    remaining = int(expiry_time - time.time())

    if remaining > 0:
        timer_label.config(text=f"Expires in: {remaining} seconds")
        timer_id = window.after(1000, countdown)
    else:
        otp_label.config(text="----", fg="red")
        timer_label.config(text="OTP Expired!")
        status_label.config(text="Generate a new OTP")
        timer_id = None

def copy_otp():
    if otp and time.time() < expiry_time:
        window.clipboard_clear()
        window.clipboard_append(otp)
        messagebox.showinfo("Success", "OTP Copied!")
    else:
        messagebox.showwarning("Expired", "Please generate a new OTP")

window = tk.Tk()
window.title("Advanced OTP Generator")
window.geometry("400x350")
window.configure(bg="#eaf2f8")

title = tk.Label(
    window,
    text="OTP GENERATOR",
    font=("Arial", 20, "bold"),
    bg="#eaf2f8"
)
title.pack(pady=20)

otp_label = tk.Label(
    window,
    text="----",
    font=("Arial", 30, "bold"),
    bg="#eaf2f8"
)
otp_label.pack(pady=15)

status_label = tk.Label(
    window,
    text="Click below to generate OTP",
    bg="#eaf2f8"
)
status_label.pack(pady=5)

timer_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="#eaf2f8"
)
timer_label.pack(pady=10)

generate_button = tk.Button(
    window,
    text="Generate OTP",
    command=generate_otp,
    bg="#0984e3",
    fg="white",
    font=("Arial", 12, "bold")
)
generate_button.pack(pady=10)

copy_button = tk.Button(
    window,
    text="Copy OTP",
    command=copy_otp
)
copy_button.pack(pady=5)

window.mainloop()
