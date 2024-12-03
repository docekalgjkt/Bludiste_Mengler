from typing import Tuple, List
from Bludiste import Bludiste


class Robot:
    def __init__(self, bludiste: Bludiste):
        self.bludiste = bludiste
        self.pozice = bludiste.start
        self.cesta = []

    def jePlatnyTah(self, souradnice: Tuple[int, int]) -> bool:
        x, y = souradnice
        if 0 <= x < self.bludiste.getSirka() and 0 <= y < self.bludiste.getVyska():
            return self.bludiste.jeVolno((x, y))
        return False

    def najdiCestu(self):
        def dfs(pozice):
            if pozice in self.cesta:
                return False

            self.cesta.append(pozice)

            if self.bludiste.jeVychod(pozice):
                return True

            x, y = pozice
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nova_pozice = (x + dx, y + dy)
                if self.jePlatnyTah(nova_pozice):
                    if dfs(nova_pozice):
                        return True

            self.cesta.pop()
            return False

        dfs(self.pozice)

    def pohniSe(self) -> bool:
        if not self.cesta:
            self.najdiCestu()

        if self.cesta:
            self.pozice = self.cesta.pop(0)
            return True

        return False