#8.16
print("8.16")

import module
print(module.make_car('Subaru', 'Impreza', type='rally car'))

from module import make_car
print(make_car('Mazda', '3', type='hatchback'))

from module import make_car as mc
print(mc('Mitsubishi', 'Lancer', addons='EVO package'))

import module as m
print(m.make_car('Hyundai', 'i30', color='black'))

from module import *
print(make_car('Volvo', 'V40', type='wagon'))