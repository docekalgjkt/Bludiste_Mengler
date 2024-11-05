# BludisteApp.py

from tkinter import Tk, Canvas
from MazeDAOXML import MazeDAOXML  # Použití XML DAO
from BludisteView import BludisteView

class BludisteApp:
    def __init__(self, dao):
        self.root = Tk()
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)  # Nastaví plné roztáhnutí na okno

        # Načteme bludiště pomocí DAO
        self.bludiste = dao.load_maze()
        self.bludisteView = BludisteView(self.bludiste)
        self.bludisteView.setCanvas(self.canvas)

        # Posluchač události pro změnu velikosti okna
        self.canvas.bind("<Configure>", self.update_view)

    def update_view(self, event):
        # Získáme aktuální rozměry okna
        window_width = event.width
        window_height = event.height

        # Vypočítáme rozměr políčka podle velikosti okna a rozměrů bludiště
        sirka, vyska = self.bludiste.getRozmery()
        rozmerPolicka = min(window_width // sirka, window_height // vyska)

        # Aktualizujeme rozměr políčka a překreslíme bludiště
        self.bludisteView.rozmerPolicka = rozmerPolicka
        self.bludisteView.vykresli()

    def spustit(self):
        self.root.mainloop()


if __name__ == "__main__":
    dao = MazeDAOXML("maze.xml")  # Načítáme bludiště z XML
    app = BludisteApp(dao)
    app.spustit()
