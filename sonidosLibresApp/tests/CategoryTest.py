from rest_framework import status
from rest_framework.test import APITestCase

from sonidosLibresApp.models import Category

class CategoryTest(APITestCase):

    def testGetCategories(self):
        url = '/api/categories'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testCreateCategory(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.get().name, 'categoriaDemo')


    def testUpdateCategory(self):
        #category=Category.objects.get()

        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }

    def testDeleteCategory(self):
        url = '/api/categories/'
