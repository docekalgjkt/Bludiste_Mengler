# MazeDAOXML.py

import xml.etree.ElementTree as ET
from typing import List
from Bludiste import Bludiste


class MazeDAOXML:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_maze(self) -> Bludiste:
        tree = ET.parse(self.filepath)
        root = tree.getroot()

        bludiste_data: List[List[int]] = []
        for row in root.findall("row"):
            values = [int(val) for val in row.text.strip().split()]
            bludiste_data.append(values)

        return Bludiste(bludiste_data)
