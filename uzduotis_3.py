# Trečia užduotis

# Sukurti funkciją, kuri sukuria darbuotoją (vardas, amžius, darbo pozicija) ir jį grąžina.

import pickle

# Funkcija:
darbuotoju_sarasas = []
def darbuotojo_funkcija() :
    while True :
        d = input("Jei norite įrašyti darbuotoją, spauskit '+'. Jei nenorite: '-'")
        if d == "+" :
            darbuotojas = {
                'vardas' : input("Įrašykite savo vardą: "),
                'amzius' : input("Įrašykite savo amžių: "),
                'darbo_pozcija' : input('Įrašykite savo darbo poziciją: ')
            }
            darbuotoju_sarasas.append(darbuotojas)
        elif d == "-" :
            break
        else :
            break
    return(darbuotoju_sarasas)

# Sukurti funkciją, kuri išsaugo darbuotojus į failą (pickle)

def darbuotoju_irasymas() :
    with open("darbuotojai.pkl", "wb") as pickle_darbuotojai:
        pickle.dump(darbuotoju_sarasas, pickle_darbuotojai)

# Sukurti funkciją, kuri užkrauna darbuotojus iš failo ir juos grąžina (pickle)

def darbuotojo_grazinimas():
    with open("darbuotojai.pkl", "rb") as pickle_darbuotojai:
        uzkrauti_darbuotojai = pickle.load(pickle_darbuotojai)
    return uzkrauti_darbuotojai

# Sukurti programą, kuri saugotų duomenis apie darbuotojus Pickle faile bei atliktų su duomenimis įvairius veiksmus:

# Programa

darbuotojo_funkcija()
darbuotoju_irasymas()
darbuotojai_dokumente = darbuotojo_grazinimas()
print(darbuotojai_dokumente)

# Panaudoti sukūrimo funkciją kelis kartus su kokiomis norite reikšmėmis. Panaudoti išsaugojimą į failą funkciją
# Panaudoti užkrovimo iš failo funkciją. Atspausdinkite užkrautus iš failo duomenis

# Šie punktai jau įvykdyti
