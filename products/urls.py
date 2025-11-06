from django.urls import path
from . import views

urlpatterns = [
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/detail/', views.ProductDetail.as_view(), \
        name='product_detail'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), \
        name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), \
        name='product_delete')
]
