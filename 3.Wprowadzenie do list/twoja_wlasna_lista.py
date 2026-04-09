commute = ['samochód' , 'rower' , 'samolot' , 'motocykl' , 'statek']

print(f"Chciałbym mieć {commute[1]} marki Specialized.")
print(f"Chciałbym mieć {commute[0]} marki Ferrari.")
print(f"Chciałbym kiedyś wejść na {commute[-1]}.")


commute.append('deskorolka')	#dodawanie elementow do listy 
print(commute)
commute.insert(1, 'narty')		#wstawianie elementu na dane miejsce w liscie
print(commute)

del commute[-1]					#usuniecie elementu z listy - brak dostępu do elementu po usunięciu
print(commute)

popped_commute = commute.pop()	#usuniecie elementu z listy - dostęp do tego elementu pod inną zmienną
print(popped_commute)
print(commute)
popped_commute_1 = commute.pop(-1)
print(popped_commute_1)
print(commute)


too_expensive = 'samolot'
commute.remove(too_expensive)	#usuniecie elementu znajac nazwe a nie znajac indexu
print(f"\n{too_expensive.title()} jest dla mnie za drogi.")
print(f"\t{commute}")


