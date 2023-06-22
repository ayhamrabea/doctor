from django import forms
from .models import Appoitment
from dentist.models import doctor
from service.models import service




class DateInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class appoitmentForm(forms.ModelForm):
    server = forms.ModelChoiceField(
        queryset=service.objects.all(),initial='FIXED',
        widget=forms.Select(attrs={'label':'What is your favorite fruit?','class':'form-control bg-light border-0' ,'style':'height: 55px'})
    )
    doctor = forms.ModelChoiceField(
        queryset=doctor.objects.all(),initial="FIXED",
        widget=forms.Select(attrs={'class':'form-control bg-light border-0' ,'style':'height: 55px'})
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter your email' , 'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    appoitment_data = forms.DateField(widget=DateInput(attrs={'class':'form-control bg-light border-0' ,'style':'height: 55px' }))
    appoitment_time = forms.TimeField(widget=TimePickerInput(attrs={'class':'form-control bg-light border-0' ,'style':'height: 55px' }))


    class Meta:
        model = Appoitment
        fields = '__all__'
        # widgets = {
        #             'appoitment_data': DateInput(),
        #         }
        
