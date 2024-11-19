#ZATIM NEFUNGUJE




from tkinter import Tk, Canvas
from MazeDAO import MazeDAO  # Používáme MazeDAO, který podporuje TXT, CSV, XML
from BludisteView import BludisteView

class BludisteApp:
    def __init__(self, dao):
        self.root = Tk()
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)

        # Načtení bludiště jako instance třídy Bludiste
        self.bludiste = dao.load_maze()  # Tento řádek vrací instanci Bludiste
        self.bludisteView = BludisteView(self.bludiste)
        self.bludisteView.setCanvas(self.canvas)

        self.canvas.bind("<Configure>", self.update_view)

    def update_view(self, event):
        window_width = event.width
        window_height = event.height

        # Získání rozměrů bludiště
        sirka, vyska = self.bludiste.getRozmery()
        # Určení velikosti políčka tak, aby se bludiště přizpůsobilo velikosti okna
        rozmerPolicka = min(window_width // sirka, window_height // vyska)

        self.bludisteView.rozmerPolicka = rozmerPolicka
        self.bludisteView.vykresli()

    def spustit(self):
        self.root.mainloop()

if __name__ == "__main__":
    dao = MazeDAO("maze.xml")
    app = BludisteApp(dao)
    app.spustit()
