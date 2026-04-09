#5.1
car = 'bmw'

print("Czy car == 'bmw'? Przewiduję wartość True.")
print(car == 'bmw')

print("\nCzy car == 'toyota'? Przewiduję wartość False.")
print(car == 'toyota')

car = 'honda'

print("\nCzy car == 'opel'? Przewiduję wartość False.")
print(car == 'opel')

print("\nCzy car == 'honda'? Przewiduję wartość True.")
print(car == 'honda')

car = 'Ferrari'

print("\nCzy car == 'ferrari'? Przewiduję wartość True.")
print(car.lower() == 'ferrari')

print("\nCzy car == 'audi'? Przewiduję wartość False.")
print(car == 'audi')


#5.2
cars = ['honda' , 'bmw' , 'audi' , 'Mercedes' , 'fiat' , 22]

print("\nCzy pierwszy samochód to honda?")
print(cars[0] == 'honda')	

print(f"\nCzy 6 pozycja jest mniejsza lub rowna 21?: {cars[5] <= 21}")		

print("\nCzy 4 samochód to mercedes?:")
print(cars[3].lower() == 'mercedes')

age_0 = 22
age_1 = 17

print("\nCzy obie osoby są pełnoletnie?")
if age_0 >= 18 and age_1 >= 18:
	print("Tak, obie osoby są pełnoletnie.")
else:
	print("Nie, któraś z tych osób jest niepełnoletnia.")

print("\nCzy któraś z tych osób jest pełnoletnia?")
if age_0 >=18 or age_1 >=18:
	print("Tak, któraś z tych osób jest pełnoletnia.")
else:
	print("Nie, żadna z nich nie jest pełnoletnia.")

requested_toppings = ['pieczarki' , 'ser' , 'cebula']

print(f"\nCzy pieczarki zostały zamówione?: {'pieczarki' in requested_toppings}")
print(f"\nCzy kukurydza została zamówiona?: {'kukurydza' in requested_toppings}")

topping = 'bekon'

print("\nCzy mój dodatek został domówiony?")
if topping not in requested_toppings:
	print(f"Twoj dodatek {topping} nie został domówiony.")
else:
	print(f"Tak {topping} został domówiony.")

answer = 17

if answer != 42:
	print(f"\n{answer} nie jest prawidłową odpowiedzią!")
else:
	print("\n42 to poprawna odpowiedź :D")
