from django.test import TestCase
from .models import Article
from django.utils.text import slugify
from .utils import slugify_instance_title
# Create your tests here.

class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_articals = 5
        for i in range(self.number_of_articals):
            Article.objects.create(name='Hello world', content='something else')
        
    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(),5)
        
    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by("id").first()
        name = obj.name
        slug = obj.slug
        slugify_title = slugify(name)
        self.assertEqual(slug, slugify_title)
        
    def test_hello_world_unique_slug(self):
        qs = Article.objects.exclude(slug__iexact= 'hello-world')
        for obj in qs:
            name = obj.name
            slug = obj.slug
            slugify_title = slugify(name)
            self.assertNotEqual(slug, slugify_title)
            
            


    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        new_slug = []
        for i in range(self.number_of_articals):
            instance = slugify_instance_title(obj, save=False)
            new_slug.append(instance.slug)
        unique_slug = list(set(new_slug))
        self.assertEqual(len(new_slug), len(unique_slug))
        
    def test_slugify_instance_title_redux(self):
        slug_list = Article.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slug_list))
        
    # def test_user_asdded_slug_unique(self):
    #     obj_user = Article.objects.create(name='hello world', content='any thingkind')
    #     slug_list =list(Article.objects.all().values_list('slug', flat=True))
    #     slug_list.append(obj_user.slug)
    #     unique_slug_list = list(set(slug_list))
    #     self.assertEqual(len(slug_list), len(unique_slug_list))
        
        
        
        
        
        
        