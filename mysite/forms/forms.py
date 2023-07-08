from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class BasicForm(forms.Form):
    nome = forms.CharField(validators=[
        validators.MinLengthValidator(2, "Please enter 2 or more characters")])
    email = forms.EmailField()
    cpf = forms.IntegerField(validators=
        [validators.MaxLengthValidator(11, "Não deve ultrapassar 11 caracteres"),
         validators.MinLengthValidator(11, "Deve ter, no mínimo, 11 caracteres")])
    senha = forms.CharField()
