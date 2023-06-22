from django.urls import path 
from . import views , api
urlpatterns = [
    path('',views.make_appoitment.as_view(),name='make_appoitment'),

    #api
    path('api/list',api.Appoitment_api,name='Appoitment_api')

]
