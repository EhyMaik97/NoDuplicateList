import tkinter as tk
import pyperclip
from utils.helpers import(
    remove_duplicates,
    is_valid_input
) 

def run_gui_app():
    def remove_duplicates_callback():
        input_text = input_entry.get()
        if is_valid_input(input_text):
            result = remove_duplicates(input_text)
            result_text.set("[" + ", ".join(map(str, result)) + "]")
        else:
            result_text.set("Invalid input: Please enter digits and spaces only")

    def copy_to_clipboard():
        result_to_copy = result_text.get()
        pyperclip.copy(result_to_copy)

    root = tk.Tk()
    root.title("Remove Duplicates")

    input_label = tk.Label(root, text="Enter a list of numbers (space-separated):")
    input_entry = tk.Entry(root)
    remove_button = tk.Button(root, text="Remove Duplicates", command=remove_duplicates_callback)
    result_label = tk.Label(root, text="Result:")
    result_text = tk.StringVar()
    result_display = tk.Label(root, textvariable=result_text)

    copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)

    input_label.pack()
    input_entry.pack()
    remove_button.pack()
    result_label.pack()
    result_display.pack()
    copy_button.pack()

    root.mainloop()
