from django.urls import path
from . import views

urlpatterns = [
    # SYSTEM ROUTES FULLSTACK
    path('suppliers/list/', views.SuppliersListView.as_view(), \
        name='suppliers_list'),
    path('suppliers/create/', views.SuppliersCreate.as_view(), \
        name='suppliers_create'),
    path('suppliers/<int:pk>/detail/', views.SuppliersDetail.as_view(), \
        name='suppliers_detail'),
    path('suppliers/<int:pk>/update/', views.SuppliersUpdate.as_view(), \
        name='suppliers_update'),
    path('suppliers/<int:pk>/delete/', views.SuppliersDelete.as_view(), \
        name='suppliers_delete'),

    # API ROUTES
    path('api/v1/suppliers/', views.SupplierCreateListAPIView.as_view(), 
        name='supplier-create-list-api-view'),
    path('api/v1/suppliers/<int:pk>', 
        views.SupplierRetrieveUpdateDestroyAPIView.as_view(), 
        name='supplier-detail-api-view'),
]
