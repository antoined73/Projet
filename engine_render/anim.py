import iter_list
import utils
import engine_render.render as render

__author__ = 'KerTakanov'


class Anim:
    def __init__(self):
        self.list = iter_list.IterList()            
        self.anim_time = 0
        self.actual_anim_time = 0
        self.name = ""
        self.pos = utils.Position()

    def add_anim(self, asset):
        self.list.add(asset)

    def update(self, dt=0):
        self.actual_anim_time += dt

        if not self.list.is_none():
            if self.actual_anim_time >= self.anim_time:
                render.draw(self.list.next(), self.pos)
                self.actual_anim_time = 0
            else:
                render.draw(self.list.current(), self.pos)
