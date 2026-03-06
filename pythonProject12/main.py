import pygame
from settings import *
from sudoku.generator import generate_sudoku
from sudoku.board import Board
from ui.grid import draw_grid
from ui.cell import draw_cells, init
from ui.button import Button

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()

restart_button = Button( #Кнопка рестарта игры
    WINDOW_SIZE // 2 - 60,
    WINDOW_SIZE + 20,
    120,
    40,
    "Restart")

def new_game():
    grid = generate_sudoku()
    return Board(grid)

board = new_game()

init()

board = Board(generate_sudoku())

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                board.place_number(event.key - pygame.K_0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if restart_button.clicked(pos):
                board = new_game()
                continue

            if pos[1] < WINDOW_SIZE:
                x, y = pos
                board.select(y // CELL_SIZE, x // CELL_SIZE)

    screen.fill(WHITE) # Фон экрана
    draw_cells(screen, board) # Клетки с цифрами
    draw_grid(screen) # Сетка
    restart_button.draw(screen) # Кнопка рестарта игры
    pygame.display.flip() # Обновление экрана

pygame.quit()