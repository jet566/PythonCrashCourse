goscie = ['dziadek' , 'dziewczyna' , 'mama' , 'przyjaciel']

print(f"Zapraszam na swiezutkie schabowe {goscie[0].title()}!")
print(f"Zapraszam na swiezutkie schabowe {goscie[1].title()}!")
print(f"Zapraszam na swiezutkie schabowe {goscie[-1].title()}!")
print(f"{goscie[-2].title()} niestety nie może pojawić się na obiedzie :(.")

del goscie[-2]									#goscie.remove('mama')


goscie.insert(2, 'tato')


print(f"\nZapraszam na swiezutkie schabowe {goscie[0].title()}!")
print(f"Zapraszam na swiezutkie schabowe {goscie[1].title()}!")
print(f"Zapraszam na swiezutkie schabowe {goscie[2].title()}!")
print(f"Zapraszam na swiezutkie schabowe {goscie[3].title()}!")
