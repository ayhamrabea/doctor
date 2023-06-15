from django.db import models

# Create your models here.


class service(models.Model):
    
    titil = models.CharField(max_length=70)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    descreption = models.TextField(max_length=270)

    
    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.titil
