dishes = ('chleb' , 'bułka' , 'ser smażony' , 'zapiekanka' , 'burger')

for dish in dishes:
	print(dish)

dishes[2] = 250 #nie mozna przypisywac do krotki(tuple) - jest niemodyfikowalna

dishes = ('woda' , 'bagietka' , 'ser smażony' , 'zapiekanka' , 'burger')

for dish in dishes:
	print(dish)