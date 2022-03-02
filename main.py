import pygame
import random

pygame.init()
pygame.display.set_caption("Kinda Blue")
screen = pygame.display.set_mode((800,600))
x = 0
y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if(x >= 800 ):
        x = 0
        y = y + 4
    if y >= 600:
        y = 0         
    r = random.randint(2, 10)
    screen.fill((135,206,235))
    pygame.draw.circle(screen, (0, 0, 150), (x,y), r)
    pygame.display.flip()        
    x = x + 2