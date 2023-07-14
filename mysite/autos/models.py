from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=220,
        help_text="Entre com uma montadora, tipo ASX.",
        validators=[MinLengthValidator(2, "Tem que ser maior que 1 caractere!")])
    
    def __str__(self):
        """String que representa o objeto do modelo"""
        return self.name
    

class Auto(models.Model):
    nickname = models.CharField(max_length=200, 
        validators=[MinLengthValidator(2, "Tem que ser maior que 1 caractere!")])
    make = models.ForeignKey('Make', on_delete=models.SET_NULL, null=True)
    mileage = models.PositiveIntegerField(default=0)
    comments = models.CharField(max_length=320)

    def __str__(self):
        return self.nickname