from django import forms
from .models import modelcontact


class contactform(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' your name' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':' your email' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'message' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))

    class Meta:

        model = modelcontact
        fields = '__all__'
