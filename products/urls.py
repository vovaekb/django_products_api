from django.urls import path
from products import views

urlpatterns = [
    path('categories/', views.categories_list),
    path('products/', views.products_list)
]