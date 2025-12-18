from lib2to3.pgen2.token import NUMBER

import pygame
import random
from pygame import K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN
from pygame.examples.go_over_there import SCREEN_SIZE
from pygame.examples.grid import TITLE
from pygame.examples.midi import BACKGROUNDCOLOR
from pygame.examples.video import backgrounds

from py2048_classes import Board
from  pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#задаем цвета для игровых полей
TEXT_DARK = pygame.Color(119, 110, 100)
TEXT_LIGHT =pygame.Color(255, 255, 255)
BACKGROUND =pygame.Color(188, 173, 159)
EMPTY =pygame.Color(206, 192, 179)
TITLE_MAX =pygame.Color(18, 91, 146)
#ЗАДАЕМ ЦВЕТА ДЛЯ ТЕКСТА
CELL_STYLES = {
0:{"fotn":TEXT_DARK, "fill":EMPTY},
1:{'fotn':TEXT_DARK, 'fill':pygame.Color(239,229,218)},
2:{'fotn':TEXT_DARK, 'fill':pygame.Color(238,225,199)},
3:{'fotn':TEXT_DARK, 'fill':pygame.Color(242,177,121)},
4:{'fotn':TEXT_DARK, 'fill':pygame.Color(245,149,99)},
5:{'fotn':TEXT_DARK, 'fill':pygame.Color(247,127,96)},
6:{'fotn':TEXT_DARK, 'fill':pygame.Color(246,94,59)},
7:{'fotn':TEXT_DARK, 'fill':pygame.Color(241,219,147)},
8:{'fotn':TEXT_DARK, 'fill':pygame.Color(237,204,97)},
9:{'fotn':TEXT_DARK, 'fill':pygame.Color(235,193,57)},
10:{'fotn':TEXT_DARK, 'fill':pygame.Color(231,181,23)},
11:{'fotn':TEXT_DARK, 'fill':pygame.Color(192,154,16)},
12:{'fotn':TEXT_DARK, 'fill':pygame.Color(94,218,146)},
13:{'fotn':TEXT_DARK, 'fill':pygame.Color(37,187,100)},
14:{'fotn':TEXT_DARK, 'fill':pygame.Color(35,140,81)},
15:{'fotn':TEXT_DARK, 'fill':pygame.Color(113,100,213)},
16:{'fotn':TEXT_DARK, 'fill':pygame.Color(25,130,205)},
}
BORDER_WIDTH = 10
TITLE_SIZE = 100
NUMBER_OF_ROWS = NUMBER_OF_COLUMNS = 4
SCREEN_WIDTH = SCREEN_HEIGHT = ((NUMBER_OF_ROWS+1)*BORDER_WIDTH) + (NUMBER_OF_COLUMNS * TITLE_SIZE)
FONT_SIZE = 24
class Tile(pygame.sprite.Sprite):
    def __init__(self, row, colum, walue=None):
        super(Tile, self).__init__()
        self.font= pygame.font.Font(pygame.font.get_default_font(),FONT_SIZE)
        self.x_pos= BORDER_WIDTH + (row *(BORDER_WIDTH + TITLE_SIZE))
        self.y_pos=BORDER_WIDTH + (colum *(BORDER_WIDTH + TITLE_SIZE))
        self.surface= pygame.Surface((TITLE_SIZE, TITLE_SIZE))
        self.value= value
        self.update(value)
        def update(self, value):
            self.change_fill(value)
            self.change_text(value)
            self.value = value
            def change_fill(self,value):
                if value:
                    if value in  CELL_STYLES[value]["fill"]
                    else:
                        fill_colour= TITLE_MAX
                else:
                    fill_colour =EMPTY
                self.surface.fill(fill_colour)

    def change_text(self, value):
        if value:
            if value in CELL_STYLES:
                text_colour = CELL_STYLES[value]["font"]
            else:
                text_colour = TEXT_LIGHT
            text_surface = self.font.render(str(2**value), True, text_colour,None)
            text_rectangle = text_surface.get_rect(center=(TITLE_SIZE/2, TITLE_SIZE/2))
            self.surface.blit((text_surface,text_rectangle))
class Game:
    def __init__(self):
        self.all_tiles = pygame.sprite.Group
        self.screen.fill(backgrounds)
        self.tiles =self.initialise_tiles()
        self.draw_tiles()
    def initialisalise_tile(self):
        tiles = []
        for row in range (0, NUMBER_OF_ROWS):
            row_of_tiles = []
            for column in range(0, NUMBER_OF_COLUMNS):
                tile = Tile(row, column)
                row_of_tiles.append(tile)
                self.all_tiles.add(tile)
            tiles.append(row_of_tiles)
        return tiles
    def draw_tiles(self):
        for tile in self.all_tiles:
            self.screen.blit(tile.surface,(tile.x_pos, tile.y_pos))
        def update_tiles(self,tile_values):
