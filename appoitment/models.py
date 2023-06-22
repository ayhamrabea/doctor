from django.db import models
# Create your models here.
from dentist.models import doctor
from service.models import service

class Appoitment(models.Model):


    server = models.OneToOneField(service, verbose_name=("service"), on_delete=models.CASCADE,blank=True, null=True )
    doctor = models.OneToOneField(doctor, verbose_name=("doctor"), on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    appoitment_data = models.DateField()
    appoitment_time = models.TimeField()
    def __str__(self):
        return self.name

