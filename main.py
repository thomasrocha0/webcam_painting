import tkinter as tk
from webcam_paint import paint
import cv2
import numpy as np


opacity = 0.5
watercolor = False
settingstext = "Opacity: {opacity}  Watercolor? {watercolor}"


"""
Starts the webpainting app

"""
def startPaint():
    paint(opacity, watercolor)
"""
Applies settings to opacity and watercolor 
"""
def applyChangesFunc():
    global opacity 
    global watercolor
    opacity = opacEntry.get()
    watercolor = var.get() == 1
    try:
        opacity = float(opacity)
        if opacity < 0 or opacity > 1:
            raise ValueError("Opacity must be between 0 and 1")
        else:
            settings.config(text=settingstext.format(opacity=opacity, watercolor=watercolor))
    except ValueError:
        settings.config(text="Please enter a valid opacity")
 
    
window = tk.Tk()
# tracks watercolor checkbutton
var = tk.IntVar()
entryLabel = tk.Label(
    text="Welcome to Webcam Paint! Please enter your desired settings below and click \"Start Painting!\" to begin your masterpiece.",
    wraplength = 300
)
opacLabel = tk.Label(
    text="Enter the opacity of your markers (decimal value between 0 and 1)",
    width=20,
    height=5,
    wraplength=150
)
opacEntry = tk.Entry(
    width=10, 
)
watercolorLabel = tk.Label(
    text="Toggle watercolor mode (True/False)",
    width=20,
    height=5,
    wraplength=150
)
watercolorEntry = tk.Checkbutton(
    variable = var
)
applyChanges = tk.Button(
    text="Apply Changes",
    width=15,
    height=5,
    command=applyChangesFunc
)
submit = tk.Button(
    text="Start Painting! (Press Q to quit)",
    width=25,
    height=5,
    bg="gray",
    fg="white",
    command=startPaint,
    wraplength=100
)
settings = tk.Label(
    text=settingstext.format(opacity=opacity, watercolor=watercolor),
    width=30,
    height=1
)

entryLabel.grid(row = 0, column = 1)
opacLabel.grid(row = 1, column = 0)
opacEntry.grid(row = 1, column = 2)
watercolorLabel.grid(row = 2, column = 0)
watercolorEntry.grid(row = 2, column = 2)

applyChanges.grid(row = 3, column = 1)
settings.grid(row = 4, column = 1)
submit.grid(row = 5, column = 1)
window.mainloop()