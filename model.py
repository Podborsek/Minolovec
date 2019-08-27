import math
import random

class Igra:
    '''Osnovni objekt, ki predstavlaj igro'''

    def __init__(self, visina, sirina, tezavnost, prvi_y = 0, prvi_x = 0):
        #Od pomoznih funkcij prejmemo matrike in jih zdruzimo v slovar
        matrika = polje_osnovno(visina, sirina, tezavnost, prvi_y = 0, prvi_x = 0)
        pass










def polje_osnovno(visina, sirina, tezavnost, prvi_y = 0, prvi_x = 0):
    '''Funkcija sestavi polje navedena velikosti in primerne tezavnosti(stevilo min). Vrne True/False matriko.'''
    #Naredimo seznam sprejemljivih lokacij za mine
    vse = list(range(visina * sirina))
    prvi = prvi_y * sirina + prvi_x
    okolica = [prvi - sirina - 1, prvi - sirina, prvi - sirina + 1, prvi - 1, prvi, prvi + 1, prvi + sirina - 1, prvi + sirina, prvi + sirina + 1]
    for st in okolica:
        if st in vse:
            vse.remove(st)

    mine = random.sample(vse, tezavnost)

    matrika = []
    for y in range(visina):
        vrstica = []
        for x in range(sirina):
            if (y * sirina + x) in mine:
                vrstica.append(True)
            else:
                vrstica.append(False)
        matrika.append(vrstica)
    
    return matrika

def polje_sosedi(matrika):
    '''Sprejme matriko lokacij min in vrne matriko, ki pove koliko min je v okolici tocke.'''
    visina = len(matrika)
    sirina = len(matrika[0])

    oblazinjena = [[False for x in range(sirina + 2)]]
    for vrstica in matrika:
        oblazinjena.append([False] + vrstica + [False])
    oblazinjena.append([False for x in range(sirina + 2)])
    print(oblazinjena)

    nova = []
    for y in range(1, visina + 1):
        vrstica = []
        for x in range(1, sirina + 1):
            sosede = 0
            for (a,b) in [(x-1,y-1),(x, y-1),(x+1, y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                if oblazinjena[a][b]:
                    sosede += 1
            vrstica.append(sosede)
        nova.append(vrstica)
    
    return nova

    

qwe = polje_osnovno(4,4,7)
print(qwe)
print(polje_sosedi(qwe))