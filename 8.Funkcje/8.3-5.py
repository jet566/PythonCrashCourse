#8.3
print("8.3")

def make_shirt(size, printed_text):
	"""Informacje dot. zamówionej koszulki - rozmiar i nadruk."""
	print(f"Zamówiłeś koszulkę w rozmiarze {size.upper()} oraz tekście '{printed_text}'.")
make_shirt('M', 'Największy bebzol w mieście!')
make_shirt(printed_text='Pomieszczę tu kratę piwa!', size='XL')


#8.4
print("\n8.4")

def make_shirt(size='XL', printed_text='Uwielbiam Pythona'):
	"""Informacje dot. zamówionej koszulki - rozmiar i nadruk."""
	print(f"Zamówiłeś koszulkę w rozmiarze {size.upper()} oraz tekście '{printed_text}'.")
make_shirt('XL')
make_shirt('L')
make_shirt('S', 'Minecraft')


#8.5
print("\n8.5")

def describe_city(city_name, country='Polsce'):
	"""Wyświetla proste zdanie o mieście i kraju."""
	print(f"{city_name.title()} leży w {country.title()}.")
describe_city('Warszawa')
describe_city('Ontario', 'Kanadzie')
describe_city(country='USA', city_name='Nowy York')

