import pygame

pygame.init()
pygame.mixer.music.load(r"C:\Users\almat\PycharmProjects\sanji\week7TSIS7\music\mockinbird.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    # Check if music is still playing
    pygame.time.Clock().tick(10)
