from tkinter import Canvas
from Bludiste import Bludiste

class BludisteView:
    def __init__(self, bludiste: Bludiste, rozmerPolicka: int = 35):
        self.bludiste = bludiste
        self.rozmerPolicka = rozmerPolicka
        self.canvas = None

    def setCanvas(self, canvas: Canvas):
        self.canvas = canvas
        self._update_canvas_size()

    def _update_canvas_size(self):
        """
        Nastaví velikost canvasu na základě velikosti bludiště.
        """
        sirka, vyska = self.bludiste.getRozmery()
        if self.canvas is not None:
            self.canvas.config(
                width=sirka * self.rozmerPolicka,
                height=vyska * self.rozmerPolicka
            )

    def vykresli(self):
        if self.canvas is None:
            print("Canvas není nastaven.")
            return

        self.canvas.delete("all")

        sirka, vyska = self.bludiste.getRozmery()

        for y in range(vyska):
            for x in range(sirka):
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
