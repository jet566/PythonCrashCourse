gory = ['Śnieżka' , 'Giewont' , 'K2' , 'Killimanjaro']
rzeki = ['Warta' , 'Wisła' , 'Amazonka' , 'Nysa']				#tworzy liste

gory.append('Mount Everest')		#dodawanie elementow do listy

rzeki.insert(1, 'Kwisa')			#wstawianie elementu na dane miejsce w liscie			

del gory[-1]			#usuniecie elementu z listy - brak dostępu do elementu po usunięciu

popped_rzeki = rzeki.pop()	#usuniecie elementu z listy - dostęp do tego elementu pod inną zmienną

gory.remove('K2')		#usuniecie elementu znajac nazwe a nie znajac indexu

len(rzeki)				#wielkosc listy

gory.sort()					#trwała zmiana kolejności elementów listy sortowanie a-z
gory.sort(reverse=True)		#trwała zmiana kolejności elementów listy sortowanie z-a

sorted(rzeki)				#tymczasowa zmiana kolejności elementów listy sortowanie a-z
sorted(rzeki, reverse=True)	#tymczasowa zmiana kolejności elementów listy sortowanie z-a

gory.reverse() 				#twała zmiana odwracanie kolejności listy - aczkolwiek możliwość 							  zmiany przez ponowne zastosowanie reverse()