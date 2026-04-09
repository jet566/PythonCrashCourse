def get_formatted_place(city, country, population = ''):
	"""Generuje elegancko sformatowaną nazwę miasta i państwa"""
	return f"{city.title()}, {country.title()} - population {population}"

print(get_formatted_place('bob', 'bobolandia', 10_000))