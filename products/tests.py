from .models import Category, Product
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
import json

TEST_SIZE = 10


class TestCategory(APITestCase):
    def setUp(self):
        self.categories = []
        # create a set of test ads
        for i in range(TEST_SIZE):
            category = Category.objects.create(name='test_category_%s' % i)
            self.categories.append(category)

    def test_list_categories(self):
        # Invalid case - normal user
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProducts(APITestCase):
    def setUp(self):
        self.products = []
        # create a set of test ads
        for i in range(TEST_SIZE):
            product = Product.objects.create(title='test_product_%s' % i)
            self.products.append(product)

    def test_list_categories(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


