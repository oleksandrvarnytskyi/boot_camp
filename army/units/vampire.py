from unit import Unit
from weapon.weapon import Fangs


class Vampire(Unit):
    def __init__(self, name='Vampire', hit_points_limit=120):
        Unit.__init__(self, name, hit_points_limit)
        self.weapon = Fangs(self)
        self.vampire_state()
        self.current_state.name = name

    def take_magic_damage(self, magic_damage):
        self.current_state.take_damage(magic_damage)

    def take_damage(self, dmg):
        self.current_state.take_damage(dmg)
        self.add_hit_points(dmg/5)

    def change_state(self):
        pass
