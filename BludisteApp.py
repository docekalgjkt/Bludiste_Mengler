# BludisteApp.py

from tkinter import Tk, Canvas
from typing import List
from Bludiste import Bludiste
from BludisteView import BludisteView

class BludisteApp:
    def __init__(self, bludiste_data: List[List[int]], rozmerPolicka: int = 20):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=800)
        self.canvas.pack()

        self.bludiste = Bludiste(bludiste_data)
        self.bludisteView = BludisteView(self.bludiste, rozmerPolicka)
        self.bludisteView.setCanvas(self.canvas)

    def spustit(self):
        self.bludisteView.vykresli()
        self.root.mainloop()


# Data pro složitější bludiště: 1 = zeď, 0 = volno, 2 = cíl, 3 = start
if __name__ == "__main__":
    bludiste_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    app = BludisteApp(bludiste_data, rozmerPolicka=50)
    app.spustit()
