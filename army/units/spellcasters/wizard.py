from spellcaster import SpellCaster
from weapon.weapon import Staff
from spells.spell import Heal
from spells.spell import Fireball
from spells.spell import ManaRecovery
from spells.spell import ManaSource


class Wizard(SpellCaster):
    def __init__(self,  name='Wizard', hit_points_limit=90, mana_limit=130):
        SpellCaster.__init__(self, name, hit_points_limit, mana_limit)
        self.weapon = Staff(self)
        self.is_battle_mage = True
        self.spellbook[1] = Heal()
        self.spellbook[2] = Fireball()
        self.spellbook[3] = ManaRecovery()
        self.spellbook[4] = ManaSource(self)
