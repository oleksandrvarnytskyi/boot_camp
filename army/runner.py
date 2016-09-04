from units.soldier import Soldier
from units.vampire import Vampire
from units.werewolf import Werewolf
from units.berserker import Berserker
from units.rogue import Rogue
from units.spellcasters.healer import Healer
from units.spellcasters.priest import Priest
from units.spellcasters.wizard import Wizard
from units.spellcasters.warlock import Warlock
from units.spellcasters.necromancer import Necromancer

soldier = Soldier()
vampire = Vampire()
werewolf = Werewolf()
berserker = Berserker()
rogue = Rogue()
healer = Healer()
priest = Priest()
wizard = Wizard()
warlock = Warlock()
necro = Necromancer()
print vampire
print soldier
print werewolf
print berserker
print rogue
print healer
print priest
print wizard
print warlock
print necro
print 25*'-' + 'Battle in progress ' + 25*'-'
vampire.attack(soldier)
print soldier
print vampire
werewolf.change_state()
print werewolf
werewolf.attack(soldier)
print werewolf
print soldier
healer.cast(2, soldier)
print healer
print soldier
priest.cast(3, healer)
print priest
print healer
warlock.cast(5, warlock)
print warlock
warlock.demon().attack(berserker)
print warlock
print berserker
necro.cast(2, soldier)
print soldier
necro.cast(4, berserker)
print necro
print berserker
berserker.attack(necro)
print necro
print 'Observables of ' + necro.current_state.name + 25*'-'
print necro.get_observables()
print 'Observers of ' + berserker.current_state.name + 25*'-'
print berserker.get_observers()
