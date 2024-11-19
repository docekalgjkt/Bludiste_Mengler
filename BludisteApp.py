from tkinter import Tk, Canvas
from MazeDAO import MazeDAO
from BludisteView import BludisteView
class BludisteApp:
    def __init__(self, dao):
        self.root = Tk()
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)

        self.bludiste = dao.load_maze()
        self.bludisteView = BludisteView(self.bludiste)
        self.bludisteView.setCanvas(self.canvas)

        self.canvas.bind("<Configure>", self.update_view)

    def update_view(self, event):
        window_width = event.width
        window_height = event.height

        sirka, vyska = self.bludiste.getRozmery()
        rozmerPolicka = min(window_width // sirka, window_height // vyska)

        self.bludisteView.rozmerPolicka = rozmerPolicka
        self.bludisteView.vykresli()

    def spustit(self):
        self.root.mainloop()

if __name__ == "__main__":
    dao = MazeDAO("maze.csv")
    app = BludisteApp(dao)
    app.spustit()
