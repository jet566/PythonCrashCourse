#9.10
print("9.10")

import restaurant 

pizzeria = restaurant.Restaurant('Alfredo', 'Włoskiej')
pizzeria.describe_restaurant()


#9.11
print("\n9.11")

import user_privileges_admin as upa

bartosz = upa.Admin('Bartosz', 'Ciołek', '27', '10.10.1996')
bartosz.describe_user()

bartosz.privileges.privileges = ['może zbanować użytkownika', 'może usunąć konto']

bartosz.privileges.show_privileges()


