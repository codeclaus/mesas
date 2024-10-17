from django.shortcuts import render
from products.models import categories, productsP
# Create your views here.


def mands_view(request):
    products = productsP.objects.all()
    return render(request, "services.html", {"prod": products})
