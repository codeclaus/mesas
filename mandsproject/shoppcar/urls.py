from django.urls import path
from . import views

app_name = "car"
urlpatterns = [
    path('agg/<int:p_id>/', views.aggArticle, name='agg'),
    path('red/<int:p_id>/', views.redArticle, name='red'),
    path('delA/<int:p_id>/', views.delArticle, name='delA'),
    path('cln/', views.clnArticle, name='cln'),
]
