message = "Witaj, świecie Pythona!"

print(message)

message = 'Witaj, świecie ksiązki "Python. Instrukcje dla programisty"!' 
print(message)

name = "jan kowalski"

print(name.title())

name = "Jan Kowalski"

print(name.upper())
print(name.lower())

first_name = "jan"
last_name = "kowalski"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Witaj, {full_name.title()}!")

message = f"Witaj, {full_name.title()}!"
print(message)

print("Python")
print ("\tPython")

print("Języki:\nPython\nC\nJavaScript")

print("Języki:\nPython\n\tC\nJavaScript")

favourite_language = '  python   '
print(favourite_language)
favourite_language = favourite_language.strip()
print(favourite_language)
