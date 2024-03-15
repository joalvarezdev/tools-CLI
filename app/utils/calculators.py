import tkinter as tk


def center_window(window: tk.Tk, width: int, height: int):
    app_width = window.winfo_screenwidth()
    app_height = window.winfo_screenheight()

    x = int((app_width / 2) - (width / 2))
    y = int((app_height / 2) - (height / 2))

    return window.geometry(f"{app_width}x{app_height}+{x}+{y}")
