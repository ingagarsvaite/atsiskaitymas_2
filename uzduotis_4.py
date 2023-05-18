# Ketvirta užduotis
#
# Sukurti funkciją, kuri priimtų sąrašą tuple elementų, kiekvienas tuple sudarytas iš 2 elementų - stringo ir sąrašo
# int skaičių. Funkcija turi grąžinti sąrašą tuple elementų, kurie sudaryti iš 2 reikšmių: stringo ir skaičių vidurkio:
# Pvz: į funkciją paduodamas sąrašas: [("apple", [1, 2, 3]), ("banana", [4, 5, 6]), ("orange", [7, 8, 9])],
# turi būti grąžinamas: [("apple", 2.0), ("banana", 5.0), ("orange", 8.0)]
# Panaudoti sukurtą funkciją su kokiomis norite reikšmėmis ir atspausdinti funkcijos rezultatus

# Funkcija
def priemimo_funkcija(kazkoks_sarasas) :
    naujas_sarasas = []
    for elementas in kazkoks_sarasas:
        listas = list(elementas)
        naujas = (listas[0], sum(listas[1])/len(listas[1]))
        naujas_sarasas.append(naujas)
    return naujas_sarasas

# Tuples
tuple1 = ("labas", [100, 185])
tuple2 = ("ka veiki", [800, 1236])
tuple3 = ("viso gero", [1773, 1794])

sarasas_tuple = [tuple1, tuple2, tuple3]

# Funkcijos iškvietimas
print(priemimo_funkcija(sarasas_tuple))


