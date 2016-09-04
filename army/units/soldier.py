from unit import Unit
from weapon.weapon import Sword


class Soldier(Unit):
    def __init__(self, name='Soldier', hit_points_limit=100):
        Unit.__init__(self, name, hit_points_limit)
        self.weapon = Sword(self)

if __name__ == '__main__':
    soldier = Soldier()
    print soldier
