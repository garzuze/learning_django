from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class BasicForm(forms.Form):
    nome = forms.CharField(validators=[
        validators.MinLengthValidator(2, "Please enter 2 or more characters")])
    email = forms.EmailField()
    cpf = forms.IntegerField(validators=
        [validators.MaxLengthValidator(14, "Não deve ultrapassar 14 caracteres"),
         validators.MinLengthValidator(14, "Deve ter, no mínimo, 14 caracteres")])
    senha = forms.CharField(widget = forms.PasswordInput())
