import pygame

__author__ = 'KerTakanov'
"""Contient une image identifiée par un nom"""


class Asset:
    def __init__(self, path, name=''):
        assert isinstance(path, str)
        self.path = path
        self.name = name
        self.image = pygame.image.load(path)
