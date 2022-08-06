from django.db import models
from rest_framework import serializers
from store.models import Category, Product, Image


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id',
                  'title',
                  'parent']


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers(many=True, required=False, read_only=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=True, allow_null=True, use_url=True, required=False)

    class Meta:
        model = Product
        fields = ['id',
                  'title',
                  'category',
                  'description',
                  'image',
                  'price']


class ImagesSerializers(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    image = serializers.ImageField(required=True)

    class Meta:
        model = Image


class ProductCreateSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=True, allow_null=True, use_url=True, required=False)

    class Meta:
        model = Product
        fields = ['id',
                  'title',
                  'category',
                  'description',
                  'image',
                  'price']

        def create(self, validated_data):
            image_data = validated_data.pop('image')
            category_data = validated_data.pop('category')
            product = Product(**validated_data)
            product.save()

            return ProductSerializers(product).data


class CategoryReportSerializers(serializers.Serializer):
    category = CategorySerializers()
    total_category = serializers.DecimalField(decimal_places=0, max_digits=None)


class ProductReportSerializers(serializers.Serializer):
    product = ProductSerializers()
    total_product = serializers.DecimalField(decimal_places=0, max_digits=None)

