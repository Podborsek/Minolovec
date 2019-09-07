import math
import random

#Definiramo konstante

ZMAGA = "+"
PORAZ = "-"

ODKRITA = "od"
ZAKRITA = "zak"
ZASTAVICA = "zas"

NAPAKA = "eee"


class Igra:
    '''Osnovni objekt, ki predstavlaj igro'''

    def __init__(self, visina, sirina, tezavnost, prvi_y = 0, prvi_x = 0):
        '''Od pomoznih funkcij prejmemo matrike in jih zdruzimo v slovar'''
        self.visina = visina
        self.sirina = sirina
        self.prvi = (prvi_x,prvi_y)
        self.tezavnost = tezavnost
        self.poraz = False

        matrika_os = polje_osnovno(visina, sirina, tezavnost, prvi_y, prvi_x)
        matrika_so = polje_sosedi(matrika_os)

        slovar = {}
        #Slovar ima za kljuce koordiante, za vrednosti pa sezname oblike [bomba(T/F), sosede(0-8), odkritost(1/2/3)]
        for x in range(sirina):
            for y in range(visina):
                slovar[(x,y)] = [matrika_os[y][x], matrika_so[y][x], ZAKRITA]
        self.slovar = slovar
    
    def __str__(self):
        sl = self.slovar
        niz = ""
        for y in range(self.visina):
            vrsta = ""
            for x in range(self.sirina):
                (_,b,c) = sl[(x,y)]
                if c == ODKRITA:
                    if b == 0:
                        vrsta += " "
                    else:
                        vrsta += str(b)
                elif c == ZAKRITA:
                    vrsta += "X"
                elif c == ZASTAVICA:
                    vrsta += "?"
                vrsta += " "
            niz += vrsta + "\n"
        return niz
    
    def odkrij(self, x, y):
        sl = self.slovar
        seznam = sl[(x,y)]
        bomba = seznam[0]
        sosede = seznam[1]
        odkritost = seznam[2]

        if odkritost == ODKRITA or odkritost == ZASTAVICA:
            return None
        else:
            self.slovar[(x,y)] = [bomba,sosede,ODKRITA]
        
        if sosede == 0:
            for (a,b) in [(x-1,y-1),(x, y-1),(x+1, y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                if 0 <= a < self.sirina and 0 <= b < self.visina:
                    self.odkrij(a,b)


    def izkoplji(self, x, y):
        seznam = self.slovar[(x,y)]
        (bomba, _, stanje) = seznam

        if stanje == ZASTAVICA or stanje == ODKRITA:
            return NAPAKA
        elif bomba == True:
            self.poraz = True
            return PORAZ
        else:
            self.odkrij(x,y)
            return None

    
    def posadi(self, x, y):
        stanje = self.slovar[(x,y)][2]

        if stanje == ODKRITA:
            return NAPAKA
        elif stanje == ZAKRITA:
            self.slovar[(x,y)] = self.slovar[(x,y)][:2] + [ZASTAVICA]
            return None
        elif stanje == ZASTAVICA:
            self.slovar[(x,y)] = self.slovar[(x,y)][:2] + [ZAKRITA]
            return None
    
    def zmaga(self):
        stevilo_zastavic = 0
        for seznam in self.slovar.values():
            if seznam[2] == ZASTAVICA:
                if not seznam[0]:
                    return False
                stevilo_zastavic += 1
            
        return stevilo_zastavic == self.tezavnost





#-----------------------------------------------------------------------
#------------------  P O M O Z N E    F U N K C I J E   ----------------
#-----------------------------------------------------------------------


def polje_osnovno(visina, sirina, tezavnost, prvi_y, prvi_x):
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

    nova = []
    for y in range(1, visina + 1):
        vrstica = []
        for x in range(1, sirina + 1):
            sosede = 0
            for (a,b) in [(x-1,y-1),(x, y-1),(x+1, y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                if oblazinjena[b][a]:
                    sosede += 1
            vrstica.append(sosede)
        nova.append(vrstica)

    return nova
