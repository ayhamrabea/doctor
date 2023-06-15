from django.db import models



group = (
    ('General Dentist','General Dentist'),
    ('Pedodontist ','Pedodontist '),
    ('Orthodontist.','Orthodontist.'),
    ('Periodontist ','Periodontist '),
    ('Endodontist ','Endodontist '),
    ('Oral Pathologist ','Oral Pathologist '),
) 

class doctor(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='doctors')
    specialist = models.CharField(max_length=60,choices=group)
    experiencce = models.IntegerField()
    about_me = models.TextField(max_length=250)
    add_at = models.DateField( auto_now_add=True)
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)

    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

    def __str__(self):
        return self.name
