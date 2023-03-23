import pygame
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
ball_size = 50
ball_radius = 25
ball_x = 375
ball_y = 275
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= 20
                if ball_y < 0:
                    ball_y = 0
            elif event.key == pygame.K_DOWN:
                ball_y += 20
                if ball_y > height - ball_size:
                    ball_y = height - ball_size
            elif event.key == pygame.K_LEFT:
                ball_x -= 20
                if ball_x < 0:
                    ball_x = 0
            elif event.key == pygame.K_RIGHT:
                ball_x += 20
                if ball_x > width - ball_size:
                    ball_x = width - ball_size
    screen.fill('white')
    pygame.draw.circle(screen, 'red', (ball_x + ball_radius, ball_y + ball_radius), ball_radius)
    pygame.display.update()
pygame.quit()
