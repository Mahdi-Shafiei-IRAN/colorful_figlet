import os, pyfiglet, random, time
from .lists import *
from pyfiglet import Figlet
from termcolor import colored

def show_fonts():
    """
    return list of fonts in list.py
    """
    return FONTS

def show_colors():
    """
    return list of colors in lists.py
    """
    return COLORS

def figlet(text, font = "", color = ""):
    """
    main func in program and change text to figlet shapes
    """
    os.system("cls")
    figlet_text = ""

    if font and font in FONTS:
            f = Figlet(font=font)
    else:
            f = Figlet(font=random.choice(FONTS))
    tmp = f.renderText(text)

    if color and color in COLORS:
        zcolor = color
    else:
        zcolor = random.choice(COLORS)
    for i in tmp:
        if i == "\n" and (not color or not color in COLORS):
            zcolor = random.choice(COLORS)
        elif i == "\n" and color in COLORS:
            zcolor = color
        figlet_text += colored(i,color=zcolor)
    return figlet_text
