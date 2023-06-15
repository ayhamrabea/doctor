from django.urls import path 
from . import views    
urlpatterns = [
    path('',views.services.as_view(),name='services'),
    path('doctor/<int:pk>',views.doctor_detail.as_view(),name='doctor_detail'),

]
