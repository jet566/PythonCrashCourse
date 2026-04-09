filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

print("\n")

with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.rstrip())

print(lines)
print("\n")

with open(filename) as file_object:
	lines = file_object.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.rstrip()
	print(pi_string)
	print(f"Dokładność do {len(pi_string)-2} miejsc po przecinku.")

print("\n")

filename = 'pi_milion_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.rstrip()
	print(f"{pi_string[:100]}...")
	print(f"Dokładność do 98 miejsc po przecinku. Plik oferuje dokładność do {len(pi_string)-2} miejsc po przecinku.")


with open(filename) as file_object:
	lines = file_object.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.rstrip()

birthday = input("Podaj swoją datę urodzenia w formacie (ddmmrr): ")

if birthday in pi_string:
	print("Twoja data urodzenia znajduje się wśród miliona pierwszych cyfr liczby pi!")
else:
	print("Twoja data urodzenia nie znajduje się wśród miliona pierwszych cyfr liczby pi. :(")