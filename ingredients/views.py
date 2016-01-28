from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from ingredients.models import Ingredient_Model
import requests

from ingredients.serializer import IngredientSerializer

def ingredient_view(request):
    query_url ='http://10.12.5.85:8529/_db/_system/ingredients/ingredients'
    r = requests.get('http://10.12.5.85:8529/_db/_system/ingredients/ingredients')
    json = r.json()
    serializer = IngredientSerializer(data=json)
    if serializer.is_valid():
        ingredient = serializer.save()
        context = {'ingredient': ingredient}
        return render(request, 'ingredient.html', context)
