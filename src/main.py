import pygame
import projector

pygame.init()

h = 500
w = 1000
Screen = projector.Screen(h, w)

pygameScreen = pygame.display.set_mode((w, h))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    pygame.display.update()