from typing import Tuple, List
from Bludiste import Bludiste
from collections import deque

class Robot:
    """
    Třída reprezentuje robota, který se pohybuje v bludišti.
    """

    def __init__(self, bludiste: Bludiste):
        """
        Inicializace robota.
        parametr: bludiste: Instance třídy Bludiste reprezentující bludiště.
        """
        self.bludiste = bludiste  # Reference na bludiště
        self.pozice = bludiste.start  # Výchozí pozice robota
        self.cesta = []  # Naplánovaná cesta robota

    def jePlatnyTah(self, souradnice: Tuple[int, int]) -> bool:
        """
        Zkontroluje, zda je tah na dané souřadnice platný.
        parametr: souradnice: Souřadnice cílového pole (x, y).
        return: True, pokud je tah platný, jinak False.
        """
        x, y = souradnice
        # Zkontroluje, zda souřadnice jsou v rozmezí a pole je průchodné
        if 0 <= x < self.bludiste.getSirka() and 0 <= y < self.bludiste.getVyska():
            return self.bludiste.bludiste[y][x] == 0 or self.bludiste.bludiste[y][x] == 3
        return False

    def najdiCestu(self):
        """
        Najde cestu z výchozího bodu na cíl pomocí algoritmu BFS.
        return: Seznam souřadnic reprezentujících cestu nebo prázdný seznam, pokud cesta neexistuje.
        """
        start = self.bludiste.start
        cil = self.bludiste.cil

        # Pokud je cesta již vypočítaná, vrátí ji
        if hasattr(self, 'cesta') and self.cesta:
            return self.cesta

        queue = [(start, [])]  # Fronta: (aktuální pozice, dosavadní cesta)
        visited = set()  # Množina navštívených pozic

        while queue:
            current_position, path = queue.pop(0)  # Odebere první prvek z fronty

            print(f"Procházím pozici: {current_position}, cesta: {path}")

            if current_position == cil:
                # Pokud jsme dosáhli cíle, uložíme cestu
                self.cesta = path + [current_position]
                print(f"Cesta byla nalezena: {self.cesta}")
                return self.cesta

            visited.add(current_position)  # Označíme pozici jako navštívenou

            # Přidáme sousední pozice, které jsou volné, do fronty
            for next_position in self.getSousedniPozice(current_position):
                if next_position not in visited and self.bludiste.jeVolno(next_position):
                    print(f"Přidávám pozici {next_position} do fronty")
                    queue.append((next_position, path + [current_position]))

        # Pokud nebyla nalezena cesta
        self.cesta = []
        print("Cesta nebyla nalezena.")
        return self.cesta

    def getSousedniPozice(self, pozice: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Vrátí seznam sousedních pozic pro danou pozici.
        parametr: pozice: Aktuální pozice (x, y).
        return: Seznam sousedních pozic.
        """
        x, y = pozice
        sousedni = []
        # Směry pohybu: nahoru, dolů, vlevo, vpravo
        if y > 0:
            sousedni.append((x, y - 1))  # nahoru
        if y < self.bludiste.getVyska() - 1:
            sousedni.append((x, y + 1))  # dolů
        if x > 0:
            sousedni.append((x - 1, y))  # vlevo
        if x < self.bludiste.getSirka() - 1:
            sousedni.append((x + 1, y))  # vpravo
        return sousedni

    def pohniSe(self) -> bool:
        """
        Posune robota na další pozici v cestě.
        return: True, pokud se robot posune, False pokud již dosáhl cíle nebo nemá cestu.
        """
        if self.cesta:  # Pokud existuje naplánovaná cesta
            nova_pozice = self.cesta.pop(0)  # Získejte další pozici
            self.pozice = nova_pozice  # Aktualizujte pozici robota
            print(f"Robot se pohybuje na pozici: {self.pozice}")

            if self.pozice == self.bludiste.cil:  # Kontrola, zda jsme dosáhli cíle
                print("Cíl dosažen!")
                return False  # Pohyb končí, protože robot je na cíli
            return True  # Robot se posunul a může pokračovat
        else:
            print("Cesta nebyla nalezena.")
            return False  # Pokud není cesta, robot se nepohne
