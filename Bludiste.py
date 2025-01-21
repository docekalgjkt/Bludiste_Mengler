from typing import List, Tuple

class Bludiste:
    """
    Třída pro reprezentaci bludiště, které je definováno jako 2D seznam.
    Hodnoty v bludišti:
    - 1: zeď
    - 0: volné pole
    - 2: východ
    - 3: start
    """

    def __init__(self, bludiste: List[List[int]]):
        """
        Inicializace bludiště, hledání startu a cíle.
        parametr bludiste: 2D seznam reprezentující bludiště.
        """
        self.bludiste = bludiste

        # Najde startovní a cílovou pozici.
        self.start = self.najdiStart()
        self.cil = self.najdiCil()

    def jeVolno(self, souradnice: Tuple[int, int]) -> bool:
        """
        Kontroluje, zda je na zadaných souřadnicích možné se pohybovat.
        parametr souradnice: Souřadnice ve formátu (x, y).
        return: True, pokud je možné vstoupit na dané pole, jinak False.
        """
        x, y = souradnice
        # Povolit pohyb na volné pole (0), startovní pole (3) nebo cíl (2)
        return self.bludiste[y][x] == 0 or self.bludiste[y][x] == 3 or self.bludiste[y][x] == 2

    def getSirka(self) -> int:
        """
        Vrací šířku bludiště (počet sloupců).
        return: Šířka bludiště.
        """
        return len(self.bludiste[0])

    def getVyska(self) -> int:
        """
        Vrací výšku bludiště (počet řádků).
        return: Výška bludiště.
        """
        return len(self.bludiste)

    def getRozmery(self) -> Tuple[int, int]:
        """
        Vrací rozměry bludiště (šířka, výška).
        return: Dvojice (šířka, výška).
        """
        return self.getSirka(), self.getVyska()

    def jeVychod(self, souradnice: Tuple[int, int]) -> bool:
        """
        Kontroluje, zda jsou zadané souřadnice východem z bludiště.
        parametr souradnice: Souřadnice ve formátu (x, y).
        return: True, pokud je pole východ, jinak False.
        """
        x, y = souradnice
        return self.bludiste[y][x] == 2

    def najdiStart(self) -> Tuple[int, int]:
        """
        Najde startovní pozici v bludišti (hodnota 3).
        return: Souřadnice startovní pozice (x, y).
                ValueError: Pokud není start definován.
        """
        for y, radek in enumerate(self.bludiste):
            for x, hodnota in enumerate(radek):
                if hodnota == 3:
                    return (x, y)
        raise ValueError("Start není definován v bludišti.")

    def najdiCil(self) -> Tuple[int, int]:
        """
        Najde cílovou pozici v bludišti (hodnota 2).
        return: Souřadnice cílové pozice (x, y).
                ValueError: Pokud není cíl definován.
        """
        for y, radek in enumerate(self.bludiste):
            for x, hodnota in enumerate(radek):
                if hodnota == 2:
                    return (x, y)
        raise ValueError("Cíl není definován v bludišti.")
