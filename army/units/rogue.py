from unit import Unit
from weapon.weapon import Dagger


class Rogue(Unit):
    def __init__(self, name='Rogue', hit_points_limit=90):
        Unit.__init__(self, name, hit_points_limit)
        self.weapon = Dagger(self)
