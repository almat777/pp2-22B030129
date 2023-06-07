import pygame
pygame.init()

pygame.image.load(r"images\background\background.jpg")

WIDTH, HEIGHT = 700, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()