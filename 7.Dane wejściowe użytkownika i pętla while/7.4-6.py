#7.4
print("7.4")

prompt = "\nPodaj dodatki, które chciałbyś mieć na pizzy:"
prompt += "\n(Kiedy skończysz wymieniać dodatki - napisz 'koniec') "

while True:
	message = input(prompt)
	if message == 'koniec':
		break
	else:
		print(f"Do twojej pizzy dodano {message.title()}!")


#7.5
print("\n7.5")

prompt = "\nPodaj swój wiek: "

while True:
	age = input(prompt)
	age = int(age)
	if age < 3:
		print("Twój bilet jest bezpłatny!")
		break
	elif age >= 3 and age < 12:
		print("Twoja wejściówka kosztuje 10 zł!")
		break
	else:
		print("Twoja wejściówka kosztuje 15zł!")
		break

#7.6
print("\n7.6")

prompt = "\nPodaj dodatki, które chciałbyś mieć na pizzy:"
prompt += "\n(Kiedy skończysz wymieniać dodatki - napisz 'koniec') "

message = ""
while message != 'koniec':
	message = input(prompt)
	if message != 'koniec':
		print(f"Do twojej pizzy dodano {message.title()}!")


prompt = "\nPodaj swój wiek: "

active = True
while active:
	age = input(prompt)
	age = int(age)
	if age < 3:
		print("Twój bilet jest bezpłatny!")
		active = False
	elif age >= 3 and age < 12:
		print("Twoja wejściówka kosztuje 10 zł!")
		active = False
	else:
		print("Twoja wejściówka kosztuje 15zł!")
		active = False




