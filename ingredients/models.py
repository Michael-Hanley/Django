from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Ingredient_Model(models.Model):
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    unit_of_measure = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.ingredient_text

