
from django.shortcuts import render
from .models import Recipe

def main(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    return render(request, 'main.html', {'latest_recipes': latest_recipes})