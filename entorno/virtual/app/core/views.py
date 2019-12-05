from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def indexcore(request):

    FormContact = ContactForm()

    if request.method == 'post':

        FormContact = ContactForm(data=request.post)

        if FormContact.is_valid():

            email = request.post.get('email', '')
            tipom = request.post.get('tipom', '')
            nombre = request.post.get('nombre', '')
            mensaje = request.post.get('mensaje', '')

            FormContact.save()
            return redirect(reverse('inicio')+"?ok")

    return render(request, 'core/index.html', {'formulario': FormContact})

    # return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def perfil(request):
    return render(request, 'core/perfil.html')