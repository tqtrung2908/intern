from django.urls import path
from store.API import views

urlpatterns = [
    path('category_list/', views.CategoryList.as_view(), name='category_list'),
    path('category_create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category_detail/<int:id>', views.CategoryDetail.as_view(), name='category_detail'),
    path('category_report/', views.CategoryReport.as_view(), name='category_report'),

    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('product_create/', views.ProductCreate.as_view(), name='product_create'),
    path('product_detail/<int:id>', views.ProductDetail.as_view(), name='product_detail'),
    path('product_report/', views.ProductReport.as_view(), name='product_report'),

]