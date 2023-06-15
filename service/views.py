from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import service
# Create your views here.


class services(ListView):
    model = service
    context_object_name = 'services'
    template_name='service.html'



class serv_detail(DetailView):
    model = service
    pk_url_kwarg = 'pk'
    context_object_name = 'services'
    template_name='deatail.html'
