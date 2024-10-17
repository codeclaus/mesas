# aqui solo crearemos una variable global donde se va a acumular la suman de lo que se tenga en session del user
def Ptotal(request):
    total = 0
    for k, v in request.session["car"].items():
        total += float(v["price"])*1000
    return {"valtotal": total}
