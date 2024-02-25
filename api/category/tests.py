
from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Category
# from .serializers import CategorySerializer

# class CategoryApiTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_create_category(self):
#         """
#         Ensure we can create a new category object.
#         """
#         initial_count = Category.objects.count()
#         new_category_data = {'name': 'Test Category'}
#         response = self.client.post('/category/', new_category_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Category.objects.count(), initial_count + 1)

#     def test_retrieve_categories(self):
#         """
#         Ensure we can retrieve a list of categories.
#         """
#         Category.objects.create(name='Test Category 1')
#         Category.objects.create(name='Test Category 2')
#         response = self.client.get('/categories/', format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)

#     def test_update_category(self):
#         """
#         Ensure we can update an existing category object.
#         """
#         category = Category.objects.create(name='Test Category')
#         updated_category_data = {'name': 'Updated Test Category'}
#         response = self.client.put(f'/category/{category.id}/', updated_category_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         category.refresh_from_db()
#         self.assertEqual(category.name, 'Updated Test Category')

#     def test_delete_category(self):
#         """
#         Ensure we can delete an existing category object.
#         """
#         category = Category.objects.create(name='Test Category')
#         response = self.client.delete(f'/category/{category.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Category.objects.filter(id=category.id).exists())

# # Create your tests here.
