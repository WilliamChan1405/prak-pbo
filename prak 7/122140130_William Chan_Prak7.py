import pygame

WIDTH, HEIGHT = 540, 540
ROWS, COLS = 9, 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FPS = 60
PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


class Sudoku:
    def __init__(self, puzzle):
        self.grid = puzzle
        self.selected = None

    def draw(self, win):
        # Draw grid lines
        gap = WIDTH / 9
        for i in range(1, 9):
            if i % 3 == 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, BLACK, (0, i * gap), (WIDTH, i * gap), thick)
            pygame.draw.line(win, BLACK, (i * gap, 0), (i * gap, HEIGHT), thick)

        for i in range(ROWS):
            for j in range(COLS):
                if self.grid[i][j] != 0:
                    self.draw_num(win, str(self.grid[i][j]), i, j)
        if self.selected:
            pygame.draw.rect(win, RED, (self.selected[1] * gap, self.selected[0] * gap, gap, gap), 3)

    def draw_num(self, win, num, row, col):
        font = pygame.font.Font(None, 40)
        gap = WIDTH / 9
        x = col * gap + (gap / 2 - 15)
        y = row * gap + (gap / 2 - 15)
        text = font.render(num, True, BLUE)
        win.blit(text, (x, y))

    def is_valid(self, num, pos):
        # Check row
        for i in range(ROWS):
            if self.grid[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(COLS):
            if self.grid[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.grid[i][j] == num and (i, j) != pos:
                    return False
        return True

    def solve(self):
        empty = find_empty(self.grid)
        if not empty:
            return True
        else:
            row, col = empty

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.grid[row][col] = i

                if self.solve():
                    return True

                self.grid[row][col] = 0

        return False


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
    return None


def draw_window(win, sudoku):
    win.fill(WHITE)
    sudoku.draw(win)
    pygame.display.update()


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    sudoku = Sudoku(PUZZLE)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // (WIDTH // 9)
                col = pos[0] // (WIDTH // 9)
                sudoku.selected = (row, col)
            if event.type == pygame.KEYDOWN:
                if sudoku.selected:
                    if event.key == pygame.K_BACKSPACE:
                        sudoku.grid[sudoku.selected[0]][sudoku.selected[1]] = 0
                    else:
                        if event.unicode.isdigit():
                            sudoku.grid[sudoku.selected[0]][sudoku.selected[1]] = int(event.unicode)
        draw_window(win, sudoku)

        if find_empty(sudoku.grid) is None and sudoku.solve():
            print("Sudoku solved successfully:")
            print_board(sudoku.grid)    
            run = False  
        pygame.quit()


if __name__ == "__main__":
    main()
