#8.12
print("8.12")

def make_sandwich(*ingredients):
	print(f"\nPrzygotowujemy dla ciebie kanapkę z:")
	for ingredient in ingredients:
		print(f"\t- {ingredient}")
make_sandwich('ser', 'pieczarki')
make_sandwich('chorizo')
make_sandwich('szynka', 'pomidor', 'ogórek')

#8.13
print("\n8.13")

def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile(
	'Mariusz', 'Kowalski', location='Sosnowiec', 
	field='wypieki na zakwasie', hobby='zjadanie hotdogow na czas')
print(user_profile)

#8.14
print("\n8.14")

def make_car(brand, model, **options):
	car_dict = {
	'brand': brand.title(),
	'model': model.title()
	}
	if brand == 'bmw':
		car_dict['brand'] = brand.upper()
	for option, value in options.items():
		car_dict[option] = value
	return car_dict

my_bmw = make_car('bmw', 'e92', type='coupe', power='170 km')
print(my_bmw)

my_subaru = make_car('subaru', 'forester', type='SUV', tow_package=True, fuel='diesel')
print(my_subaru)