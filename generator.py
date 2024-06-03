'''
1. Лабиринт - список списков
[
    ['1', '0', '█'],
    ['█', '░', '█'],
    ['█', '░', '█'],
]

2. Полностью заполняем лабиринт стенами

3. Количество колонн и рядов - нечетное

4. Бульдозер начинает в четной клетке

5. Если в двух клетках от него стены - ломает обе

6. Лабиринт проходми, когда в четных нет стен

7. Внутренний лабиринт очертить границами - стенами

8. Все четные свободны - выход (0, любая четная)
'''

import random

COLS = 77
ROWS = 59 

WALL = '█'
EMPTY = '░'
EXIT = 'X'


class Maze:
    def __init__(self,
                 rows: int,
                 cols: int) -> None:
        self.wall_sprite = '█'
        self.empty_sprite = '█'
        self.exit_sprite = '█'
        self.map = [[WALL for column in range(cols)] for row in range(rows)]

    def is_passable(self) -> None:
        pass


class Bulldozer:
    def __init__(self,
                 maze: Maze) -> None:
        self.bulldozer_col = random.choice(range(0, COLS, 2))
        self.bulldozer_row = random.choice(range(0, ROWS, 2))
        self.maze = maze
        self.directions = []

    def get_directions(self) -> None:
        while self.maze.is_passable():
            pass

    def bulid_maze(self) -> None:
        pass


def build_maze() -> None:
    maze = [[WALL for column in range(COLS)] for row in range(ROWS)]
    bulldozer_col = random.choice(range(0, COLS, 2))
    bulldozer_row = random.choice(range(0, ROWS, 2))
    maze[bulldozer_row][bulldozer_col] = EMPTY
    for i in range(1000000):  # Остановить цикл, когда сломаны все четные
        bulldozer_directions = []
        if bulldozer_col + 2 < COLS:
            bulldozer_directions.append('right')
        if bulldozer_col - 2 >= 0:
            bulldozer_directions.append('left')
        if bulldozer_row + 2 < ROWS:
            bulldozer_directions.append('down')
        if bulldozer_row - 2 >= 0:
            bulldozer_directions.append('up')

        if not bulldozer_directions:
            print('Нет свободных направлений')
            break

        direction = random.choice(bulldozer_directions)
        if direction == 'right':
            if maze[bulldozer_row][bulldozer_col + 2] == WALL:
                maze[bulldozer_row][bulldozer_col + 1] = EMPTY
                maze[bulldozer_row][bulldozer_col + 2] = EMPTY
            bulldozer_col += 2
        elif direction == 'left':
            if maze[bulldozer_row][bulldozer_col - 2] == WALL:
                maze[bulldozer_row][bulldozer_col - 1] = EMPTY
                maze[bulldozer_row][bulldozer_col - 2] = EMPTY
            bulldozer_col -= 2
        elif direction == ('down'):
            if maze[bulldozer_row + 2][bulldozer_col] == WALL:
                maze[bulldozer_row + 1][bulldozer_col] = EMPTY
                maze[bulldozer_row + 2][bulldozer_col] = EMPTY
            bulldozer_row += 2
        elif direction == 'up':
            if maze[bulldozer_row - 2][bulldozer_col] == WALL:
                maze[bulldozer_row - 1][bulldozer_col] = EMPTY
                maze[bulldozer_row - 2][bulldozer_col] = EMPTY
            bulldozer_row -= 2
    maze[0][COLS-1] = EXIT
    return maze

