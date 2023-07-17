from django.db import models

# Create your models here.

class Breed(models.Model):
    name = models.CharField(max_length=120)

    def __init__(self):
        return self.name


class Cat(models.Model):
    nickname = models.CharField(max_length=120)
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=120)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __init__(self):
        return self.nickname