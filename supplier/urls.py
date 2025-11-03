from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/list/', views.SuppliersListView.as_view(), \
        name='suppliers_list'),
    path('suppliers/create/', views.SuppliersCreate.as_view(), \
        name='suppliers_create'),
    path('suppliers/<int:pk>/detail/', views.SuppliersDetail.as_view(), \
        name='suppliers_detail'),
    path('suppliers/<int:pk>/update/', views.SuppliersUpdate.as_view(), \
        name='suppliers_update'),
    path('suppliers/<int:pk>/delete/', views.SuppliersDelete.as_view(), \
        name='suppliers_delete')
]
