import tkinter as tk
from Bludiste import Bludiste
from BludisteView import BludisteView
class BludisteApp:
    def __init__(self, root: tk.Tk, bludiste: Bludiste, rozmerPolicka: int):
        self.root = root
        self.canvas = tk.Canvas(root, width=bludiste.getSirka() * rozmerPolicka,
                                height=bludiste.getVyska() * rozmerPolicka)
        self.canvas.pack()

        # Vytvoří objekt BludisteView a vykreslí ho na plátno
        self.bludisteView = BludisteView(bludiste, rozmerPolicka)
        self.bludisteView.setCanvas(self.canvas)
        self.bludisteView.vykresli(self.canvas)

# Příklad bludiště: 0 = volná cesta, 1 = stěna
bludiste_data = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

# Inicializace a spuštění aplikace
root = tk.Tk()
bludiste = Bludiste(bludiste_data)
app = BludisteApp(root, bludiste, 40)
root.mainloop()
