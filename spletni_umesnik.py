import model
import bottle


@bottle.get("/")
def index():
    return bottle.template("index.tpl")

bottle.run(reloder=True, debug=True)