import pygame, random
from pygame.locals import *
from pygame.time import Clock

def on_grid_random():
  x= random.randint(0,59)
  y= random.randint(0,59)
  return(x* 10, y * 10) #Uma divisão inteira, para gerar um número inteiro e multiplo de 10

def collision(c1, c2):
  return(c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600)) #tupla para definir a dimensão da tela. Uma matiz de 600 por 500 px. O 0,0 é em cima e cresce de cima para baixo e da esquerda pra direita.
pygame.display.set_caption('Cobrinha') #comando usado para dar o nome do arquivo

snake = [(200,200), (210,200), (220,200)] #A cobra é uma lista de segmentos. Cada segmento vai ser representado por uma tupla, um valor de x e y onde está posicionado aquele quadrado
snake_skin = pygame.Surface((10,10)) #Definir o tamanho do quadradinho
snake_skin.fill((255,255,255)) #Definir a cor rgb. Ai é branco

apple_pos = on_grid_random() #Uma posição aleatória para a maçã, porém alinhados com a cobra
apple = pygame.Surface((10,10)) #Definir o tamanho da maçã
apple.fill((255,105,180)) #Definir a cor rgb. Aí é rosa


my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0 #contador dos pontos

game_over = False

while not game_over:
  clock.tick(10)
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
    snake.append((0,0))
    score += 1

  if snake[0][0] == 600 or snake[0][1]==600 or snake[0][0] < 0 or snake [0][1] < 0: #Para checar se a cobrinha bate nas bordas
    game_over = True
    break

  for c in range(1, len(snake) -1): #Para ver se a cobrinha bate nela mesma
    if snake[0][0] == snake[c][0] and snake[0][1] == snake[c][1]:
      game_over = True
      break

  if game_over:
    break
  
  for i in range(len(snake) - 1, 0, -1):
    snake[i] = (snake[i-1][0], snake[i-1][1])

  if my_direction == UP:
    snake[0] =(snake[0][0], snake[0][1] - 10)
  if my_direction == DOWN:
    snake[0] =(snake[0][0], snake[0][1] + 10)
  if my_direction == RIGHT:
    snake[0] =(snake[0][0] + 10, snake[0][1])
  if my_direction == LEFT:
    snake[0] =(snake[0][0] - 10, snake[0][1])

  screen.fill((0,0,0)) #Serve para limpar a tela, já que ela vai ser atualizada várias vezes por segundo
  screen.blit(apple, apple_pos)

  score_font = font.render('Score: %s' % (score), True,(255,255,255))
  score_rect = score_font.get_rect()
  score_rect.topleft = (600 - 120, 10)
  screen.blit(score_font, score_rect)
  
  for pos in snake:
    screen.blit(snake_skin, pos)

  pygame.display.update()

while True:
  game_over_font= pygame.font.Font('freesansbold.ttf', 75)
  game_over_screen = game_over_font.render('Game Over', True, (219,112,147))
  game_over_rect = game_over_screen.get_rect()
  game_over_rect.midtop = (300, 10)
  screen.blit(game_over_screen, game_over_rect)
  pygame.display.update()
  pygame.time.wait(500)
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()

