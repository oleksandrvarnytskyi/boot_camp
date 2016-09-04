from unit import Unit
from weapon.weapon import Sword
from weapon.weapon import Claws


class Werewolf(Unit):
    def __init__(self, name='Werewolf', hit_points_limit=120):
        Unit.__init__(self, name, hit_points_limit)
        self.weapon = Sword(self)
        self.current_state.title = 'Werewolf'
        self.current_state.is_werewolf = True
        self.current_state.is_infected = True
        self.alt_weapon = Claws(self)
