# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
import json
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template import Context, Template
from django.template.loader import get_template



# our view
@csrf_exempt
def contacto(request):
    form_class = ContactForm
    
    # new logic!
    if request.method == 'POST':
        json_data = request.POST['json']
        data = json.loads(json_data)
        form = form_class(data=data)
        print('data')
        # print(request.body)
        if form.is_valid():
            print('entro')
            Nombre = data['nombre']
            email = data['email']
            form_content = data['comentarios']

            template = get_template('contact_template.txt')
            context = {
                'Nombre': Nombre,
                'email': email,
                'form_content': form_content,
            }
            content = template.render(context)
            email = EmailMessage(
                "Nuevo contacto a traves de la pagina web",
                content,
                "Contacto a travez de Página WEB" +'',
                ['rodrigohernan.ramos@gmail.com','danajuliamehle@gmail.com'],
                headers = {'Reply-To': email }
            )
            print('enviandoo')
            email.send()
            print("se envioo")
            return HttpResponse(json.dumps({'data': 'mail Enviado'}))
        else: 
            print(form)
            return HttpResponse(json.dumps({'data': 'form no valido'}))
    return render(request, 'contacto.html', {
        'form': form_class,
    })

