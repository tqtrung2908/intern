from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('product_show/<product_id>', views.product_show, name='product_show'),
    path('products/', views.all_products, name="all_products"),
    path('add_product/', views.add_product, name="add_product"),
    path('product_update/<product_id>', views.product_update, name='product_update'),
    path('product_delete/<product_id>', views.product_delete, name='product_delete'),

    path('category_show/<category_id>', views.category_show, name='category_show'),
    path('categories/', views.all_categories, name="all_categories"),
    path('add_category/', views.add_category, name="add_category"),
    path('category_update/<category_id>', views.category_update, name='category_update'),
    path('category_delete/<category_id>', views.category_delete, name='category_delete'),
]
