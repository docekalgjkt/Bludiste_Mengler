class Maze:
    def __init__(self, filename):
        self.maze = self.load_maze(filename)
        self.start_position = None

    def load_maze(self, filename):
        with open(filename, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]

    def set_start_position(self, x, y):
        if self.maze[y][x] == ' ':
            self.start_position = (x, y)
        else:
            print("Zadaná pozice není průchodná. Zkuste jinou pozici.")

    def display_maze(self):
        for row in self.maze:
            print(''.join(row))

    def is_valid_move(self, x, y):
        if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):
            return self.maze[y][x] in [' ', 'E']
        return False

    def find_exit(self, algorithm='dfs'):
        if not self.start_position:
            print("Nejprve musíte nastavit startovní pozici.")
            return False

        start_x, start_y = self.start_position
        visited = set()

        if algorithm == 'dfs':
            return self.dfs(start_x, start_y, visited)
        elif algorithm == 'bfs':
            return self.bfs(start_x, start_y)
        else:
            print(f"Neznámý algoritmus: {algorithm}")
            return False

    def dfs(self, x, y, visited):
        if self.maze[y][x] == 'E':
            print("Východ nalezen!")
            return True

        visited.add((x, y))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # dolů, doprava, nahoru, doleva

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                if self.dfs(new_x, new_y, visited):
                    return True

        return False

    def bfs(self, start_x, start_y):
        from collections import deque
        queue = deque([(start_x, start_y)])
        visited = set()
        visited.add((start_x, start_y))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # dolů, doprava, nahoru, doleva

        while queue:
            x, y = queue.popleft()
            if self.maze[y][x] == 'E':
                print("Východ nalezen!")
                return True

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

        print("Východ nelze nalézt z této pozice.")
        return False


def main():
    print("Vítejte v simulaci bludiště!")
    filename = input("Zadejte název souboru s bludištěm (např. bludiste1.txt): ")
    maze = Maze(filename)

    maze.display_maze()

    x = int(input("Zadejte startovní X pozici robota: "))
    y = int(input("Zadejte startovní Y pozici robota: "))

    maze.set_start_position(x, y)

    algorithm = input("Zvolte algoritmus (dfs/bfs): ")
    maze.find_exit(algorithm)


if __name__ == "__main__":
    main()
