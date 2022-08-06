from dataclasses import dataclass
from decimal import Decimal
from django.db.models import Sum, Count
from store.models import Category, Product


@dataclass
class CategoryReport:
    category: Category
    total_category: Decimal


@dataclass
class ProductReport:
    product: Product
    total_product: Decimal


def category_report():
    data = []

    queryset = Product.objects.values("category").annotate(
        total_product=Count('id'),
    )

    categories_index = {}
    for category in Category.objects.all():
        categories_index[category.id] = category

    for item in queryset:
        category = categories_index[item['category']]
        data_input = CategoryReport(category, item['total_product'])
        data.append(data_input)

    return data


def product_report():
    data = []

    for item in Product.objects.all():
        data_input = ProductReport(item)
        data.append(data_input)

    return data

