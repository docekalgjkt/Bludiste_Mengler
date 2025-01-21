from tkinter import Canvas
from Robot import Robot

class RobotView:
    """
    Třída zajišťuje vizualizaci robota v bludišti na zadaném Canvasu.
    """

    def __init__(self, robot: Robot, barva: str = "red"):
        """
        Inicializace třídy RobotView.
        parametr: robot: Instance třídy Robot, která obsahuje data o aktuální pozici robota.
        parametr: barva: Barva, která se použije pro zobrazení robota (výchozí hodnota je "red").
        """
        self.robot = robot  # Reference na instanci robota
        self.barva = barva  # Barva pro vykreslení robota
        self.sprite = None  # ID grafického objektu na Canvasu (pro mazání a aktualizace)

    def vykresli(self, canvas: Canvas, rozmerPolicka: int):
        """
        Vykreslí robota na Canvasu na základě jeho aktuální pozice.
        parametr: canvas: Instance tkinter.Canvas, kde se robot vykreslí.
        parametr: rozmerPolicka: Velikost jednoho políčka v pixelech.
        """
        # Pokud již existuje sprite robota, smaže ho z Canvasu
        if self.sprite:
            canvas.delete(self.sprite)

        # Získá aktuální pozici robota
        x, y = self.robot.pozice

        # Vytvoří grafickou reprezentaci robota jako ovál
        self.sprite = canvas.create_oval(
            x * rozmerPolicka + 2,  # Levý horní roh X (s odsazením)
            y * rozmerPolicka + 2,  # Levý horní roh Y (s odsazením)
            (x + 1) * rozmerPolicka - 2,  # Pravý dolní roh X (s odsazením)
            (y + 1) * rozmerPolicka - 2,  # Pravý dolní roh Y (s odsazením)
            fill=self.barva  # Nastaví barvu oválu
        )
