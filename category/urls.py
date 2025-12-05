from django.urls import path
from . import views

urlpatterns = [
    # SYSTEM ROUTES FULLSTACK
    path('categories/list/', views.CategoryListView.as_view(), \
        name='category_list'),
    path('categories/create/', views.CategoryCreate.as_view(), \
        name='category_create'),
    path('categories/<int:pk>/detail/', views.CategoryDetail.as_view(), \
        name='category_detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), \
        name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), \
        name='category_delete'),

    # API ROUTES
    path('api/v1/categories/', views.CategoryCreateListAPIView.as_view(), 
        name='category-create-list-api-view'),
    path('api/v1/categories/<int:pk>', 
        views.CategoryRetrieveUpdateDestroyAPIView.as_view(), 
        name='category-detail-api-view'),
]
