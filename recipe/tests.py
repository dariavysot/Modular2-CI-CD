from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe

class RecipeAppTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Тестова категорія")
        self.recipe = Recipe.objects.create(
            title="Тестовий рецепт",
            description="Опис тестового рецепта",
            ingredients="Інгредієнти",
            instructions="Інструкції",
            category=self.category
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Тестова категорія")
        self.assertEqual(str(self.category), "Тестова категорія")

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Тестовий рецепт")
        self.assertEqual(self.recipe.category.name, "Тестова категорія")

    def test_main_view_status_code_and_template(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, "Тестовий рецепт")

    def test_category_list_view_status_code_and_template(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertContains(response, "Тестова категорія")