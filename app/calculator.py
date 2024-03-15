import tkinter as tk
from tkinter import font

from app.constants.calculator import (
    BACKGROUND_COLOR_DARK,
    FONT_COLOR,
    SPECIAL_BUTTON_COLOR,
    SIMPLE_BUTTON_COLOR,
)
from app.utils.calculators import center_window


class FormCalculator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.build_widget()

    def config_window(self):
        self.title("Calculator")
        self.configure(bg=BACKGROUND_COLOR_DARK)
        self.attributes("-alpha", 0.96)
        w, h = 370, 570
        center_window(self, w, h)
        self.bind("<Key>", self.other_test)

    def build_widget(self):
        self.label_operation = tk.Label(
            self,
            text="",
            font=("Ubuntu", 16),
            fg=FONT_COLOR,
            bg=BACKGROUND_COLOR_DARK,
            justify="right",
        )
        self.label_operation.grid(row=0, column=3, padx=10, pady=10)
        self.entry = tk.Entry(
            self,
            width=12,
            font=("Ubuntu", 40),
            bd=0,
            fg=FONT_COLOR,
            bg=BACKGROUND_COLOR_DARK,
            justify="right",
        )
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        buttons = [
            "C",
            "%",
            "<",
            "/",
            "7",
            "8",
            "9",
            "*",
            "4",
            "5",
            "6",
            "-",
            "1",
            "2",
            "3",
            "+",
            "0",
            ".",
            "=",
        ]
        row_val = 2
        col_val = 0
        font_buttons = font.Font(family="Ubuntu", size=16)

        for text in buttons:
            if text in ["=", "*", "/", "-", "+", "C", "<", "%"]:
                background_color = SPECIAL_BUTTON_COLOR
                font_button = font.Font(size=16, weight="bold")
            else:
                background_color = SIMPLE_BUTTON_COLOR
                font_button = font_buttons

            if text == "=":
                width_button = 13
                col_span = 2
            else:
                width_button = 5
                col_span = 1

            button = tk.Button(
                self,
                text=text,
                width=width_button,
                height=2,
                bg=background_color,
                fg=FONT_COLOR,
                relief=tk.FLAT,
                command=lambda b=text: self.on_click_button(b),
                font=font_button,
                padx=5,
                pady=5,
                overrelief="flat",
            )

            button.grid(row=row_val, column=col_val, columnspan=col_span, pady=5)

            col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

    def other_test(self, event):
        if event.char == "n":
            self.on_click_button("0")
        elif event.char == "h":
            self.on_click_button("=")
        elif event.char == "m":
            self.on_click_button("1")
        elif event.char == ",":
            self.on_click_button("2")
        elif event.char == ".":
            self.on_click_button("3")
        elif event.char == "/":
            self.on_click_button("+")
        elif event.char == "j":
            self.on_click_button("4")
        elif event.char == "k":
            self.on_click_button("5")
        elif event.char == "l":
            self.on_click_button("6")
        elif event.char == ";":
            self.on_click_button("-")
        elif event.char == "u":
            self.on_click_button("7")
        elif event.char == "i":
            self.on_click_button("8")
        elif event.char == "o":
            self.on_click_button("9")
        elif event.char == "p":
            self.on_click_button("*")
        elif event.char == "[":
            self.on_click_button("/")
        elif event.char == "]":
            self.on_click_button("<")
        elif event.char == "y":
            self.on_click_button("C")
        elif event.char == "d":
            self.on_click_button(".")

    def on_click_button(self, value):
        if value == "=":
            try:
                expression = self.entry.get().replace("%", "/100")
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                operation = expression + " " + value
                self.label_operation.config(text=operation)
            except Exception as e:
                print(e)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.label_operation.config(text="")
        elif value == "C":
            self.entry.delete(0, tk.END)
            self.label_operation.config(text="")
        elif value == "<":
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
                self.label_operation.config(text=new_text + " ")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
            if value == "=":
                self.label_operation.config(text="")


def init():
    app = FormCalculator()
    app.mainloop()


if __name__ == "__main__":
    init()
