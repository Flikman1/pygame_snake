import pygame
from random import randrange
pygame.init()
RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dris = {'W': True, 'S': True, 'D': True, 'A': True,}

length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 7
k = 0

sc = pygame.display.set_mode([RES, RES])
font = pygame.font.Font('Fonts/Font1.ttf', 30)
font_end = pygame.font.Font('Fonts/Font1.ttf', 70)
mouse = pygame.mouse.get_pos()
text_restart = font_end.render('RESTART', True, 'orange')
text_restart_rect = text_restart.get_rect(topleft=(200, 400))
clock = pygame.time.Clock()
game = False
while not game:
    sc.fill(pygame.Color('black'))

    text_score = font.render(f'SCORE:  {k}', True, 'orange')
    sc.blit(text_score, (10, 10))
    #creating snake, apple
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j,SIZE, SIZE ))) for i, j, in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    #snake move
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while not game:
            text_end = font_end.render('GAME OVER', True, 'orange')
            sc.blit(text_restart, text_restart_rect)
            sc.blit(text_end, (200, 300))

            if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                game = True
                k = 0
                x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)


            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()



    #eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1
        k += 1
    pygame.display.update()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dris['W']:
        dx, dy = 0, -1
        dris = {'W': True, 'S': False, 'D': True, 'A': True, }
    elif key[pygame.K_s] and dris['S']:
        dx, dy = 0, 1
        dris = {'W': False, 'S': True, 'D': True, 'A': True, }
    elif key[pygame.K_a] and dris['A']:
        dx, dy = -1, 0
        dris = {'W': True, 'S': True, 'D': False, 'A': True, }
    elif key[pygame.K_d] and dris['D']:
        dx, dy = 1, 0
        dris = {'W': True, 'S': True, 'D': True, 'A': False, }

