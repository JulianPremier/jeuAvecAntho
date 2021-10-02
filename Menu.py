import pygame
import tkinter as tk
from tkinter import messagebox
import os


class Menu(tk.Frame):
    def __init__(self, engine, master=None):
        self.engine = engine

        super().__init__(master)
        self.master = master
        self.master.title("MENU")
        self.master.minsize(250, 50)
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.pack(fill=tk.X)

        self.create_widgets()

        #config attribut
        self.closeWindow = True

    def create_widgets(self):
        """
        Create all widget the menu need

        :return: Void
        """

        #Skin color button
        self.skinColorButton = tk.Button(self)
        self.skinColorButton["text"] = "Skin color"
        self.skinColorButton["command"] = self.setSkinColorFromEngine
        self.skinColorButton.pack(fill=tk.X)

        #Pseudo button
        self.pseudoButton = tk.Button(self)
        self.pseudoButton["text"] = "Pseudo"
        self.pseudoButton["command"] = self.setPseudoTextFromEngine
        self.pseudoButton.pack(fill=tk.X)

        #Leave button
        self.quit = tk.Button(self)
        self.quit["text"] = "Leave"
        self.quit["command"] = self.master.destroy
        self.quit.pack(fill=tk.X)

    def closing(self):
        """
        Lock all action

        :return: Void
        """
        self.closeWindow = False
        self.skinColorButton["state"] = tk.DISABLED
        self.pseudoButton["state"] = tk.DISABLED
        self.quit["state"] = tk.DISABLED

    def opened(self):
        """
        Unlock all closed action

        :return: Void
        """
        self.closeWindow = True
        self.skinColorButton["state"] = tk.NORMAL
        self.pseudoButton["state"] = tk.NORMAL
        self.quit["state"] = tk.NORMAL

    def setSkinColorFromEngine(self):
        """
        Change skin color (use "setSkinColor" from Engine object) 

        :return: Void
        """

        self.closing()

        os.system("cls")
        print("select your R G B level :")
        try:
            R = int(input("R (0 - 255) >> "))
            G = int(input("G (0 - 255) >> "))
            B = int(input("B (0 - 255) >> "))
            newColor = pygame.Color(R, G, B)

            if(R > 255 or G > 255 or B > 255):
                raise ValueError
            else:
                self.engine.setSkinColor(newColor)

            os.system("cls")
            print("Color changed")

        except ValueError:
            os.system("cls")
            print("Bad value")
            print("Color unchanged")

        self.opened()

    def on_closing(self):
        """
        Check if Menu window can be destroy

        :return: Void
        """

        if(self.closeWindow == True):
            self.master.destroy()
        else:
            tk.messagebox.showwarning("WARNING", "the menu cant be close, u must end ur request.")

    def setPseudoTextFromEngine(self):
        """
        Change pseudo text (use "setPseudo" from Engine object) 

        :return: Void
        """
        self.closing()

        os.system("cls")
        print("Write your new pseudo : ")
        newPseudo = input("New pseudo >> ")

        if newPseudo == "":
            newPseudo = "Unknown"

        self.engine.setPseudo(newPseudo)

        os.system("cls")
        print("Pseudo changed")

        self.opened()
