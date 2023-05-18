# Penkta užduotis
#
# Sukurti programą, kuri nuskaitys iš .txt failo skaičius
# (failą kokį norite susikurkite bei užpildykite kokiais norite skaičiais), suskaičiuos visų skaičių vidurkį
# (naudojant reduce() funkciją) bei išsaugos rezultatą į kitą .txt  failą (šį failą taip pat susikurkite kokį norite).
# Taip pat, tą patį vidurkį išspausdinkit ir į terminalą.

with open("skaiciu_failas.txt", 'r+') as failas:
    failas.write("100\n50\n28\n85.7\n0.111")
    print(failas.read())

# Sprendimas be reduce()
# suma = []
#
# with open("skaiciu_failas.txt", 'r+') as failas:
#     for eilute in failas:
#         skaicius = float(eilute)
#         suma.append(skaicius)
#     vidurkis = sum(suma)/len(suma)
#     print(vidurkis)

# Sprendimas su reduce
from functools import reduce

sarasas = []
with open("skaiciu_failas.txt", 'r+') as failas:
    for eilute in failas:
        sarasas.append(float(eilute))
    naujas = round(reduce(lambda x, y: (x + y), sarasas)/float(len(sarasas)), 2)
    print(naujas)

with open("naujas_skaiciu_failas.txt", 'w') as failas:
    failas.write(str(naujas))





