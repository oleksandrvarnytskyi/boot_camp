class UnitIsDead(Exception):
    pass


class Unit:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hit_points = hp
        self.hit_points_limit = hp
        self.dmg = dmg

    def ensure_is_alive(self):
        if self.hit_points == 0:
            raise UnitIsDead()

    def add_hit_points(self, hp):
        self.ensure_is_alive()
        self.hit_points += hp
        if self.hit_points > self.hit_points_limit:
            self.hit_points = self.hit_points_limit

    def take_damage(self, dmg):
        self.ensure_is_alive()
        self.hit_points -= dmg
        if self.hit_points <= 0:
            raise UnitIsDead()

    def attack(self, enemy):
        enemy.take_damage(self.dmg)
        self.counter_attack(enemy)

    def counter_attack(self, enemy):
        self.ensure_is_alive()
        self.hit_points -= enemy.dmg/2
        if self.hit_points <= 0:
            raise UnitIsDead()

    def __str__(self):
        return 'Unit name: {0}\nhit_points_limit/hit_points: {1}/{2}' \
               '\ndamage: {3}\n'.format(self.name, self.hit_points_limit,
                                        self.hit_points, self.dmg)


barbarian = Unit("Barbarian", 200, 20)
knight = Unit("Knight", 180, 30)

print barbarian
print knight

barbarian.attack(knight)
print knight
print barbarian

knight.attack(barbarian)
print knight
print barbarian
