def count_words(filename, word):
	"""Liczy ilość wystąpień podanego słowa"""
	try:
		with open(filename, encoding='utf-8') as f:
			lines = f.readlines()
	except FileNotFoundError:
		print(f"Błąd! Nie znaleziono pliku o nazwie '{filename}'.")
	else:
		occurence = 0
		for line in lines:
			occurence += line.lower().count(word)
		print(f"Słowo '{word}' pojawia się w {filename.title().replace('.Txt', '')} {occurence} razy.")

filenames = ['romeo_and_juliet.txt', 'frankenstein.txt', 'book_of_veterinary_medicine.txt', 'krolewna_sniezka.txt']
word = 'the '

for filename in filenames:
	count_words(filename, word)
