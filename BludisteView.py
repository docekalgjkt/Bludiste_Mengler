# BludisteView.py

from tkinter import Canvas
from Bludiste import Bludiste

class BludisteView:
    def __init__(self, bludiste: Bludiste, rozmerPolicka: int = 20):
        self.bludiste = bludiste
        self.rozmerPolicka = rozmerPolicka
        self.canvas = None

    def setCanvas(self, canvas: Canvas):
        self.canvas = canvas

    def vykresli(self):
        if self.canvas is None:
            print("Canvas není nastaven.")
            return

        for y in range(self.bludiste.getVyska()):
            for x in range(self.bludiste.getSirka()):
                barva = "white"
                if self.bludiste.bludiste[y][x] == 1:
                    barva = "black"  # Zeď
                elif self.bludiste.bludiste[y][x] == 2:
                    barva = "green"  # Cíl
                elif self.bludiste.bludiste[y][x] == 3:
                    barva = "blue"  # Start

                self.canvas.create_rectangle(
                    x * self.rozmerPolicka,
                    y * self.rozmerPolicka,
                    (x + 1) * self.rozmerPolicka,
                    (y + 1) * self.rozmerPolicka,
                    fill=barva
                )
