from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from .forms import appoitmentForm
# Create your views here.


class make_appoitment(CreateView):
    template_name = "appoitment.html"
    form_class = appoitmentForm

    
    def get_success_url(self):
        return reverse(
            "make_appoitment"
        )



# def make_appoitment(request):
    
#     return render(request,'appoitment.html')