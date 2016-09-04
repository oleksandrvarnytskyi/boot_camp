from spellcaster import SpellCaster
from weapon.weapon import Staff
from spells.spell import Heal
from spells.spell import Fireball


class Healer(SpellCaster):
    def __init__(self,  name='Healer', hit_points_limit=80, mana_limit=110):
        SpellCaster.__init__(self, name, hit_points_limit, mana_limit)
        self.weapon = Staff(self)
        self.spellbook[1] = Heal()
        self.spellbook[2] = Fireball()
