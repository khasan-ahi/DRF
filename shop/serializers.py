from rest_framework.serializers import ModelSerializer

from shop.models import Product, Category


class ProductSerializer(ModelSerializer):
    category = Category

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
