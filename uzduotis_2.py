# 2 užduotis
# Sukurti funkciją, kuri priimtų tuple ir grąžintų kitą tuple, tik su pašalintais dublikatais. Eiliškumas elementų turi išlikti toks pats:
# Pvz: jeigu funkcija priima (1, 2, 3, 4, 3, 2, 1) tuple, tai turėtų grąžinti (1, 2, 3, 4)
# Pvz: jeigu funkcija priima (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’, ‘q’, ‘h’, ‘d’) tuple, tai turėtų grąžinti (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’)
# Paduoti tuple į funkciją (reikšmes sugalvokite patys) ir išspausdinti funkcijos rezultatą.

from collections import OrderedDict

# Pati funkcija
def tuple_funkcija(kazkoks_tuple):
    istrinti_dublikatai = tuple(OrderedDict.fromkeys(kazkoks_tuple))
    return istrinti_dublikatai

# Mano pasirinkti tuple
mano_tuple = (1, 2, 3, 4, 3, 2, 1, 8, 4, 7, 1, 8, 1)
mano_kitas_tuple = ('a', 'd', 'g', 'h', 'i', 'g', 'q', 'h', 'd', 'g', 's', 'a')

# Funkcijos iškvietimas
print(tuple_funkcija(mano_tuple))
print(tuple_funkcija(mano_kitas_tuple))


