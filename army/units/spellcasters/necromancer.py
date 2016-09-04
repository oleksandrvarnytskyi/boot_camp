from spellcaster import SpellCaster
from weapon.weapon import Staff
from spells.spell import Heal
from spells.spell import Fireball
from spells.spell import ManaRecovery
from spells.spell import ManaSource


class Necromancer(SpellCaster):
    def __init__(self,  name='Necromancer', hit_points_limit=100,
                 mana_limit=120):
        SpellCaster.__init__(self, name, hit_points_limit, mana_limit)
        self.weapon = Staff(self)
        self.current_state.is_undead = True
        self.current_state.title = 'Undead'
        self.is_battle_mage = True
        self.spellbook[1] = Heal()
        self.spellbook[2] = Fireball()
        self.spellbook[3] = ManaRecovery()
        self.spellbook[4] = ManaSource(self)

    def take_damage(self, dmg):
        if dmg >= self.current_state.hit_points:
            self.inform()
            self.send_notification()

        self.current_state.take_damage(dmg)

    def cast(self, spell_id, target):
        SpellCaster.cast(self, spell_id, target)
        if target.current_state.hit_points and \
           self.spellbook[spell_id].is_battle_spell:
            self.add_observable(target)

    def attack(self, enemy):
        SpellCaster.attack(self, enemy)
        if enemy.current_state.hit_points:
            self.add_observable(enemy)
