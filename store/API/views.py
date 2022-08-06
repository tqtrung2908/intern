from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from store.models import Category, Product
from store.API.serializers import CategorySerializers, ProductSerializers, ProductCreateSerializers
from store.API.serializers import CategoryReportSerializers, ProductReportSerializers
from store.report import category_report, product_report
from rest_framework.response import Response


class CategoryList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializers

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializers

    def perform_create(self, serializer):
        return serializer.save()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializers
    lookup_field = 'id'

    def get_queryset(self):
        return Category.objects.all()


class ProductList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializers

    def get_queryset(self):
        return Product.objects.all()


class ProductCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductCreateSerializers

    def perform_create(self, serializer):
        return serializer.save()


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializers
    lookup_field = 'id'

    def get_queryset(self):
        return Product.objects.all()


class CategoryReport(APIView):
    def get(self, request):
        data = category_report()
        serializers = CategoryReportSerializers(instance=data, many=True)
        return Response(data=serializers.data)


class ProductReport(APIView):
    def get(self, request):
        data = product_report()
        serializers = ProductReportSerializers(instance=data, many=True)
        return Response(data=serializers.data)



