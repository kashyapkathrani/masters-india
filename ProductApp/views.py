from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from ProductApp.models import Category, SubCategory, Product
from ProductApp.serializer import CategorySerializer, SubCategorySerializer, ProductSerializer


@api_view(['GET'])
def get_categories(request):
    """
    Method to retrieve all categories
    """
    
    categories = Category.objects.all()
    category_serializer = CategorySerializer(categories, many=True)

    return Response(category_serializer.data)

@api_view(['GET'])
def get_subcategories(request, category_id):
    """
    Method to retrieve subcatergories for a categoory
    """

    subcategories = SubCategory.objects.filter(category=category_id)
    subcategory_serializer = SubCategorySerializer(subcategories, many=True)

    return Response(subcategory_serializer.data)

@api_view(['GET'])
def get_products(request):
    """
    Method to retrieve products by category or subcategory
    """

    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')

    if subcategory_id:
        products = Product.objects.filter(sub_category = int(subcategory_id))
        product_serializer = ProductSerializer(products, many=True)

        return Response(product_serializer.data)

    if category_id:
        products = Product.objects.filter(sub_category__category = int(category_id))
        product_serializer = ProductSerializer(products, many=True)

        return Response(product_serializer.data)

    products = Product.objects.all()
    product_serializer = ProductSerializer(products, many=True)

    return Response(product_serializer.data)

@api_view(['POST'])
def add_product(request):
    """
    Method to add product for existing subcategory
    """

    product_data = JSONParser().parse(request)
    products_serializer = ProductSerializer(data=product_data)
    if products_serializer.is_valid():
        products_serializer.save()
        return Response({"message": "Added Successfully!"})

    return Response({"message":"Failed to add."})
