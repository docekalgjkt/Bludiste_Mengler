from tkinter import Canvas
from Robot import Robot
class RobotView:
    def __init__(self, robot: Robot, barva: str = "red"):
        self.robot = robot
        self.barva = barva
        self.sprite = None

    def vykresli(self, canvas: Canvas, rozmerPolicka: int):
        if self.sprite:
            canvas.delete(self.sprite)

        x, y = self.robot.pozice
        self.sprite = canvas.create_oval(
            x * rozmerPolicka + 2,
            y * rozmerPolicka + 2,
            (x + 1) * rozmerPolicka - 2,
            (y + 1) * rozmerPolicka - 2,
            fill=self.barva
        )