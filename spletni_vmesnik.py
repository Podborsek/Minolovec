import model
import bottle

#Ustvarimo slovar, ki bo shranjeval igre
igre = []

@bottle.get("/")
def izbira_tezavnosti():
    return bottle.template("izbira_tezavnosti.tpl")


@bottle.post("/nova_igra")
def nova_igra():
    tezavnost = bottle.request.forms.getunicode("tezavnost")
    return bottle.template("nova_igra.tpl", tezavnost=tezavnost)

@bottle.post("/igraj")
def ugibaj():
    ugib = bottle.request.forms.getunicode("ugib")

    if ugib[0] == "n":
        #Naredi novo igro
        (_,a,b,c,d,e) = ugib.split(",")
        igre.append(model.Igra(int(a),int(b),int(c),int(e),int(d)))
        igra = igre[-1]
        igra.izkoplji(int(d),int(e))
    else:
        #Nadaljuje igro
        igra = igre[-1]
        tip,x,y = ugib.split(",")
        x,y = int(x),int(y)

        if tip == "o":
            igra.izkoplji(x,y)
        elif tip == "z":
            igra.posadi(x,y)

    if igra.zmaga():
        return bottle.template("zadnja_stran.tpl", vrednost="ZMAGA")
    elif igra.poraz == True:
        return bottle.template("zadnja_stran.tpl", vrednost="PORAZ")


    return bottle.template("main.tpl", igra=igra)



bottle.run(reloder=True)

