from typing import List, Tuple

class Bludiste:
    def __init__(self, bludiste: List[List[int]]):
        # 1 = zeď, 0 = volné pole, 2 = východ, 3 = start
        self.bludiste = bludiste
        self.start = self.najdiStart()
        self.cil = self.najdiCil()

    def jeVolno(self, souradnice: Tuple[int, int]) -> bool:
        x, y = souradnice
        return self.bludiste[y][x] == 0 or self.bludiste[y][x] == 3  # Start je také volný

    def getSirka(self) -> int:
        return len(self.bludiste[0])

    def getVyska(self) -> int:
        return len(self.bludiste)

    def getRozmery(self) -> Tuple[int, int]:
        return self.getSirka(), self.getVyska()

    def jeVychod(self, souradnice: Tuple[int, int]) -> bool:
        x, y = souradnice
        return self.bludiste[y][x] == 2

    def najdiStart(self) -> Tuple[int, int]:
        for y, radek in enumerate(self.bludiste):
            for x, hodnota in enumerate(radek):
                if hodnota == 3:
                    return (x, y)
        raise ValueError("Start není definován v bludišti.")

    def najdiCil(self) -> Tuple[int, int]:
        for y, radek in enumerate(self.bludiste):
            for x, hodnota in enumerate(radek):
                if hodnota == 2:
                    return (x, y)
        raise ValueError("Cíl není definován v bludišti.")
