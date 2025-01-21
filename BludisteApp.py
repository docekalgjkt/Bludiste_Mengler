from tkinter import Tk, Canvas, filedialog, messagebox
from MazeDAO import MazeDAO
from BludisteView import BludisteView
from Robot import Robot
from RobotView import RobotView


class BludisteApp:
    """
    Hlavní třída aplikace pro vizualizaci a simulaci bludiště s robotem.
    """

    def __init__(self):
        """
        Inicializace aplikace, vytvoření hlavního okna, plátna a načtení bludiště.
        """
        self.root = Tk()
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)  # Plátno vyplní celé okno

        self.bludiste = None  # Instance bludiště
        self.bludisteView = None  # Vizualizace bludiště
        self.robot = None  # Robot pohybující se v bludišti
        self.robotView = None  # Vizualizace robota

        self.vyber_a_nacti_bludiste()  # Načteme bludiště při spuštění aplikace

        # Aktualizace zobrazení při změně velikosti okna
        self.canvas.bind("<Configure>", self.update_view)

        # Spuštění automatického pohybu robota po načtení bludiště
        self.automatickyPohyb()

    def vyber_a_nacti_bludiste(self):
        """
        Otevře dialogové okno pro výběr souboru s bludištěm a načte jeho obsah.
        """
        try:
            # Dialog pro výběr souboru
            soubor = filedialog.askopenfilename(
                title="Vyberte soubor s bludištěm",
                filetypes=(("Textové soubory", "*.txt"), ("CSV soubory", "*.csv"), ("XML soubory", "*.xml"))
            )
            if not soubor:
                # Pokud není vybrán žádný soubor, ukončí aplikaci
                messagebox.showinfo("Ukončení", "Nebyl vybrán žádný soubor. Aplikace se ukončí.")
                self.root.destroy()
                return

            # Načtení bludiště pomocí DAO třídy
            dao = MazeDAO(soubor)
            self.bludiste = dao.load_maze()

            # Vizualizace bludiště
            self.bludisteView = BludisteView(self.bludiste)
            self.bludisteView.setCanvas(self.canvas)

            # Inicializace robota a jeho vizualizace
            self.robot = Robot(self.bludiste)
            self.robotView = RobotView(self.robot)

            # Aktualizace zobrazení
            self.update_view()

        except Exception as e:
            # Chybová zpráva a ukončení aplikace při selhání
            messagebox.showerror("Chyba", f"Chyba při načítání bludiště: {e}")
            self.root.destroy()

    def update_view(self, event=None):
        """
        Aktualizuje zobrazení bludiště a pozice robota na základě aktuálních dat.
        parametr: event: Událost změny velikosti okna (nepovinné).
        """
        if not self.bludiste:
            return  # Pokud není bludiště načteno, ukončí metodu

        # Získání aktuálních rozměrů okna
        window_width = self.canvas.winfo_width()
        window_height = self.canvas.winfo_height()

        # Výpočet velikosti políčka na základě rozměrů okna
        sirka, vyska = self.bludiste.getRozmery()
        rozmerPolicka = min(window_width // sirka, window_height // vyska)

        # Aktualizace velikosti políček ve vizualizaci bludiště
        self.bludisteView.rozmerPolicka = rozmerPolicka
        self.bludisteView.vykresli()

        # Vykreslení robota na aktuální pozici
        if self.robot and self.robotView:
            self.robotView.vykresli(self.canvas, self.bludisteView.rozmerPolicka)

    def spustit(self):
        """
        Spustí hlavní smyčku aplikace Tkinter.
        """
        if self.bludiste:
            self.root.mainloop()

    def automatickyPohyb(self):
        """
        Automatický pohyb robota v bludišti. Funkce se volá rekurzivně každých 100 ms.
        """
        if self.robot:
            if not self.robot.cesta:
                # Pokud robot nemá vypočítanou cestu, najde ji
                self.robot.najdiCestu()
                if not self.robot.cesta:
                    # Pokud cesta není nalezena, ukončí pohyb
                    messagebox.showinfo("Chyba", "Cesta nebyla nalezena.")
                    return

            if self.robot.pohniSe():
                # Robot se posunul na nové políčko
                print(f"Robot se automaticky pohybuje na pozici: {self.robot.pozice}")
                self.update_view()  # Aktualizace zobrazení
            else:
                # Robot dosáhl cíle
                print("Robot dosáhl cíle!")
                self.update_view()
                return

            # Pokračování v pohybu za 100 ms
            self.root.after(100, self.automatickyPohyb)


if __name__ == "__main__":
    app = BludisteApp()
    app.spustit()
