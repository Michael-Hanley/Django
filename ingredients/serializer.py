from rest_framework import serializers
from .models import Ingredient_Model

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient_Model
        fields = ('price_per_unit', 'unit_of_measure', 'name')
