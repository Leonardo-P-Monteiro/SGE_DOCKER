from django.urls import path
from . import views

urlpatterns = [
    # SYSTEM ROUTES FULLSTACK
    path('brands/list/', views.BrandListView.as_view(), name='brand_list'),
    path('brands/create/', views.BrandCreate.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/', views.BrandDetail.as_view(), \
        name='brand_detail'),
    path('brands/<int:pk>/update/', views.BrandUpdate.as_view(), \
        name='brand_update'),
    path('brands/<int:pk>/delete/', views.BrandDelete.as_view(), \
        name='brand_delete'),

    # API ROUTES
    path('api/v1/brands/', views.BrandCreateListAPIView.as_view(), 
        name='brand-create-list-api-view'),
    path('api/v1/brands/<int:pk>', 
        views.BrandRetrieveUpdateDestroyAPIView.as_view(), 
        name='brand-detail-api-view'),
]
