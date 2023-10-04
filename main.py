"""
Made by   : Rohit Kumar Yadav
Created On: 03 Oct 2023
"""
# This is a beautifully designed calculator application 
# with a clean and intuitive interface.

# Import the necessary modules
import tkinter as tk # module is used for performing GUI 
from tkinter import ttk

# Define the click event handler
def click(event):
    text = event.widget.cget("text")

    # Perform the appropriate action based on the clicked button
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "AC":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create the main window
main = tk.Tk()
main.title("Calculator")
main.iconbitmap('./cal.ico')

# Set the style and theme of the window
style = ttk.Style()
style.theme_use("vista")
main.option_add("*Font", "Roboto 15 bold")

# Define the color scheme for the buttons
button_colors = {
    "+": "ivory3",
    "-": "ivory3",
    "*": "ivory3",
    "/": "ivory3",
    "=": "DarkSlateGray4",
    "AC": "coral1"
}

# Configure the layout of the window
main.columnconfigure(0, pad=10)
main.rowconfigure(0, pad=10)
main.config(borderwidth=5)
main.config(relief="groove")

# Create a StringVar to store the text entered in the calculator
screen = tk.StringVar()
entry = tk.Entry(main, textvar=screen, font="Roboto 20 bold", justify="right")
entry.pack(fill=tk.X, ipadx=8, padx=10, pady=10)

# Create a frame to hold the buttons
button_frame = tk.Frame(main)
button_frame.pack()

# Define the buttons to be displayed on the calculator
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'AC', '0', '=', '/'
]

# Place the buttons on the button frame
row, col = 0, 0
for button_text in buttons:
    button_color = button_colors.get(button_text, "lightgray")  # Use a default color for numeric buttons
    button = tk.Button(button_frame, text=button_text, font="Roboto 15 bold", width=5, height=2, bg=button_color)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main event loop
main.mainloop()
