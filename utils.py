__author__ = 'KerTakanov'


class Position:
    """Permet de créer une position pour un objet."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x, self.y
