#4.7
liczby = list(range(3,31,3))

for liczba in liczby:
	print(liczba)

#4.7-2
squares=[]

for value in range(3,31):		#przypisz wartość od 3 do 30 dla value 
	square = value**2			#dodaj wartość przypisana do zmiennej i podnies do kwadratu
	squares.append(square)		#dodaj kwadrat do listy i rozpocznij od nowa 
print(squares)

#4.8
cubes = []
for value in range(1,11):		#przypisz wartość od 1 dla value 
	cube = value**3				#dodaj wartość przypisana do zmiennej i podnies do szescianu
	cubes.append(cube)			#dodaj szescian do listy i rozpocznij od nowa, przypisujac 2
print(cubes)

#4.9
squares = [value**3 for value in range(1,11)]	#lista skladana, 
print(squares)





