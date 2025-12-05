from django.urls import path
from . import views

urlpatterns = [
    # SYSTEM ROUTES FULLSTACK
    path('inflows/list/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', views.InflowCreate.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetail.as_view(), \
        name='inflow_detail'),
    
    # API ROUTES
    path('api/v1/inflows/', views.InflowCreateListAPIView.as_view(), 
        name='inflow-create-list-api-view'),
    path('api/v1/inflows/<int:pk>', 
        views.InflowRetrieveAPIView.as_view(), 
        name='inflows-detail-api-view'),
]
