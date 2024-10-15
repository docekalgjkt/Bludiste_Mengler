class BludisteView:
    def __init__(self, bludiste: Bludiste, rozmerPolicka: int):
        self.bludiste = bludiste
        self.rozmerPolicka = rozmerPolicka

    # Nastavení plátna (canvas) pro vykreslení
    def setCanvas(self, canvas):
        self.canvas = canvas

    # Metoda pro vykreslení bludiště
    def vykresli(self, canvas):
        sirka, vyska = self.bludiste.getRozmery()
        for y in range(vyska):
            for x in range(sirka):
                color = "white" if self.bludiste.jeVolno((x, y)) else "black"
                canvas.create_rectangle(
                    x * self.rozmerPolicka, y * self.rozmerPolicka,
                    (x + 1) * self.rozmerPolicka, (y + 1) * self.rozmerPolicka,
                    fill=color
                )
