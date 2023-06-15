from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import doctor
# Create your views here.


class services(ListView):
    model = doctor
    context_object_name = 'doctors'
    template_name='our_doctors.html'



class doctor_detail(DetailView):
    model = doctor
    pk_url_kwarg = 'pk'
    context_object_name = 'doctors'
    template_name='detail.html'