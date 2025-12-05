from django.urls import path
from . import views

urlpatterns = [
    # SYSTEM ROUTES FULLSTACK
    path('outflows/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', views.OutflowCreate.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetail.as_view(), \
        name='outflow_detail'),
    
    # API ROUTES
    path('api/v1/outflows/', views.OutflowCreateListAPIView.as_view(), 
        name='outflow-create-list-api-view'),
    path('api/v1/outflows/<int:pk>', 
        views.OutflowRetrieveAPIView.as_view(), 
        name='outflow-detail-api-view'),
]
