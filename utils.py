__author__ = 'KerTakanov'


class Position:
    """Permet de cr�er une position pour un objet."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x, self.y

    def __add__(self, other):
        _other = other
        if isinstance(other, tuple):
            _other = Position(other[0], other[1])

        return Position(self.x + _other.x, self.y + _other.y)

    def __iadd__(self, other):
        _other = other
        if isinstance(other, tuple):
            _other = Position(other[0], other[1])

        self.x += _other.x
        self.y += _other.y

        return self

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
