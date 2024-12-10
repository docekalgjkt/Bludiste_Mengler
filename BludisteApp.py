from tkinter import Tk, Canvas, filedialog, messagebox
from MazeDAO import MazeDAO
from BludisteView import BludisteView
from Robot import Robot
from RobotView import RobotView

class BludisteApp:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)

        self.bludiste = None
        self.bludisteView = None
        self.robot = None
        self.robotView = None

        self.vyber_a_nacti_bludiste()  # Načteme bludiště při spuštění

        self.canvas.bind("<Configure>", self.update_view)

    def vyber_a_nacti_bludiste(self):
        try:
            # Otevře dialogové okno pro výběr souboru
            soubor = filedialog.askopenfilename(
                title="Vyberte soubor s bludištěm",
                filetypes=(("Textové soubory", "*.txt"), ("CSV soubory", "*.csv"), ("XML soubory", "*.xml"))
            )
            if not soubor:
                messagebox.showinfo("Ukončení", "Nebyl vybrán žádný soubor. Aplikace se ukončí.")
                self.root.destroy()  # Zavře aplikaci, pokud není vybrán žádný soubor
                return

            dao = MazeDAO(soubor)
            self.bludiste = dao.load_maze()

            # Vytvoří nový BludisteView s nově načteným bludištěm
            self.bludisteView = BludisteView(self.bludiste)
            self.bludisteView.setCanvas(self.canvas)

            # Vytvoření robota a jeho vizualizace
            self.robot = Robot(self.bludiste)
            self.robotView = RobotView(self.robot)

            # Překreslí okno s novým bludištěm
            self.update_view()

        except Exception as e:
            messagebox.showerror("Chyba", f"Chyba při načítání bludiště: {e}")
            self.root.destroy()  # Zavře aplikaci při chybě

    def update_view(self, event=None):
        if not self.bludiste:
            return  # Pokud není bludiště načteno, nic nedělej

        window_width = self.canvas.winfo_width()
        window_height = self.canvas.winfo_height()

        sirka, vyska = self.bludiste.getRozmery()
        rozmerPolicka = min(window_width // sirka, window_height // vyska)

        self.bludisteView.rozmerPolicka = rozmerPolicka
        self.bludisteView.vykresli()

        # Vykreslení robota
        if self.robot and self.robotView:
            self.robotView.vykresli(self.canvas, self.bludisteView.rozmerPolicka)

    def pohniRobotem(self):
        """
        Posune robota o jeden krok a překreslí okno.
        """
        if self.robot.pohniSe():
            self.update_view()
        else:
            messagebox.showinfo("Informace", "Robot dosáhl cíle nebo není možné pokračovat.")

    def spustit(self):
        if self.bludiste:
            self.root.after(100, self.automatickyPohyb)  # Automatický pohyb robota (volitelné)
            self.root.mainloop()

    def automatickyPohyb(self):
        if self.robot and self.robot.pohniSe():
            self.update_view()
            self.root.after(100, self.automatickyPohyb)

if __name__ == "__main__":
    app = BludisteApp()
    app.spustit()
