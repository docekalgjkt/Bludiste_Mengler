from typing import List, Tuple

# Třída pro bludiště
class Bludiste:
    def __init__(self, bludiste: List[List[int]]):
        self.bludiste = bludiste

    # Zkontroluje, zda je na daných souřadnicích volné místo (0 je volno, 1 je stěna)
    def jeVolno(self, souradnice: Tuple[int, int]) -> bool:
        x, y = souradnice
        return self.bludiste[y][x] == 0

    # Vrátí šířku bludiště
    def getSirka(self) -> int:
        return len(self.bludiste[0])

    # Vrátí výšku bludiště
    def getVyska(self) -> int:
        return len(self.bludiste)

    # Vrátí rozměry bludiště jako tuple (šířka, výška)
    def getRozmery(self) -> Tuple[int, int]:
        return (self.getSirka(), self.getVyska())

    # Zkontroluje, zda jsou souřadnice východem (poslední bod bludiště)
    def jeVychod(self, souradnice: Tuple[int, int]) -> bool:
        return souradnice == (self.getSirka() - 1, self.getVyska() - 1)
