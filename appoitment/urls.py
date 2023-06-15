from django.urls import path 
from . import views
urlpatterns = [
    path('',views.make_appoitment.as_view(),name='make_appoitment'),
]
