#8.16

def make_car(brand, model, **options):
	"""
	Creates a position in car dictionary. Requires brand and model of the car, and accepts any choosen options given as key-word. Returns dictionary, which makes the dict rewrite itself.
	"""
	car_dict = {
	'brand': brand.title(),
	'model': model.title()
	}
	if brand == 'bmw':
		car_dict['brand'] = brand.upper()
	for option, value in options.items():
		car_dict[option] = value
	return car_dict
