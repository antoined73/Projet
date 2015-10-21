__author__ = 'KerTakanov'

"""C'est ici que l'on éxecute tous nos tests."""

if __name__ == "__main__":
    import engine_render as er
    import pygame
    import time
    import utils

    screen = pygame.display.set_mode((700, 600))

    asset = er.asset.Asset("assets/projectiles/bullet.bmp", pos=(200, 100))

    temps = 0
    close = False

    while not close:
        t = time.time()

        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

        screen.fill((0, 0, 0))

        asset.pos += (1, 2)
        er.render.draw(asset)
        pygame.display.flip()

        # time management
        dt = time.time() - t
        deltat = pygame.time.delay(int((1/60) * 1000) - int(dt*1000))