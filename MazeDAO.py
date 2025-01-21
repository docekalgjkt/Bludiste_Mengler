from Bludiste import Bludiste
from typing import List


class MazeDAO:
    """
    Třída MazeDAO slouží k načítání dat bludiště z různých typů souborů
    a jejich převodu na instanci třídy Bludiste.
    """

    def __init__(self, soubor: str):
        """
        Inicializuje instanci třídy MazeDAO s cestou k souboru.
        parametr: soubor: Cesta k souboru s daty bludiště.
        """
        self.soubor = soubor

    def load_maze(self) -> Bludiste:
        """
        Načte bludiště ze souboru a vytvoří instanci třídy Bludiste.
        return: Objekt třídy Bludiste.
        """
        maze_data = self.nacti_soubor()
        print("Načtené bludiště:", maze_data)  # Ladicí výpis načteného bludiště
        return Bludiste(maze_data)

    def nacti_soubor(self) -> List[List[int]]:
        """
        Detekuje formát souboru podle přípony a načte data bludiště.
        return: Dvourozměrný seznam reprezentující bludiště.
        """
        if self.soubor.endswith('.txt'):
            return self._load_txt_maze()
        elif self.soubor.endswith('.csv'):
            return self._load_csv_maze()
        elif self.soubor.endswith('.xml'):
            return self._load_xml_maze()
        else:
            raise ValueError("Nepodporovaný formát souboru.")  # Chyba při neznámé příponě

    def _load_txt_maze(self) -> List[List[int]]:
        """
        Načte bludiště z textového souboru, kde každá řádka obsahuje čísla oddělená mezerami.
        return: Dvoumístný seznam reprezentující bludiště.
        """
        with open(self.soubor, 'r') as file:
            return [[int(x) for x in line.split()] for line in file]

    def _load_csv_maze(self) -> List[List[int]]:
        """
        Načte bludiště z CSV souboru, kde každá řádka obsahuje čísla oddělená čárkami.
        return: Dvoumístný seznam reprezentující bludiště.
        """
        import csv
        with open(self.soubor, 'r') as file:
            reader = csv.reader(file)
            return [[int(x) for x in row] for row in reader]

    def _load_xml_maze(self) -> List[List[int]]:
        """
        Načte bludiště z XML souboru, kde každá řádka je reprezentována elementem <row>.
        return: Dvoumístný seznam reprezentující bludiště.
                ValueError: Pokud XML soubor obsahuje chybný formát nebo je prázdný.
        """
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.soubor)  # Načte XML soubor
        root = tree.getroot()

        maze = []
        for row in root.findall('row'):
            try:
                # Převede text elementu na seznam čísel
                maze.append([int(cell) for cell in row.text.split()])
            except ValueError:
                raise ValueError("Chybný formát XML: řádky musí obsahovat pouze čísla oddělená mezerami.")

        if not maze:
            raise ValueError("Bludiště z XML je prázdné.")  # Chyba při prázdném bludišti

        return maze
