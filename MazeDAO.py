from Bludiste import Bludiste
from typing import List


class MazeDAO:
    def __init__(self, soubor: str):
        self.soubor = soubor

    def load_maze(self) -> Bludiste:
        # Načtení bludiště v požadovaném formátu (txt, xml, csv)
        maze_data = self.nacti_soubor()
        print("Načtené bludiště:", maze_data)  # Testovací výpis pro ladění
        return Bludiste(maze_data)

    def nacti_soubor(self) -> List[List[int]]:
        # Kód pro načtení souboru a vytvoření seznamu seznamů (2D matice)
        if self.soubor.endswith('.txt'):
            return self._load_txt_maze()
        elif self.soubor.endswith('.csv'):
            return self._load_csv_maze()
        elif self.soubor.endswith('.xml'):
            return self._load_xml_maze()
        else:
            raise ValueError("Nepodporovaný formát souboru.")

    def _load_txt_maze(self) -> List[List[int]]:
        with open(self.soubor, 'r') as file:
            return [[int(x) for x in line.split()] for line in file]

    def _load_csv_maze(self) -> List[List[int]]:
        import csv
        with open(self.soubor, 'r') as file:
            reader = csv.reader(file)
            return [[int(x) for x in row] for row in reader]

    def _load_xml_maze(self) -> List[List[int]]:
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.soubor)
        root = tree.getroot()

        # Ověření správnosti formátu XML
        maze = []
        for row in root.findall('row'):
            try:
                maze.append([int(cell) for cell in row.text.split()])
            except ValueError:
                raise ValueError("Chybný formát XML: řádky musí obsahovat pouze čísla oddělená mezerami.")

        if not maze:
            raise ValueError("Bludiště z XML je prázdné.")

        return maze
