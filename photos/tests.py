from django.test import TestCase
from .models import Photo, Category
# Create your tests here.

class GalleryTestClass(TestCase):
    def setUp(self):
        self.new_category = Category(category_name='Code')
        self.new_category.save_category()
        
    def tearDown(self):
        Category.objects.all().delete()
        Photo.objects.all().delete()
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Photo))
        self.assertTrue(isinstance(self.new_category,Category))
    
    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Photo.objects.all()
        self.assertTrue(len(all_objects)>0)
    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Photo.objects.filter(image_name='moringa')
        Photo.delete_image(filtered_object)
        all_objects = Photo.objects.all()
        self.assertTrue(len(all_objects) == 0)
    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Photo.retrieve_all()
        self.assertEqual(all_objects.get(id=1).image_name,'moringa')
    def test_update_single_object_property(self):
        self.new_image.save_image()
        # # fetched = Image.objects.get(image_name='Greener')
        # self.assertEqual(fetched.get(id=1).image_name,'Greener')
    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Photo.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)
    def test_search_by_category(self):
        self.new_image.save_image()
        fetch_specific = Category.objects.get(category_name='Code')
        self.assertTrue(fetch_specific.category_name=='Code')

