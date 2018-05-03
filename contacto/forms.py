from django import forms

# our new form
class ContactForm(forms.Form):
    nombre = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    comentarios = forms.CharField(
        required=True,
    )
    