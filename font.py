import tkinter as tk
import tkinter.font
import PySimpleGUI as psg

root= tk.Tk()

font=tkinter.font.families()

for i in range(len(font)):
    print(font[i])