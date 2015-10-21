import pygame
import engine_render.render as render
import utils

__author__ = 'KerTakanov'


class Asset:
    """Contient une image identifiée par un nom."""
    def __init__(self, path: str, name='', pos=utils.Position(0, 0)):
        """

        :type pos: utils.Position or tuple(x, y)
        :type path: string
        """

        if not isinstance(pos, utils.Position):
            pos = utils.Position(pos[0], pos[1])

        self.path = path
        self.name = name
        self.image = pygame.image.load(path)
        self.pos = pos

    def update(self, dt=0):
        self.pos.update()
        render.draw(self)
