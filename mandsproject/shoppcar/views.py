from django.shortcuts import redirect
from products.models import productsP
from .car import ShoppCar

# Create your views here.


def aggArticle(request, p_id):
    car = ShoppCar(request)
    prod_conf = productsP.objects.get(id=p_id)
    car.aggArticle(p_ide=prod_conf)
    return redirect("servicesapp")


def redArticle(request, p_id):
    car = ShoppCar(request)
    prod_conf = productsP.objects.get(id=p_id)
    car.redArticle(p_i=prod_conf)
    return redirect("servicesapp")


def delArticle(request, p_id):
    car = ShoppCar(request)
    prod_conf = productsP.objects.get(id=p_id)
    car.delArticleA(p_ido=prod_conf)
    return redirect("servicesapp")


def clnArticle(request):
    car = ShoppCar(request)
    car.clnCar()
    return redirect("servicesapp")
