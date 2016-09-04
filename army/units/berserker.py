from unit import Unit
from weapon.weapon import Axe


class Berserker(Unit):
    def __init__(self, name='Berserker', hit_points_limit=180):
        Unit.__init__(self, name, hit_points_limit)
        self.weapon = Axe(self)

    def take_magic_damage(self, magic_damage):
        if self.current_state.is_transformed:
            self.take_magic_damage(magic_damage)

    def add_hit_points(self, hp):
        if self.current_state.is_transformed:
            self.current_state.add_hit_points(hp)
