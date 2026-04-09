def display_names(filename):
	"""Wyświetla imiona zwierząt na ekranie"""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.readlines()
	except FileNotFoundError:
		pass
	else:
		print(f"Imiona pliku '{filename}': ")
		for name in contents:
			print(f"\t{name.title().strip()}")

filenames = ['dogs.txt', 'cats.txt']

for filename in filenames:
	display_names(filename)
