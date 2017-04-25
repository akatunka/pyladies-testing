# Napis nasledujici funkci: At uzivatel zada cislo, ktere je mezi 50.0 a 150.0 a je to desetine cislo
# Napis test k teto funkci.

def zadej_float():
    while True:
        cislo = input("Zadej desetine cislo mezi 50.0 a 150.0: ")
        try:
            cislo = float(cislo)
            if cislo < 50:
                print('Cislo je mensi nez 50.0')
            elif cislo > 150:
                print('Cislo je vetsi nez 150.0')
            else:
                return cislo
        except ValueError:
            print('Cislo musi byt desetine.')

zadej_float()
