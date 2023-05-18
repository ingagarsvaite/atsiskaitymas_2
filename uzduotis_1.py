# 1 užduotis:
# Sukurti funkciją, kuri iš vardų sąrašo sudarytų sąrašą tik iš vardų pirmų raidžių ir tą sąrašą grąžintų:
# Pvz: paduodamas sąrašas į funkciją: [‘Jonas’, ‘Petras’, ‘Linas’], tai grąžinamas turėtų būti [‘J’, ‘P’, ‘L’]
# Paduoti vardų sąrašą į funkciją (vardus galite sugalvoti patys) ir atspausdinti funkcijos rezultatą.

# Funkcija
def vardu_funkcija(vardu_sarasas) :
    vardo_raide = []
    for vardas in vardu_sarasas:
        vardo_raide.append(vardas[0])
    return vardo_raide

# Pasirinktas vardų sąrašas
sarasas = ['Liutauras', "Valentina", "Radvilas", "Monika"]

print(vardu_funkcija(sarasas))

