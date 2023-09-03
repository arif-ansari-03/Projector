import pygame
import projector

pygame.init()

def update(pd):
    if pd[0]:
        camera.updatePos(0, 10, 0)
    if pd[1]:
        camera.updatePos(0, -10, 0)
    if pd[2]:
        camera.updatePos(10, 0, 0)
    if pd[3]:
        camera.updatePos(-10, 0, 0)
    if pd[4]:
        camera.updatePos(0, 0, 10)
    if pd[5]:
        camera.updatePos(0, 0,-10)    

h = 500
w = 1000
Screen = projector.Screen(h, w)

pygameScreen = pygame.display.set_mode((w, h))
running = True
points = [projector.Point(h/2 - 250, w/2, 1000, (255, 0, 0, 0)),
          projector.Point(h/2 - 250, w/2, 750, (255, 0, 0, 0)),
          projector.Point(h/2 - 250, w/2, 500, (255, 0, 0, 0)),
          projector.Point(h/2 - 250, w/2, 250, (255, 0, 0, 0)),
          projector.Point(h/2 + 250, w/2, 1000, (255, 0, 0, 0)),
          projector.Point(h/2 + 250, w/2, 750, (255, 0, 0, 0)),
          projector.Point(h/2 + 250, w/2, 500, (255, 0, 0, 0)),
          projector.Point(h/2 + 250, w/2, 250, (255, 0, 0, 0))]
camera = projector.Camera(h/2,w/2, 0, 200)

pd = [False, False, False, False, False, False]
while running:
    pygameScreen.fill((0, 0, 0, 0))
    Screen.update(camera, points, pygameScreen)
    # print(camera.x, camera.y, camera.z)
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pd[0] = Truezzzzz
            if event.key == pygame.K_w:
                pd[1] = True
            if event.key == pygame.K_d:
                pd[2] = True
            if event.key == pygame.K_a:
                pd[3] = True
            if event.key == pygame.K_z:
                pd[4] = True
            if event.key == pygame.K_x:
                pd[5] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                pd[0] = False
            if event.key == pygame.K_w:
                pd[1] = False
            if event.key == pygame.K_d:
                pd[2] = False
            if event.key == pygame.K_a:
                pd[3] = False
            if event.key == pygame.K_z:
                pd[4] = False
            if event.key == pygame.K_x:
                pd[5] = False

        update(pd)

        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    pygame.display.update()