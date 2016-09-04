class Spell:
    def __init__(self, spell_name, spell_power, spell_cost):
        self.spell_name = spell_name
        self.spell_power = spell_power
        self.spell_cost = spell_cost
        self.is_battle_spell = False

    def action(self, target):
        pass

    def __str__(self):
        return '"{0}" : power - {1} / cost - {2}'.format(self.spell_name,
                                                         self.spell_power,
                                                         self.spell_cost)


class Fireball(Spell):
    def __init__(self):
        Spell.__init__(self, 'Fireball', 30, 20)
        self.is_battle_spell = True

    def action(self, target):
        target.take_magic_damage(self.spell_power)


class Heal(Spell):
    def __init__(self):
        Spell.__init__(self, 'Heal', 20, 10)

    def action(self, target):
        target.add_hit_points(self.spell_power)


class ManaSource(Spell):
    def __init__(self, owner):
        Spell.__init__(self, 'ManaSource', 15, 5)
        self.owner = owner
        self.is_battle_spell = True

    def action(self, target):
        target.take_magic_damage(self.spell_power)
        self.owner.add_mana(self.spell_power)


class ManaRecovery(Spell):
    def __init__(self):
        Spell.__init__(self, 'ManaRecovery', 15, 10)

    def action(self, target):
        target.add_mana(self.spell_power)


class SummonDemon(Spell):
    def __init__(self):
        Spell.__init__(self, 'SummonDemon', 10, 50)
        self.is_battle_spell = True

    def action(self, target):
        target.summon()


