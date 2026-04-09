cats = ['puszek' , 'okruszek']

for cat in cats: 		#pobranie imienia z listy i umieszczenie go w zmiennej cat
	print(cat)

range(1,5)					#generowanie serii liczb od 1 do 4
range(6)					#generowanie serii liczb od 0 do 5

for value in range(1,10):
	print(value)


list()						#konwersja na listę

numbers = list(range(4))
print(numbers)

even_numbers = list(range(2,13,2))		#generowanie liczb 2-12 co 2
print(even_numbers)

digits = [1,2,4,5,11,6,-10]

min(digits)						#wskazanie najmiejszej liczby z listy
max(digits)						#wskazanie najwiekszej liczby z listy
sum(digits)						#okreslenie sumy liczb z listy


squares = [value**2 for value in range(1,11)]	#tworzenie skladanej listy kwadratow


