
from django import forms

from core.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
          model = Contact
          fields = '__all__'
          widgets = {
               'Fname': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control' , 'placeholder': "Full Name" }),
               'email': forms.EmailInput(attrs={'class':'col-md-4' 'form-group' 'form-control' , 'placeholder':"Email Address" }),
               'phone': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control' , 'placeholder':"Phone Number" }),
               'message': forms.Textarea(attrs={'class':'col-md-12' 'form-group' 'form-control' , 'rows': 4, 'placeholder':"Write Message" }),
                                         
               }