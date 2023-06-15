from django import forms
from .models import Appoitment




class appoitmentForm(forms.ModelForm):

    server = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'choice a server' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    doctor = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'choice a doctor' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter your email' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    appoitment_data = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    appoitment_time = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control bg-light border-0' ,'style':'height: 55px' }))

    class Meta:
        model = Appoitment
        fields = '__all__'
