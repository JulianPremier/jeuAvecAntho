import pygame
import tkinter as tk
import os


class Menu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.skinColor = None

    def create_widgets(self):
        self.skinColor = tk.Button(self)
        self.skinColor["text"] = "skin color"
        self.skinColor["command"] = self.getNewSkinColor
        self.skinColor.pack(side="top")

    def getNewSkinColor(self):
        os.system("cls")
        print("select your R G B level :")
        R = int(input("R (0 - 255) >> "))
        G = int(input("G (0 - 255) >> "))
        B = int(input("B (0 - 255) >> "))
        newColor = pygame.Color(R, G, B)
        engine.setSkinColor(newColor)