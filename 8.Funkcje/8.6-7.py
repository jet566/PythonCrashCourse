#8.6
print("8.6")

def city_country(city_name, country_name):
	"""Zwraca miasto oraz państwo"""
	formated_text = f"{city_name}, {country_name}"
	return formated_text.title()

text = city_country('santiago', 'chile')
print(text)
text = city_country('mallorca', 'spain')
print(text)
text = city_country('rhodos', 'greece')
print(text)


#8.7
print("\n8.7")

def make_album(title, band_name = '', artist_name = '', songs_number = None):
	"""Zwraca słownik zawierający zespół lub artyste, oraz tytuł albumu"""
	formated_text = {'title': title}
	if band_name:
		formated_text['band_name'] = band_name
		if songs_number:
			formated_text['songs_number'] = songs_number
	elif artist_name:
		formated_text['artist_name'] = artist_name
		if songs_number:
			formated_text['songs_number'] = songs_number
	return formated_text

text = make_album('Finally Rich', artist_name= 'Chief Keef')
print(text)
text = make_album('Grajcowanie', band_name= 'Zakopower')
print(text)
text = make_album('Super Slimey', artist_name= 'Future')
print(text)
text = make_album('Wu-Tang Forever', band_name= 'Wu-Tang Clan', songs_number=20)
print(text)





