from django.urls import path 
from . import views , api 
urlpatterns = [
    path('',views.contactview.as_view(),name='contactview'),

    #api
    path('api/list',api.contact_api,name='contact_api')
]
