import model

#=================================================================================================================================
#=================== I Z P I S ===================================================================================================
#=================================================================================================================================

def izpis_igre(igra):
    niz = "==" * igra.sirina + "\n"
    niz += str(igra)
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

def preveri_vnost(igra, vnos):
    '''Vrne False, če je vnos neustrezen, drugače vrne ustrezen seznam'''
    n1 = vnos.strip()
    niz = n1.lower()

    if "," in niz:
        sez = niz.split(",")
    elif " " in niz:
        sez = niz.split(" ")
    else:
        return False
    
    if sez[0] in ["o", "z", "odkrij", "zastavica"] and 0 < int(sez[1]) <= igra.sirina and 0 < int(sez[2]) <= igra.visina and len(sez) == 3:
        return sez
    else:
        return False

def vnesi(igra, niz):
    lep = preveri_vnost(igra, niz)
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
    niz = input("Izberite težavnost!\nLAHKA ==> 6X6 z 7 minami\nSREDNJE ==> 9x9 z 20 minami\nTEZKO ==> 12x12 z 40 minami\n").lower()
    if niz == "lahka":
        return (6,6,7)
    elif niz == "srednje":
        return (9,9,20)
    elif niz == "tezko":
        return (12,12,40)
    else:
        print("Neustrezen vnos")
        return izbira_tezavnosti()




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
    a,b,c = izbira_tezavnosti()

    for _ in range(a):
        print("X " * a)

    niz1 = zahtevaj_vnos()
    d,e = niz1.split()[1:]

    
    igra = model.Igra(a,b,c, int(d) - 1, int(e) - 1)
    vnesi(igra, niz1)
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