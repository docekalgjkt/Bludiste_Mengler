import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Definice velikosti políčka v GUI
CELL_SIZE = 40


class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bludiště")
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.load_maze_button = tk.Button(self.root, text="Načíst bludiště", command=self.load_maze)
        self.load_maze_button.pack()

        self.start_button = tk.Button(self.root, text="Spustit robota", command=self.start_robot)
        self.start_button.pack()

        self.maze = []
        self.robot_position = None
        self.exit_position = None

    def load_maze(self):
        # Funkce pro načtení bludiště ze souboru
        maze_file = filedialog.askopenfilename(title="Vyber soubor bludiště", filetypes=[("Textové soubory", "*.txt")])
        if maze_file:
            self.read_maze_from_file(maze_file)
            self.draw_maze()

    def read_maze_from_file(self, file_path):
        # Načti bludiště z textového souboru
        with open(file_path, 'r') as file:
            self.maze = [list(line.strip()) for line in file.readlines()]
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'R':
                    self.robot_position = (x, y)
                elif cell == 'E':
                    self.exit_position = (x, y)

    def draw_maze(self):
        # Vyčisti plátno
        self.canvas.delete("all")

        # Nakresli bludiště
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                x1, y1 = x * CELL_SIZE, y * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE

                if cell == '#':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")  # Zeď
                elif cell == 'E':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")  # Východ
                elif cell == 'R':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")  # Robot
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")  # Prázdné políčko

    def start_robot(self):
        if self.robot_position is None or self.exit_position is None:
            messagebox.showerror("Chyba", "Chybí startovní nebo cílová pozice!")
            return

        path_found = self.solve_maze()
        if path_found:
            messagebox.showinfo("Výsledek", "Robot našel cestu k východu!")
        else:
            messagebox.showinfo("Výsledek", "Robot nenašel cestu k východu.")

    def solve_maze(self):
        # Použijeme BFS pro hledání cesty
        from collections import deque

        queue = deque([self.robot_position])
        visited = set()
        visited.add(self.robot_position)

        while queue:
            x, y = queue.popleft()

            if (x, y) == self.exit_position:
                return True  # Našli jsme východ

            # Prozkoumej sousední políčka
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(self.maze[0]) and 0 <= ny < len(self.maze) and (nx, ny) not in visited:
                    if self.maze[ny][nx] in (' ', 'E'):
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        return False  # Nenašli jsme východ


# Hlavní část programu
if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
