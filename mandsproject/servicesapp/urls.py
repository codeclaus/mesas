from django.urls import path
from . import views
from . import cancelshop

urlpatterns = [
    path('', views.mands_view, name='servicesapp'),
    path('page/', cancelshop.pagar, name='page'),
    # path('cancelShop/', cancelshop.cancelShop, name='cancelShop'),
]
