# Generated by Django 4.2.3 on 2023-07-14 12:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Entre com uma montadora, tipo ASX.', max_length=220, validators=[django.core.validators.MinLengthValidator(2, 'Tem que ser maior que 1 caractere!')])),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Tem que ser maior que 1 caractere!')])),
                ('mileage', models.PositiveIntegerField(default=0)),
                ('comments', models.CharField(max_length=320)),
                ('make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autos.make')),
            ],
        ),
    ]
