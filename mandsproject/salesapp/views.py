from django.shortcuts import redirect
from .models import saleArticles
from shoppcar.car import ShoppCar
from django.contrib.auth.models import User
# Create your views here.


def sales_view(request):
    usuario = request.user.username
    user = User.objects.get(username=usuario)
    all_articles = ShoppCar(request)
    all_a = all_articles.car
    for k, v in all_a.items():
        saleArticles.objects.create(
            user=user,
            name=v["name"],
            categorie=v["categorie"],
            quantify=v["cant"],
        )
        return redirect(request.path)
