import pygame
import random
import math

# Настройки
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE, BLACK, RED = (255, 255, 255), (10, 10, 15), (255, 0, 0)
GREEN, BLUE, YELLOW, PURPLE = (0, 255, 100), (0, 150, 255), (255, 255, 0), (200, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)

# Игрок и Босс
player_pos = [WIDTH // 2, HEIGHT - 50]
bullets = []
bug_pos, bug_speed, bug_hp = [WIDTH // 2, 80], [4, 0], 50

# Помощники и суперудар
minions = []
minion_bullets = []
lasers = []
spawn_timer = 0
laser_timer = 0
kills = 0
super_effect_timer = 0

# Бонус уровень
bonus_mode = False
bonus_items = []
bonus_score = 0


def draw_ui():
    if not bonus_mode:
        status = "ГОТОВ (Пробел!)" if kills >= 5 else f"Заряд: {kills}/5"
        hp_text = font.render(f"HP БОССА: {bug_hp} | СУПЕРУДАР: {status}", True, WHITE)
    else:
        hp_text = font.render(f"БОНУС УРОВЕНЬ! СОБРАНО: {bonus_score}", True, YELLOW)
    screen.blit(hp_text, (10, 10))


running = True
while running:
    screen.fill(BLACK)
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not bonus_mode:
            bullets.append([list(player_pos), [0, -10]])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and kills >= 5 and not bonus_mode:
                bug_hp -= 10
                kills = 0
                super_effect_timer = 10

    player_pos = list(pygame.mouse.get_pos())

    if bug_hp > 0:
        # ПРОВЕРКА КАСАНИЯ БОССА (ТРОЯН)
        boss_rect = pygame.Rect(bug_pos[0] - 25, bug_pos[1] - 25, 50, 50)
        if boss_rect.collidepoint(player_pos):
            screen.fill((50, 0, 0))
            error_font = pygame.font.SysFont("Courier", 32, bold=True)
            msg = error_font.render("КРИТИЧЕСКАЯ ОШИБКА: ВЗЛОМ ТРОЯНОМ НАЧАЛСЯ!", True, RED)
            screen.blit(msg, (WIDTH // 2 - 350, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        # Логика Босса
        bug_pos[0] += bug_speed[0]
        if bug_pos[0] < 50 or bug_pos[0] > WIDTH - 50: bug_speed[0] *= -1

        laser_timer += dt
        if laser_timer > 1500:
            lasers.append([list(bug_pos), list(player_pos), 40, 10])
            laser_timer = 0

        # Логика пуль игрока
        for b in bullets[:]:
            b[0][1] += b[1][1]
            if math.hypot(b[0][0] - bug_pos[0], b[0][1] - bug_pos[1]) < 30:
                bug_hp -= 1
                if b in bullets: bullets.remove(b)
                continue
            for m in minions[:]:
                if math.hypot(b[0][0] - m[0], b[0][1] - m[1]) < 20:
                    m[2] -= 1
                    if b in bullets: bullets.remove(b)
                    if m[2] <= 0:
                        minions.remove(m)
                        kills += 1
            if b[0][1] < 0 and b in bullets: bullets.remove(b)

        # Логика помощников
        spawn_timer += dt
        if spawn_timer > 10000:
            for i in range(5):
                minions.append([random.randint(100, WIDTH - 100), random.randint(150, 300), 3])
            spawn_timer = 0

        for m in minions:
            if random.random() < 0.01:
                minion_bullets.append([[m[0], m[1]], [random.uniform(-2, 2), 3]])

        for mb in minion_bullets[:]:
            mb[0][0] += mb[1][0]
            mb[0][1] += mb[1][1]
            if math.hypot(mb[0][0] - player_pos[0], mb[0][1] - player_pos[1]) < 15:
                running = False
            if mb[0][1] > HEIGHT: minion_bullets.remove(mb)

        # Логика лучей
        for l in lasers[:]:
            if l[2] > 0:
                pygame.draw.line(screen, WHITE, l[0], l[1], 1)
                l[2] -= 1
            elif l[3] > 0:
                pygame.draw.line(screen, RED, l[0], l[1], 6)
                d = abs((l[1][1] - l[0][1]) * player_pos[0] - (l[1][0] - l[0][0]) * player_pos[1] + l[1][0] * l[0][1] -
                        l[1][1] * l[0][0]) / (math.hypot(l[1][1] - l[0][1], l[1][0] - l[0][0]) + 0.1)
                if d < 12: running = False
                l[3] -= 1
            else:
                lasers.remove(l)
    else:
        # ЛОГИКА БОНУСНОГО УРОВНЯ
        bonus_mode = True
        if random.random() < 0.05:
            bonus_items.append([random.randint(20, WIDTH - 20), -20])

        for item in bonus_items[:]:
            item[1] += 5
            if math.hypot(item[0] - player_pos[0], item[1] - player_pos[1]) < 30:
                bonus_score += 1
                bonus_items.remove(item)
            elif item[1] > HEIGHT:
                bonus_items.remove(item)

    # Отрисовка суперудара
    if super_effect_timer > 0:
        pygame.draw.circle(screen, PURPLE, bug_pos, 100, 5)
        screen.fill((50, 0, 50), special_flags=pygame.BLEND_RGB_ADD)
        super_effect_timer -= 1

    # ОТРИСОВКА ИГРОКА (ЖУК)
    px, py = player_pos
    pygame.draw.line(screen, GREEN, (px - 20, py - 10), (px + 20, py + 10), 2)
    pygame.draw.line(screen, GREEN, (px - 20, py + 10), (px + 20, py - 10), 2)
    pygame.draw.ellipse(screen, GREEN, (px - 15, py - 20, 30, 40))
    pygame.draw.circle(screen, WHITE, (px - 7, py - 12), 3)
    pygame.draw.circle(screen, WHITE, (px + 7, py - 12), 3)

    # Отрисовка объектов
    if bug_hp > 0:
        pygame.draw.rect(screen, RED, (bug_pos[0] - 25, bug_pos[1] - 25, 50, 50))
        for m in minions: pygame.draw.circle(screen, YELLOW, (m[0], m[1]), 15)
        for b in bullets: pygame.draw.circle(screen, BLUE, (int(b[0][0]), int(b[0][1])), 5)
        for mb in minion_bullets: pygame.draw.circle(screen, YELLOW, (int(mb[0][0]), int(mb[0][1])), 8)
    else:
        # Отрисовка бонусов
        for item in bonus_items:
            pygame.draw.circle(screen, YELLOW, (item[0], item[1]), 10)
            pygame.draw.circle(screen, WHITE, (item[0], item[1]), 10, 2)
        win_text = font.render(f"ПОБЕДА! СОБИРАЙ БОНУСЫ: {bonus_score}", True, GREEN)
        screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2))

    draw_ui()
    pygame.display.flip()

pygame.quit()