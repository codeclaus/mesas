# aquí modelaremos el funcionamiento del carrito de compras, claves: session, objeto
# el objeto es el que se crea con el modelo de los productos, los cuales, a traves de
# el id del producto
# la session se crea cuando se identifica el usuario, se logea y comienza a navegar por la pagina


class ShoppCar:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        car = self.session.get('car')
        if not car:
            car = self.session['car'] = {}
        self.car = car

    def aggArticle(self, p_ide):
        if (str(p_ide.id) not in self.car.keys()):
            self.car[p_ide.id] = {
                "pedo_id": p_ide.id,
                "name": p_ide.name,
                "price": str(p_ide.price),
                "cant": 1,
                "description": p_ide.description,
                "disponible": p_ide.available,
                "categorie": str(p_ide.categorie),
            }
        else:

            for k, v in self.car.items():
                if k == str(p_ide.id):
                    v["cant"] = v["cant"]+1
                    v["price"] = (float(
                        v["price"])+float(p_ide.price))
                    break
        self.salvar()

    def redArticle(self, p_i):
        for k, v in self.car.items():
            if k == str(p_i.id):
                v["cant"] = v["cant"]-1
                if v["cant"] < 1:
                    self.delArticle(p_i)
                v["price"] = (float(
                    v["price"])-float(p_i.price))
                break
        self.salvar()

    def salvar(self):
        self.session["car"] = self.car
        self.session.modified = True

    def delArticle(self, p_i):
        p_i.id = str(p_i.id)
        if p_i.id in self.car:
            del self.car[p_i.id]
            self.salvar()

    def delArticleA(self, p_ido):
        p_ido.id = str(p_ido.id)
        if p_ido.id in self.car:
            del self.car[p_ido.id]
            self.salvar()

    def clnCar(self):
        car = self.session["car"] = {}
        self.session.modified = True
