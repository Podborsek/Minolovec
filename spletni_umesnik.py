import model
import bottle

igra = model.Igra(12,20,40,5,5)
'''
@bottle.get("/")
def index():
    return bottle.template("izbira_tezavnosti.tpl")



@bottle.post("/nova_igra")
def nova_igra():
    global tezavnost
    tezavnost = bottle.request.forms.getunicode("tezavnost")
    print(tezavnost)
    return bottle.template("nova_igra.tpl", tezavnost=tezavnost)

'''

@bottle.get("/")
def index():
    return bottle.template("main.tpl", igra=igra)

@bottle.post("/igraj")
def ugibaj():
    ugib = bottle.request.forms.getunicode("gumb")

    tip,x,y = ugib.split(",")
    x,y = int(x),int(y)

    if tip == "o":
        igra.izkoplji(x,y)
    elif tip == "z":
        igra.posadi(x,y)

    return bottle.template("main.tpl", igra=igra)






bottle.run(reloder=True, debug=True)