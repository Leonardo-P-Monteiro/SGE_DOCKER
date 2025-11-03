from django.urls import path
from . import views

urlpatterns = [
    path('categories/list/', views.CategoryListView.as_view(), \
        name='category_list'),
    path('categories/create/', views.CategoryCreate.as_view(), \
        name='category_create'),
    path('categories/<int:pk>/detail/', views.CategoryDetail.as_view(), \
        name='category_detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), \
        name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), \
        name='category_delete')
]
