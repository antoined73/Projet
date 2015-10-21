import pygame
import logger
import threading

__author__ = 'KerTakanov'


class Render(threading.Thread):
    def __init__(self):
        logger.info("Render successfully created")


def draw(asset, position = None):
    if not position:
        position = asset.pos

    pygame.display.get_surface().blit(asset.image, position.to_tuple())


if __name__ == "__main__":
    import engine_render as er
    testasset = er.asset.Asset("assets/projectiles/bullet.bmp")
    render = Render()
    draw(testasset)
