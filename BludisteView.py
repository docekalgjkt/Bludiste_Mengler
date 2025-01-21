from tkinter import Canvas
from Bludiste import Bludiste

class BludisteView:
    """
    Třída zajišťuje vizualizaci bludiště na zadaném Canvasu.
    """

    def __init__(self, bludiste: Bludiste, rozmerPolicka: int = 35):
        """
        Inicializace třídy BludisteView.
        parametr: bludiste: Instance třídy Bludiste, která obsahuje data o bludišti.
        parametr: rozmerPolicka: Velikost jednoho políčka v pixelech (výchozí hodnota je 35).
        """
        self.bludiste = bludiste  # Reference na data bludiště
        self.rozmerPolicka = rozmerPolicka  # Velikost políčka v pixelech
        self.canvas = None  # Canvas, na kterém se bude bludiště vykreslovat

    def setCanvas(self, canvas: Canvas):
        """
        Nastaví Canvas, na kterém se bude bludiště vykreslovat.
        parametr: canvas: Instance tkinter.Canvas.
        """
        self.canvas = canvas
        self._update_canvas_size()  # Aktualizace velikosti canvasu na základě rozměrů bludiště

    def _update_canvas_size(self):
        """
        Nastaví velikost canvasu podle rozměrů bludiště a velikosti políček.
        """
        sirka, vyska = self.bludiste.getRozmery()  # Získá šířku a výšku bludiště
        if self.canvas is not None:
            self.canvas.config(
                width=sirka * self.rozmerPolicka,  # Šířka canvasu v pixelech
                height=vyska * self.rozmerPolicka  # Výška canvasu v pixelech
            )

    def vykresli(self):
        """
        Vykreslí bludiště na nastaveném Canvasu.
        """
        if self.canvas is None:
            print("Canvas není nastaven.")  # Kontrola, zda byl nastaven Canvas
            return

        self.canvas.delete("all")  # Vymaže všechny prvky z Canvasu

        sirka, vyska = self.bludiste.getRozmery()  # Získá rozměry bludiště

        # Prochází jednotlivé buňky bludiště a vykresluje je na Canvas
        for y in range(vyska):
            for x in range(sirka):
                # Určí barvu podle typu buňky
                barva = "white"  # Výchozí barva pro volné pole
                if self.bludiste.bludiste[y][x] == 1:
                    barva = "black"  # Zeď
                elif self.bludiste.bludiste[y][x] == 2:
                    barva = "green"  # Cíl
                elif self.bludiste.bludiste[y][x] == 3:
                    barva = "blue"  # Start

                # Vytvoří obdélník na Canvasu odpovídající aktuální buňce
                self.canvas.create_rectangle(
                    x * self.rozmerPolicka,  # Levý horní roh X
                    y * self.rozmerPolicka,  # Levý horní roh Y
                    (x + 1) * self.rozmerPolicka,  # Pravý dolní roh X
                    (y + 1) * self.rozmerPolicka,  # Pravý dolní roh Y
                    fill=barva  # Nastaví barvu podle typu buňky
                )
