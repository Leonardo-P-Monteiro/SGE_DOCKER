from django.urls import path
from . import views

urlpatterns = [
    path('brands/list/', views.BrandListView.as_view(), name='brand_list'),
    path('brands/create/', views.BrandCreate.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/', views.BrandDetail.as_view(), \
        name='brand_detail'),
    path('brands/<int:pk>/update/', views.BrandUpdate.as_view(), \
        name='brand_update'),
    path('brands/<int:pk>/delete/', views.BrandDelete.as_view(), \
        name='brand_delete')
]
