from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredient
# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')
    def test_user_pw(self):
        checked = self.user_a.check_password("abc123")
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('klm',password="123abc")
        self.recipe_a = Recipe.objects.create(
            name= 'Grilled chicken',
            user= self.user_a,
        )
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe= self.recipe_a,
            name = 'chicken',
            quantity = '1/2',
            unit= 'pound',
        )
    
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEquals(qs.count(),1)
        
    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        self.assertEquals(qs.count(),1)
    def test_user_recipe_forword_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEquals(qs.count(),1)
    
    def test_recipe_ingreient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
        self.assertEquals(qs.count(),1)
    def test_recipe_ingredient_forword_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe= recipe)
        self.assertEquals(qs.count(),1)
    
    def test_user_two_levels_reverse_count_via_recipe(self):
        user = self.user_a
        Ids = user.recipe_set.all().values_list('id', flat=True)
        qs = RecipeIngredient.objects.filter(recipe__id__in = Ids)
        self.assertEquals(qs.count(),1)
    def test_user_two_levels_forword_count(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user = user)
        self.assertEquals(qs.count(),1)
    
    def test_user_two_levels_reverse_count(self):
        user = self.user_a
        recipe = self.recipe_a
        ingredient_ids = user.recipe_set.all().values_list('recipeingredient__id',flat=True)
        qs = RecipeIngredient.objects.filter(id__in= ingredient_ids)
        
class RecipeIngredientTest(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('klm',password="123abc")
        self.recipe_a = Recipe.objects.create(
            name= 'Grilled chicken',
            user= self.user_a,
        )
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe= self.recipe_a,
            name = 'chicken',
            quantity = '1/2',
            unit= 'pound',
        )
    
    def test_unit_measure_validation(self):
        ingredient = RecipeIngredient(
            name = 'new',
            quantity = 10,
            recipe = self.recipe_a,
            unit = 'pound'
        )
        ingredient.full_clean()
    
    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_float)