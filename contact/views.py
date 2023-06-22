from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView 
from .models import modelcontact
from .forms import contactform
from django.core.mail import send_mail
# Create your views here.


class contactview(CreateView):
    model = modelcontact
    template_name = "contact.html"
    form_class = contactform

    
    def get_success_url(self):
        return reverse(
            "contactview" 
        )
    

    # send_mail(
    # "Subject here",
    # "Here is the message.",
    # "from@example.com",
    # ["to@example.com"],
    # fail_silently=False,
# )



# mypasswordemail : eeaxbwhubfsnsenf