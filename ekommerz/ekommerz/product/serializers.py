from rest_framework import serializers

from .models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all_-"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = "__all__"
