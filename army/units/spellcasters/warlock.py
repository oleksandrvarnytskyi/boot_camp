from spellcaster import SpellCaster
from units.demon import Demon
from exclusions.exclusions import SummonException
from weapon.weapon import Staff
from spells.spell import Heal
from spells.spell import Fireball
from spells.spell import ManaRecovery
from spells.spell import ManaSource
from spells.spell import SummonDemon


class Warlock(SpellCaster):
    def __init__(self,  name='Warlock', hit_points_limit=90, mana_limit=150):
        SpellCaster.__init__(self, name, hit_points_limit, mana_limit)
        self.weapon = Staff(self)
        self.is_battle_mage = True
        self.spellbook[1] = Heal()
        self.spellbook[2] = Fireball()
        self.spellbook[3] = ManaRecovery()
        self.spellbook[4] = ManaSource(self)
        self.spellbook[5] = SummonDemon()
        self.slave = None

    def set_slave(self, demon):
        self.slave = demon

    def free_slave(self):
        if not self.current_state.is_transformed:
            self.slave = None

    def summon(self):
        if not self.current_state.is_transformed:
            if self.slave:
                self.free_slave()

            self.slave = Demon(self)

    def demon(self):
        if not self.current_state.is_transformed:
            if not self.slave:
                raise SummonException()

            return self.slave
        else:
            raise SummonException()

    def __str__(self):
        return '{0}\nhas a slave: {1}'.format(SpellCaster.__str__(self),
                                            self.slave)
