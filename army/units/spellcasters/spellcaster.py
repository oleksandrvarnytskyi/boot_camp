from units.unit import Unit
from exclusions.exclusions import OutOfMana
from exclusions.exclusions import NoSuchSpell


class SpellCaster(Unit):
    def __init__(self, name='SpellCaster', hit_points_limit=80,
                 mana_limit=100):
        Unit.__init__(self, name, hit_points_limit)
        self.mana = mana_limit
        self.mana_limit = mana_limit
        self.is_battle_mage = False
        self.spellbook = {}

    def is_mana(self):
        if not self.mana:
            raise OutOfMana()

    def set_mana(self, spell_cost):
        self.is_mana()
        if spell_cost > self.mana:
            raise OutOfMana()

        self.mana -= spell_cost

    def cast(self, spell_id, target):
        if not self.current_state.is_transformed:
            self.current_state.is_alive()
            if spell_id in self.spellbook:
                self.set_mana(self.spellbook[spell_id].spell_cost)
                if (self.is_battle_mage and
                    self.spellbook[spell_id].is_battle_spell) or (
                            not self.is_battle_mage and
                            not self.spellbook[spell_id].is_battle_spell):
                    self.spellbook[spell_id].action(target)
                else:
                    temp = self.spellbook[spell_id].spell_power
                    self.spellbook[spell_id].spell_power /= 2
                    self.spellbook[spell_id].action(target)
                    self.spellbook[spell_id].spell_power = temp
            else:
                raise NoSuchSpell()

    def add_mana(self, mana_amount):
        total = mana_amount + self.mana
        if total > self.mana_limit:
            self.mana = self.mana_limit
            return

        self.mana += mana_amount

    def show_spellbook(self):
        return '\n'.join(str(key) + ': ' + str(self.spellbook[key])
                         for key in self.spellbook)

    def __str__(self):
        return '{0}\nMana[{1}/{2}] {3} > has in Spellbook:\n{4}'.format(
            Unit.__str__(self), self.mana, self.mana_limit,
            (' battle mage' if self.is_battle_mage else ' healer'),
            self.show_spellbook())
