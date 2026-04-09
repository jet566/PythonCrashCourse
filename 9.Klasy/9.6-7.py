#9.6
print("9.6")

from IceCreamStand import IceCreamStand as ics

louda = ics('Lody Louda')
louda.flavors = ['Pistacja', 'Malina', 'Orzech']

louda.describe_restaurant()
louda.show_flavors()

#9.7
print("\n9.7")

from Admin import Admin 

malgosia = Admin('Malgosia', 'Husaria', '25', '06.04.1998')
malgosia.privileges = ['może dodać post', 'może zbanować użytkownika', 'może usunąć post']

malgosia.describe_user()
malgosia.show_privileges()
