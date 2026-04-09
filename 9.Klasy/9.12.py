#9.12
print("9.12")

import privileges_admin as pa

mateusz = pa.Admin('Mati', 'Spec', '17', '05.03.2006')
mateusz.describe_user()

mateusz.privileges.privileges = ['może wstawić post', 'może napisać komentarz']
mateusz.privileges.show_privileges()