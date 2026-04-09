#7.8
print("7.8")
sandwich_orders = ['muffuletta', 'kanapka nicejska', 'grzanki z batatów', 'kanapki z pastą jajeczną']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"Przygotowano {current_sandwich}!")
	finished_sandwiches.append(current_sandwich)
print("-----Przygotowano już wszystkie kanapki-----")
for sandwich in finished_sandwiches:
	print(sandwich)


#7.9
print("\n7.9")

sandwich_orders = ['muffuletta', 'kanapka nicejska', 'kanapka z pastrami', 'grzanki z batatów', 'kanapka z pastrami', 'kanapki z pastą jajeczną', 'kanapka z pastrami']
print("Aktywne zamówienia:")
for sandwich in sandwich_orders: 
	print(sandwich)

print("\n\tUwaga niestety skończyło się pastrami!")

while 'kanapka z pastrami' in sandwich_orders:
	sandwich_orders.remove('kanapka z pastrami')

print("\nAktywne zamówienia:")
for sandwich in sandwich_orders:
	print(sandwich)