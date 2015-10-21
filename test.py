__author__ = 'KerTakanov'

"""C'est ici que l'on éxecute tous nos tests."""

if __name__ == "__main__":
    import engine_render as er
    import pygame
    import time
    import utils

    screen = pygame.display.set_mode((700, 600))

    asset1 = er.asset.Asset("assets/running_1.png")
    asset2 = er.asset.Asset("assets/running_2.png")
    asset3 = er.asset.Asset("assets/running_3.png")

    anim = er.anim.Anim()
    anim.add_anim(asset1)
    anim.add_anim(asset2)
    anim.add_anim(asset3)
    anim.anim_time = 1000
    anim.pos = utils.Position(100, 100)

    temps = 0
    deltat = 0
    close = False

    while not close:
        t = time.time()

        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

        screen.fill((0, 0, 0))
        anim.update(deltat)
        pygame.display.flip()

        # time management
        dt = time.time() - t
        deltat = pygame.time.delay(int((1/60) * 1000) - int(dt*1000))