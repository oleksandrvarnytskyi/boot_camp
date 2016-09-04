from exclusions.exclusions import OutOfHitPoints


class States:
    def __init__(self, name, hit_points_limit, title):
        self.name = name
        self.hit_points = hit_points_limit
        self.hit_points_limit = hit_points_limit
        self.title = title
        self.is_undead = False
        self.is_werewolf = False
        self.is_transformed = False
        self.is_infected = False

    def is_alive(self):
        if not self.hit_points:
            raise OutOfHitPoints()

    def take_damage(self, damage):
        self.is_alive()

        if damage > self.hit_points:
            self.hit_points = 0
            return

        self.hit_points -= int(damage)

    def take_magic_damage(self, magic_damage):
        self.take_damage(magic_damage)

    def add_hit_points(self, hp):
        self.is_alive()
        total_hit_points = self.hit_points + hp

        if total_hit_points > self.hit_points_limit:
            self.hit_points = self.hit_points_limit
            return

        self.hit_points = total_hit_points

    def vampire_state(self, unit):
        pass

    def wolf_state(self, unit):
        pass

    def initial_state(self, unit):
        pass


class InitialState(States):
    def __init__(self, name, hit_points_limit, title='Human'):
        States.__init__(self, name, hit_points_limit, title)
        self.is_undead = False
        self.is_werewolf = False
        self.is_transformed = False
        self.is_infected = False

    def vampire_state(self, unit):
        if not self.is_werewolf:
            unit.set_current_state(VampireState('Vampire-'+self.name,
                                                self.hit_points_limit*1.5,
                                                'Undead'))
            unit.take_damage(int((self.hit_points_limit-self.hit_points)*1.5))

    def wolf_state(self, unit):
        if not self.is_undead:
            unit.set_current_state(WolfState('Wolf-'+self.name,
                                             self.hit_points_limit*2,
                                             'Werewolf'))
            unit.take_damage((self.hit_points_limit - self.hit_points)*2)


class VampireState(States):
    def __init__(self, name, hit_points_limit, title="Undead"):
        States.__init__(self, name, hit_points_limit, title)
        self.is_undead = True
        self.is_werewolf = False
        self.is_transformed = True
        self.is_infected = True

    def initial_state(self, unit):
        unit.set_current_state(InitialState(unit.name,
                                            self.hit_points_limit/1.5,
                                            'Undead'))
        unit.take_damage(int((self.hit_points_limit-self.hit_points)/1.5))
        unit.current_state.is_infected = True
        unit.current_state.is_undead = True


class WolfState(States):
    def __init__(self, name, hit_points_limit, title='Werewolf'):
        States.__init__(self, name, hit_points_limit, title)
        self.is_undead = False
        self.is_werewolf = True
        self.is_transformed = True
        self.is_infected = True

    def initial_state(self, unit):
        unit.set_current_state(InitialState(unit.name, self.hit_points_limit/2,
                                            'Werewolf'))
        unit.take_damage((self.hit_points_limit - self.hit_points)/2)
        unit.current_state.is_infected = True
        unit.current_state.is_werewolf = True

    def take_magic_damage(self, magic_damage):
        self.take_damage(magic_damage*1.5)
