from django.db import models
from django import forms

# Create your models here.
class ItemModel(models.Model):
    choices = (
                    ('mustitem', '必需品'),
                    ('notmustitem', '娯楽品'),
                )
    name = models.CharField('itemname', max_length=200)
    price = models.IntegerField('price', max_length=140, blank=True)
    type = models.CharField('type', max_length=30, choices=choices)
    date = models.DateField('date', max_length=1000)