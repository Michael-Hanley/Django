from django.db import models

class Ingredient(models.Model):
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    unit_of_measure = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
