# aqui vamos a recuperar lo guardado hasta ahora en la session y lo vamos a enviar al correo, una vez
# se haga el envio, la pagina va a redirigir al home, donde al tiempo, vamos a llamar a la función borrar, para
# que limpie el carro
from shoppcar.car import ShoppCar
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from shoppcar.context_processor import Ptotal
from salesapp.views import sales_view


def pagar(request):
    totality = Ptotal(request)
    tot = totality['valtotal']
    asunto = "pedido"
    ser = ShoppCar(request)
    tanto = ser.car.items()
    usuario = request.user.username
    correo = request.user.email
    corres = str(correo)
    sales_view(request)
    send_dict_email(asunto, corres, tanto, tot)
    ser.clnCar()
    return render(request, 'cancelShop2.html', {"data": tanto, "val": tot, "user": usuario, "correo": correo})


def send_dict_email(subject, to_email, tanto, tot):
    # Renderiza el diccionario a una plantilla HTML
    html_content = render_to_string(
        'cancelShop.html', {'data': tanto, "val": tot})

    # Crea el mensaje de correo
    email = EmailMessage(
        subject,
        html_content,
        to_email,
        [to_email, "jhonbtm1998@gmail.com"]
    )
    email.content_subtype = "html"  # Define el contenido como HTML
    email.send()


# def cancelShop(request):
#     return render(request, 'cancelShop.html')
