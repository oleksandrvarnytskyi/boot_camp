class Weapon:
    def __init__(self, owner, name, damage):
        self.owner = owner
        self.name = name
        self.damage = damage

    def action(self, target):
        pass

    def __str__(self):
        return 'weapon: {0} - dmg({1})'.format(self.name, self.damage)


class Sword(Weapon):
    def __init__(self, owner):
        Weapon.__init__(self, owner, 'Sword', 20)

    def action(self, target):
        target.take_damage(self.damage)
        self.owner.take_damage(target.weapon.damage/2)


class Fangs(Weapon):
    def __init__(self, owner):
        Weapon.__init__(self, owner, 'Fangs', 30)

    def action(self, target):
        target.take_damage(self.damage)
        self.owner.take_damage(target.weapon.damage/2)
        self.owner.add_hit_points(self.damage/3)
        if not target.current_state.is_werewolf and not \
                target.current_state.is_infected:
            target.vampire_state()
            target.change_weapon(Fangs(target))


class Claws(Weapon):
    def __init__(self, owner):
        Weapon.__init__(self, owner, 'Claws', 30)

    def action(self, target):
        target.take_damage(self.damage)
        self.owner.take_damage(target.weapon.damage/2)
        if not target.current_state.is_undead and not \
                target.current_state.is_werewolf:
            target.wolf_state()
            target.change_weapon(Claws(target))


class Dagger(Weapon):
    def __init__(self, owner):
        Weapon.__init__(self, owner, 'Dagger', 20)

    def action(self, target):
        target.take_damage(self.damage)


class Axe(Weapon):
    def __init__(self, owner):
        Weapon.__init__(self, owner, 'Axe', 25)
        self.chance_of_double_damage = 1

    def action(self, target):
        if self.chance_of_double_damage % 2 == 0:
            print 'Axe inflicts double damage- ' + str(self.damage*2) + '!!!\n'
            target.take_damage(self.damage*2)
        else:
            target.take_damage(self.damage)

        self.owner.take_damage(target.weapon.damage/2)
        self.chance_of_double_damage += 1


class Staff(Weapon):
    def __init__(self, owner):
        Weapon.__init__(self, owner, 'Staff', 10)
        self.chance_of_double_damage = 1

    def action(self, target):
        dmg = self.damage
        if target.current_state.is_undead and not \
                self.owner.current_state.is_undead:
            dmg *= 2

        target.take_damage(dmg)
        self.owner.take_damage(target.weapon.damage/2)


class Prayer(Weapon):
    def __init__(self, owner):
        Weapon.__init__(self, owner, 'Prayer', 10)

    def action(self, target):
        dmg = self.damage
        if target.is_undead:
            dmg *= 2

        target.take_damage(dmg)
        self.owner.take_damage(target.weapon.damage/2)
