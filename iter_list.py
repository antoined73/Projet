__author__ = 'KerTakanov'


class IterList:
    def __init__(self):
        self.list = list()
        self.it = 0

    def add(self, element):
        self.list += [element]

    def current(self):
        return self.list[self.it] if self.list else None

    def next(self):
        if self.list:
            self.it = self.it + 1 if self.it < len(self.list) - 1 else 0
            return self.list[self.it]

        return None

    def is_none(self):
        return False if self.list else True
