
# from django import forms
# from user.models import User

# from django.contrib.auth import get_user_model


# User = get_user_model()


# class UserRegisterForm(forms.ModelForm):
#      password = forms.CharField(widget=forms.PasswordInput)
#      password2 = forms.CharField(widget=forms.PasswordInput, label= 'Confirm Password')

#     # confirm_password = forms.CharField(widget=forms.PasswordInput)

#      class Meta:
#         model = User
#         # fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password',)
#         fields = ('first_name', 'last_name', 'username', 'email',  'password', 'password2', 'address', 'image')
#         widgets = {
#                 'username': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control' }),
#                'first_name': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control' }),
#                'last_name': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control' }),
#                'email': forms.EmailInput(attrs={'class':'col-md-4' 'form-group' 'form-control' }),
#                'address': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control' }),
#             #    'phone': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control' }),
#                'password': forms.PasswordInput(attrs={'class':'col-md-4' 'form-group' 'form-control'}),
#                'password2': forms.PasswordInput(attrs={'class':'col-md-4' 'form-group' 'form-control'}),
                                         
#                }
        
#      def __init__(self, *args, **kwargs):
#             super(UserRegisterForm, self).__init__(*args, **kwargs)
#             self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', })
#             self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', })


     
#      def clean_password2(self):

#         cd = self.cleaned_data

#         print("gdhdhdjdj", self.cleaned_data)
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']
    

# #      def clean_username(self):
# #             username = self.cleaned_data.get('username')
# #             if User.objects.filter(username=username).exists():
# #                  raise forms.ValidationError('Username already exists')
# #             return username
            




# #      def clean_email(self):
# #             email = self.cleaned_data.get('email')
# #             if User.objects.filter(email=email).exists():
# #                  raise forms.ValidationError('Email already exists')
# #             return email

    
# #      def clean_password(self):
# #             password = self.cleaned_data.get('password')
# #             if len(password) < 1:
# #                  raise forms.ValidationError('Password must be at least 8 characters')




# class UserLoginForm(forms.Form):
#     username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
#     password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
      


from django import forms
from user.models import User

from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterForm(forms.ModelForm):
     
     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'email-bt', 'placeholder':"Confirm Password"}), label= 'Confirm Password')

    # confirm_password = forms.CharField(widget=forms.PasswordInput)

     class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password',)
        fields = ('first_name', 'last_name', 'username', 'email',  'password', 'confirm_password', 'address', 'image')
        widgets = {
               'username': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control', 'placeholder':"Username" }),
               'first_name': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control', 'placeholder':"First Name" }),
               'last_name': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control', 'placeholder':"Last Name"}),
               'email': forms.EmailInput(attrs={'class':'col-md-4' 'form-group' 'form-control', 'placeholder':"Email" }),
               'address': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control', 'placeholder':"Adress" }),
            #    'phone': forms.TextInput(attrs={'class':'col-md-4' 'form-group' 'form-control' }),
               'password': forms.PasswordInput(attrs={'class':'col-md-4' 'form-group' 'form-control', 'placeholder':"Password"}),
               # 'password2': forms.PasswordInput(attrs={'class':'col-md-4' 'form-group' 'form-control'}),
                                         
               }


     def clean(self):

            cleaned_data = super(UserRegisterForm, self).clean()

            password = cleaned_data.get("password")

            confirm_password = cleaned_data.get("confirm_password")


            if password != confirm_password:

                raise forms.ValidationError(

                    "password and confirm password does not match"

                )








class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
      






















    