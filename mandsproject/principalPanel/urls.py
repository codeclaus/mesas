from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('register2', views.register2, name='register2'),
    path('close', views.close_sesion, name="close"),
    path('logear', views.logear, name="logear"),
    path('logear2', views.logear2, name="logear2"),
    path('send_email/', views.send_email, name='send_email'),
    path('success/', views.success, name='success'),
]
