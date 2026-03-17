import pygame

# Инициализация звукового микшера pygame
pygame.mixer.init()

# Загрузка звука поедания фрукта
fruit_eat = pygame.mixer.Sound("C:\Users\student\Documents\GitHub\3m0k1d\home-and-class-work\pythonProject12\pythonProject1\eating-a-bite-of-an-apple.wav")
# Установка громкости звука поедания (0.5 = 50%)
fruit_eat.set_volume(0.5)

# Загрузка фоновой музыки
main_music = pygame.mixer.Sound("C:\Users\student\Documents\GitHub\3m0k1d\home-and-class-work\pythonProject12\pythonProject1\retro-dreamscape_92772.ogg")
# Установка громкости фоновой музыки (0.1 = 10%)
main_music.set_volume(0.1)