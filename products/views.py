from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def categories_list(request):
    """
    Returns a list of :model:`products.Category`.
    """
    categories = Category.objects.all()

    categories_serializer = CategorySerializer(categories, many=True)
    return JsonResponse(categories_serializer.data, safe=False)

@api_view(['GET'])
def products_list(request):
    """
    Returns a list of :model:`products.Product`.
    """
    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)
    return JsonResponse(products_serializer.data, safe=False)