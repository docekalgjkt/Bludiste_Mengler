from tkinter import Tk, Canvas, filedialog, messagebox
from MazeDAO import MazeDAO
from BludisteView import BludisteView


class BludisteApp:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)

        self.bludiste = None
        self.bludisteView = None

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

    def spustit(self):
        if self.bludiste:  # Spustí hlavní smyčku jen pokud bylo bludiště načteno
            self.root.mainloop()


if __name__ == "__main__":
    app = BludisteApp()
    app.spustit()
