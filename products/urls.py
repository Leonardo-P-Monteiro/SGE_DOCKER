from django.urls import path
from . import views

urlpatterns = [
    # SYSTEM ROUTES FULLSTACK
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/detail/', views.ProductDetail.as_view(), \
        name='product_detail'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), \
        name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), \
        name='product_delete'),

    # API ROUTES
    path('api/v1/products/', views.ProductCreateListAPIView.as_view(), 
        name='product-create-list-api-view'),
    path('api/v1/products/<int:pk>', 
        views.ProductRetrieveUpdateDestroyAPIView.as_view(), 
        name='product-detail-api-view'),
]
