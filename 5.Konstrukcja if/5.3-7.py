#5.3
print("5.3")

alien_color = 'zielony'
if (alien_color == 'zielony'):
	print(f"Ustrzeliłeś obcego w kolorze {alien_color}m! +5pkt")
else:
	print(f"Ustrzeliłeś obcego w kolorze {alien_color}m! +0pkt")

#5.4
print("\n5.4")

alien_color = 'czerwony'
if (alien_color == 'zielony'):
	print(f"Ustrzeliłeś obcego w kolorze {alien_color}m! +5pkt")
if (alien_color == 'żółty'):
	print(f"Ustrzeliłeś obcego w kolorze {alien_color}m! +10pkt")
if (alien_color == 'czerwony'):
	print(f"Ustrzeliłeś obcego w kolorze {alien_color}m! +10pkt")

#5.5
print("\n5.5")

alien_color = 'żółty'
if (alien_color == 'zielony'):
	print(f"Ustrzeliłeś obcego w kolorze {alien_color}m! +5pkt")
elif (alien_color == 'czerwony'):
	print(f"Ustrzeliłeś obcego w kolorze {alien_color}m! +10pkt")
else:
	print(f"Ustrzeliłeś obcego w kolorze {alien_color}m! +15pkt")

#5.6
print("\n5.6")

age = 70
if age < 2:
	print("Jesteś niemowlęciem")
elif age > 2 and age < 4:
	print("Jesteś dzieckiem, które uczy się chodzić")
elif age > 4 and age < 13:
	print("Jesteś dzieckiem")
elif age > 13 and age < 20:
	print("Jesteś nastolatkiem")
elif age > 20 and age < 65:
	print("Jesteś dorosły")
else:
	print("Jesteś seniorem")

#5.7
print("\n5.7")

favourite_fruits = ['banany' , 'maliny' , 'borówki' , 'jabłka' , 'truskawki']

if 'banany' in favourite_fruits:
	print("Naprawdę lubisz banany!")
if 'maliny' in favourite_fruits:
	print("Naprawdę lubisz maliny!")
if 'ananasy' in favourite_fruits:
	print("Naprawdę lubisz ananasy!")
if 'mango' in favourite_fruits:
	print("Naprawdę lubisz mango!")
if 'truskawki' in favourite_fruits:
	print("Naprawdę lubisz truskawki!")

