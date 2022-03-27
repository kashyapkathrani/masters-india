from django.urls import path
from ProductApp import views

urlpatterns = [
    path('category/', views.get_categories),
    path('<int:category_id>/subcategory/', views.get_subcategories),
    path('product/', views.get_products),
    path('product/add', views.add_product)
]
