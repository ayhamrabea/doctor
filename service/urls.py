from django.urls import path 
from . import views    
urlpatterns = [
    path('',views.services.as_view(),name='services'),
    path('detail/<int:pk>',views.serv_detail.as_view(),name='serv_detail'),
]
