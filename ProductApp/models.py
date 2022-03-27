from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Model for Categories with field - Name
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    """
    Model for Subcategories with fields - Name and Category (as Foriegn Key)
    """
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model for Products with fields - Name and Sub Category (as Foriegn Key)
    """
    name = models.CharField(max_length=250)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name