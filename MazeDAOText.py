from typing import List
from Bludiste import Bludiste

class MazeDAOText:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_maze(self) -> Bludiste:
        bludiste_data: List[List[int]] = []
        with open(self.filepath, "r") as file:
            for line in file:
                row = [int(x) for x in line.strip()]
                bludiste_data.append(row)
        return Bludiste(bludiste_data)
