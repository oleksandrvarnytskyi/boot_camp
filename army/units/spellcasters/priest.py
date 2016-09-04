from spellcaster import SpellCaster
from exclusions.exclusions import NoSuchSpell
from weapon.weapon import Prayer
from spells.spell import Heal
from spells.spell import Fireball
from spells.spell import ManaRecovery


class Priest(SpellCaster):
    def __init__(self,  name='Priest', hit_points_limit=80, mana_limit=110):
        SpellCaster.__init__(self, name, hit_points_limit, mana_limit)
        self.weapon = Prayer(self)
        self.spellbook[1] = Heal()
        self.spellbook[2] = Fireball()
        self.spellbook[3] = ManaRecovery()

    def cast(self, spell_id, target):
        if not self.current_state.is_transformed:
            self.current_state.is_alive()
            if spell_id in self.spellbook:
                self.set_mana(self.spellbook[spell_id].spell_cost)
                if (target.current_state.is_undead and
                    self.spellbook[spell_id].is_battle_spell) or not \
                        self.spellbook[spell_id].is_battle_spell:
                    self.spellbook[spell_id].action(target)
                else:
                    temp = self.spellbook[spell_id].spell_power
                    self.spellbook[spell_id].spell_power /= 2
                    self.spellbook[spell_id].action(target)
                    self.spellbook[spell_id].spell_power = temp
            else:
                raise NoSuchSpell()
