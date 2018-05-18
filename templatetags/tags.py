# app/templatetags/util.py
from django import template
register = template.Library()

'''para registrar todos los tags
    -crear una carpeta dentro de una app que se llame [templatetags]
    -dentro un archivo al cual vas a llamar desde el template [ej: tags.py]

    y dentro coloca la siguiente linea
        from rr.templatetags.tags import register
'''



@register.filter
def get_type(value):
    ''' ej:
    {%  if field.field.widget|get_type == 'CheckboxInput' %}
    '''
    return value.__class__.__name__

@register.filter
def pruebatag(value):
    return "prueba"

@register.filter
def cards_pinterest(count):
    '''
     modo de uso:
     class=" {{ object_list.count|cards_pinterest }}"   
    '''
    if count  >= 5:
        return 'cards-pinterest' 
    elif count  >= 3:
        return 'cards-pinterest-pocos'
    else:
        return 'cards-pinterest-dos' 
