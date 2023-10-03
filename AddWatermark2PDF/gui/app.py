import PySimpleGUI as sg
from utils import helpers

def create_gui():
    layout = [
        [sg.Text("Select PDF File: "), sg.InputText(key="-PDF-"), sg.FileBrowse()],
        [sg.Text("Watermark Text: "), sg.InputText(key="-WATERMARK-")],
        [sg.Text("Position (x, y): "), sg.InputText(key="-POSITION-")],
        [sg.Button("Apply Watermark"), sg.Button("Exit")],
    ]

    window = sg.Window("PDF Watermark App", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        if event == "Apply Watermark":
            input_pdf = values["-PDF-"]
            watermark_text = values["-WATERMARK-"]
            position = values["-POSITION-"].split(",") if values["-POSITION-"] else (100, 100)
            output_pdf = "output.pdf"

            helpers.apply_watermark(input_pdf, watermark_text, output_pdf)
            sg.popup("Watermark Applied Successfully!", title="Success")

    window.close()