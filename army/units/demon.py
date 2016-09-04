from soldier import Soldier
from weapon.weapon import Axe


class Demon(Soldier):
    def __init__(self, master, name='Demon'):
        Soldier.__init__(self, name)
        self.weapon = Axe(self)
        self.current_state.is_undead = True
        self.current_state.title = 'Undead'
        self.master = master
        master.set_slave(self)
