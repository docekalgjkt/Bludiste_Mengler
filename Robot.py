from typing import Tuple, List
from Bludiste import Bludiste
from collections import deque

class Robot:
    def __init__(self, bludiste: Bludiste):
        self.bludiste = bludiste
        self.pozice = bludiste.start
        self.cesta = []

    def jePlatnyTah(self, souradnice: Tuple[int, int]) -> bool:
        x, y = souradnice
        # Zkontrolujte, zda souřadnice spadají do platného rozsahu pomocí metod z Bludiste
        if 0 <= x < self.bludiste.getSirka() and 0 <= y < self.bludiste.getVyska():
            # Zkontrolujte hodnotu bludiště na dané pozici
            return self.bludiste.bludiste[y][x] == 0 or self.bludiste.bludiste[y][x] == 3
        return False

    def najdiCestu(self):
        start = self.bludiste.start
        cil = self.bludiste.cil

        if hasattr(self, 'cesta') and self.cesta:
            return self.cesta

        queue = [(start, [])]  # (pozice, aktuální cesta)
        visited = set()  # Záznam navštívených pozic

        while queue:
            current_position, path = queue.pop(0)  # BFS - pop z fronty

            print(f"Procházím pozici: {current_position}, cesta: {path}")

            if current_position == cil:
                self.cesta = path + [current_position]
                print(f"Cesta byla nalezena: {self.cesta}")
                return self.cesta

            visited.add(current_position)

            for next_position in self.getSousedniPozice(current_position):
                if next_position not in visited and self.bludiste.jeVolno(next_position):
                    print(f"Přidávám pozici {next_position} do fronty")
                    queue.append((next_position, path + [current_position]))

        self.cesta = []  # Pokud cesta není nalezena
        print("Cesta nebyla nalezena.")
        return self.cesta

    def getSousedniPozice(self, pozice):
        x, y = pozice
        sousedni = []
        # Směry: nahoru, dolů, vlevo, vpravo
        if y > 0: sousedni.append((x, y - 1))  # nahoru
        if y < self.bludiste.getVyska() - 1: sousedni.append((x, y + 1))  # dolů
        if x > 0: sousedni.append((x - 1, y))  # vlevo
        if x < self.bludiste.getSirka() - 1: sousedni.append((x + 1, y))  # vpravo
        return sousedni

    def pohniSe(self):
        if self.cesta:  # Pokud máme cestu
            nova_pozice = self.cesta.pop(0)  # Získejte další pozici z cesty
            self.pozice = nova_pozice  # Aktualizujte pozici robota
            print(f"Robot se pohybuje na pozici: {self.pozice}")

            if self.pozice == self.bludiste.cil:  # Pokud jsme dosáhli cíle
                print("Cíl dosažen!")
                return False  # Zastavit pohyb, protože cíl byl dosažen
            return True  # Pokračovat v pohybu
        else:
            print("Cesta nebyla nalezena.")
            return False  # Pokud není cesta, pohyb se nezahájí





