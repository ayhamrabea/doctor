from django.urls import path 
from . import views , api

urlpatterns = [
    path('',views.mydoctor.as_view(),name='mydoctor'),
    path('doctor/<int:pk>',views.doctor_detail.as_view(),name='doctor_detail'),

    #api
    path('api/list',api.dentist_api,name='dentist_api')
]
