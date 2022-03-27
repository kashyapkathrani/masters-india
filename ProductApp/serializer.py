from rest_framework import serializers

from ProductApp.models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category Model
    """
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for SubCategory Model
    """
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product Model
    """
    class Meta:
        model = Product
        fields = '__all__'