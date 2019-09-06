import model
import bottle

igra = model.Igra(12,12,50)

@bottle.get("/")
def index():
    return bottle.template("main.tpl", igra=igra)

@bottle.get("/igraj")
def igraj():
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