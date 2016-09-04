from states.states import InitialState
from interfaces.interfaces import Observable, Observer


class Unit(Observer, Observable):
    def __init__(self, name, hit_points_limit):
        Observer.__init__(self)
        Observable.__init__(self)
        self.name = name
        self.hit_points_limit = hit_points_limit
        self.current_state = InitialState(name, hit_points_limit)
        self.weapon = None
        self.alt_weapon = None

    def attack(self, enemy):
        self.current_state.is_alive()
        self.weapon.action(enemy)

    def take_damage(self, dmg):
        if dmg >= self.current_state.hit_points:
            self.inform()
        self.current_state.take_damage(dmg)

    def take_magic_damage(self, magic_damage):
        if magic_damage >= self.current_state.hit_points:
            self.inform()
        self.current_state.take_magic_damage(magic_damage)

    def add_hit_points(self, hp):
        self.current_state.add_hit_points(hp)

    def add_mana(self, mana_amount):
        pass

    def summon(self):
        pass

    def change_weapon(self, new_weapon):
        temp_weapon = self.weapon
        self.weapon = new_weapon
        self.alt_weapon = temp_weapon

    def change_state(self):
        if self.current_state.is_infected:
            temp_weapon = self.weapon
            if not self.current_state.is_transformed:
                if self.current_state.is_werewolf:
                    self.wolf_state()
                if self.current_state.is_undead:
                    self.vampire_state()
            else:
                self.initial_state()
            self.weapon = self.alt_weapon
            self.alt_weapon = temp_weapon

    def set_current_state(self, state):
        self.current_state = state

    def vampire_state(self):
        self.current_state.vampire_state(self)

    def wolf_state(self):
        self.current_state.wolf_state(self)

    def initial_state(self):
        self.current_state.initial_state(self)

    def inform(self):
        for observer in self.observers:
            if observer.current_state.hit_points > 0:
                observer.add_hit_points(self.current_state.hit_points_limit/10)
            observer.observables.remove(self)

    def send_notification(self):
        if self.observables:
            for observable in self.observables:
                observable.observers.remove(self)
            self.observables = set()

    def __str__(self):
        return '\n{0} -> race: {1}, hp: {2}/{3}, {4}'.format(
            self.current_state.name, self.current_state.title,
            self.current_state.hit_points,
            self.current_state.hit_points_limit, self.weapon)
