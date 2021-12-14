import pygame
import random
from pygame.locals import *
from pygame.time import Clock


def on_grid_random():
    x = random.randint(0, 29)
    y = random.randint(2, 29)  # Para ficar abaixo dos indices de time e score
    return(x * 20, y * 20)  # Para gerar um número inteiro e multiplo de 10


def collision(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

tempo = 8

pygame.init()
# tupla para definir a dimensão da tela. Uma matiz de 600 por 500 px. O 0,0 é em cima e cresce de cima para baixo e da esquerda pra direita.
screen = pygame.display.set_mode((600, 600))
# comando usado para dar o nome do arquivo
pygame.display.set_caption('Cobrinha')

# A cobra é uma lista de segmentos. Cada segmento vai ser representado por uma tupla, um valor de x e y onde está posicionado aquele quadrado
snake = [(200, 200), (220, 200), (240, 200)]
snake_skin = pygame.Surface((20, 20))  # Definir o tamanho do quadradinho
snake_skin.fill((196, 16, 16))  # Definir a cor rgb. Ai é branco

# Uma posição aleatória para a maçã, porém alinhados com a cobra
apple_pos = on_grid_random()
apple = pygame.image.load('imagens/desenho_maca.png')  # Definir maçã

my_direction = LEFT

clock = pygame.time.Clock()  # Objeto criado para limitar o tempo da cobrinha

placar = {}  # Dicionario
placar["score"] = 0  # Para ver a potuação do jogador
placar["tempo_segundo"] = 0  # Para ver o tempo em segundo
timer = 1

# Definir fonte e tamanho das letras
fonte = pygame.font.Font('freesansbold.ttf', 18)
# Serve para definir a palavra que vai ser mostrada
time_fonte = fonte.render(
    'Time: ' + str(placar["tempo_segundo"]), True, (0, 0, 0))
time_rect = time_fonte.get_rect()
time_rect.topleft = (30, 10)  # Definir posição

game_over = False

while not game_over:  # Laço principal do jogo
    clock.tick(tempo)  # Quadros por segundo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        placar["score"] += 1

    # Para checar se a cobrinha bate nas bordas
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    for c in range(1, len(snake)):  # Para ver se a cobrinha bate nela mesma
        if snake[0][0] == snake[c][0] and snake[0][1] == snake[c][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 20, snake[0][1])

    if timer < tempo:  # Fazer a contagem do tempo em segundo
        timer += 1
    else:
        placar["tempo_segundo"] += 1
        time_fonte = fonte.render(
            'Time: ' + str(placar["tempo_segundo"]), True, (0, 0, 0))
        timer = 1

    screen.fill((200, 200, 200))  # Cor da tela
    screen.blit(apple, apple_pos)  # Serve para colocar na tela
    screen.blit(time_fonte, time_rect)

    font = pygame.font.Font('freesansbold.ttf', 18)
    score_font = font.render('Score: ' + str(placar["score"]), True, (0, 0, 0))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 0, 0))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (300, 250)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
