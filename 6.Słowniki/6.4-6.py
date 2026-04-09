#6.4
print("6.4")

glosariusz = {
	'Iteracja': 'Powtarzanie tej samej operacji aż do spełnienia warunku',
	'Test warunkowy': 'Sprawdzenie czy spełniono dany warunek',
	'Lista': 'Lista nieuporządkowanych informacji',
	'Krotka': 'Lista bez możliwości modyfikacji',
	'Pętla': 'Powtarzanie',
	'In': 'Zawiera',
	'Sorted()': 'Wyświetla posortowane dane',
	'Values()': 'Wyświetla wartości',
	'Keys()': 'Wyświetla klucze',
	'del': 'Usuwa pare klucz-wartość',
}

for key, value in glosariusz.items():
	print(f"{key}:\t{value}")

#6.5
print("\n6.5")

rivers = {
	'Nil': 'Egipt',
	'Wisła': 'Polska',
	'Wołga': 'Rosja',
}

for river, country in rivers.items():
	print(f"{river} przepływa przez {country}.")

for river in rivers.keys():
	print(river)

for country in rivers.values():
	print(country)

#6.6
print("\n6.6")

favourite_language = {
	'vanessa': 'c',
	'igor': 'phyton',
	'oliwier': 'html',
	'natalia': 'ruby',
	'kamil': 'kotlins',
}

respondents = ['vanessa' , 'kamil' , 'mariusz' , 'wacek' , 'bob']

for respondent in respondents:
	if respondent in favourite_language.keys():
		print(f"Dziękujemy za wzięcie udziału w naszej ankiecie {respondent}.")
	else:
		print(f"Witaj {respondent}, nalegamy abyś wziął udział w naszej ankiecie. ")