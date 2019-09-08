import model

#=================================================================================================================================
#=================== I Z P I S ===================================================================================================
#=================================================================================================================================

def izpis_igre(igra):
    niz = "==" * igra.sirina + "\n"

    if igra.sirina == 9:
        niz += "a b c d e f g h i\n"
    elif igra.sirina == 12:
        niz += "a b c d e f g h i j k l\n"

    sl = igra.slovar
    for y in range(igra.visina):
        vrsta = ""
        for x in range(igra.sirina):
            (_,b,c) = sl[(x,y)]
            if c == model.ODKRITA:
                if b == 0:
                    vrsta += " "
                else:
                    vrsta += str(b)
            elif c == model.ZAKRITA:
                vrsta += "X"
            elif c == model.ZASTAVICA:
                vrsta += "?"
            vrsta += " "
        niz += vrsta + str(y + 1) + " \n"

    print(niz)

def izpis_zmage():
    print("Čestitke!")

def izpis_poraza():
    return "BUM!"


#================================================================================================================================
#============= I N P U T ========================================================================================================
#================================================================================================================================

def zahtevaj_vnos():
    return input("Napišite tip ugibanja in kooordinate polja:")

def preveri_vnos(igra, vnos):
    '''Vrne False, če je vnos neustrezen, drugače vrne ustrezen seznam'''
    n1 = vnos.strip()
    niz = n1.lower()

    if niz == "restart" or niz == "start":
        zazeni_vmesnik()

    if "," in niz:
        sez = niz.split(",")
    elif " " in niz:
        sez = niz.split(" ")
    else:
        return False
    
    if len(sez) != 3:
        return False

    (oblika, crka, stevilka) = sez

    if isinstance(oblika, str) and isinstance(crka, str) and stevilka in "0123456789101112131415":
        pass
    else:
        return False

    crka = abc_v_int(crka)
    stevilka = int(stevilka)


    if oblika in ["o", "z", "odkrij", "zastavica"] and 0 < crka <= igra.sirina and 0 < stevilka <= igra.visina:
        return [oblika, crka, stevilka]
    else:
        return False

def vnesi(igra, niz):
    lep = preveri_vnos(igra, niz)
    if lep == False:
        print("Neustrezen vnos")
        vnesi(igra, zahtevaj_vnos())
    else:
        (tip, x, y) = lep
        x = int(x) - 1
        y = int(y) - 1
        if tip in ["o", "odkrij"]:
            igra.izkoplji(x,y)
        else:
            igra.posadi(x,y)


def izbira_tezavnosti():
    niz = input("Za pričetek izberite težavnost!\nLAHKA ==> 9x9 z 12 minami\nSREDNJE ==> 12x12 z 25 minami\nTEZKO ==> 12x12 z 54 minami\n").lower()
    if niz == "lahka":
        return (9,9,12)
    elif niz == "srednje":
        return (12,12,25)
    elif niz == "tezko":
        return (12,12,54)
    else:
        print("Neustrezen vnos")
        return izbira_tezavnosti()

def abc_v_int(znak):
    '''Funkcija crko pretvori v ustrezno stevilko'''
    crka = znak.lower()
    if crka in "abcdefghijkl":
        return "abcdefghijkl".index(crka) + 1
    else:
        return 100



#=================================================================================================================================
#=================I Z V A J A N J E ==============================================================================================
#=================================================================================================================================

def nova_igra():
    vnos = input("Ali želite igrati novo igro?(odgovorite z da/ne)")
    if vnos.lower() == "da":
        zazeni_vmesnik()
    else:
        pass




def zazeni_vmesnik():
    #Navodila
    print("M I N O L O V E C\n\nCilj igre je označiti vse mine. Številka v polju pove koliko min je na sosednjih poljih.\nČe mislite, da je polje varno ga lahko odkrijete. Polja na katerih so mine označite z zastavico.\nPolje odkrijete/označite tako, da napišete tip ugibanja o/z, potem črko stolpca in na koncu številko vrstice,\nna primer: z c 5\nIgra se konča, ko označite vse mine ali ko odkopljete mino.\n")

    #Igralec najprej izbere tezavnost
    a,b,c = izbira_tezavnosti()

    if a == 9:
        print("a b c d e f g h i")
    elif a == 12:
        print("a b c d e f g h i j k l")

    for y in range(a):
        print("X " * a + "{}".format(y + 1))


    #Igralec izbere prvo polje preden zares začnemo igro, tako preprečimo, da bi bila že prva poteza na mini
    while True:
        vnos = zahtevaj_vnos()
        lep = preveri_vnos(model.Igra(a,b,c), vnos)

        if lep == False:
            continue
        else:
            (_,d,e) = lep
            break


    #Naredimo igro in vnesemo prvo potezo
    igra = model.Igra(a,b,c, int(e) - 1, int(d) - 1)
    vnesi(igra, vnos)

    #Dejansko zacnemo igro
    while True:
        #Izpišemo stanje
        print(izpis_igre(igra))
        
        #Igralec ugiba
        niz = zahtevaj_vnos()
        vnesi(igra, niz)


        #Preverimo če je igralec zmagal ali izgubil
        if igra.poraz:
            print(izpis_poraza())
            break

        if igra.zmaga():
            print(izpis_zmage())
            break
    
    nova_igra()
    return


zazeni_vmesnik()