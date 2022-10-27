from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
     class Meta:
         model = Volunteer 
         fields = ['fname','lname','usrname','email','instiname','phone','passwd','cpasswd']
