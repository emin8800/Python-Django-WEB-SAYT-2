
# from django.shortcuts import render, redirect
# from user.models import *
# from user.forms import UserRegisterForm, UserLoginForm
# from django import forms
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout




# def register(request):
#     context = {
#         'title': 'Register',
#         'form' : UserRegisterForm()
#     }
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             return redirect('home')   
#     return render (request, 'register.html', context)
    
# def custom_authenticate(request, **credentials):
#     email = credentials.get('email')
#     password = credentials.get('password')
#     if email is None or password is None:
#         return None
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return None
#     # if user.check_password(password):
#     #     return user
#     # return None



# def login(request):
#     context = {
#         'title': 'Login',
#         'login': UserLoginForm()
#     }    
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         if User.objects.filter(username=username).exists():
#             user = authenticate(request, username=username, password=password)
#         elif User.objects.filter(email=email).exists():
#             user = custom_authenticate(request, email=email, password=password)
#         else:
#             raise forms.ValidationError('Username or Email does not exists')
#         if user is not None:
#             auth_login(request, user)
#             return redirect('home')
#         else:
#             context['form'] = UserLoginForm()
#             if username is None:
#                 context['error'] = 'Username in incorrect'
#             elif email is None:
#                 context['error'] = 'Email in incorrect'
#             elif password is None:
#                 context['error'] = 'Password in incorrect'

#     return render (request, 'login.html', context)

# def logout(request):
#     auth_logout(request)
#     return redirect('home')

# Create your views here.

# def register(request):
#     context = {
#         'title': 'Register',
#         'form' : UserRegisterForm()
#     }
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             password = form.cleaned_data.get('password')
#             password2 = form.cleaned_data.get('password2')
#             if password != password2:
#                 raise forms.ValidationError('Password and Confirm Password must be identical')
#             user = form.save()
#             user.set_password(user.password)
#             user.save()
#             return redirect('home')   
#         else:
#             context['form'] = form

#             return render (request, 'register.html', context)

   

from django.shortcuts import render, redirect
from user.models import *
from user.forms import UserRegisterForm, UserLoginForm
from django import forms
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout




def register(request):

    context = {

        'title': 'Register',

        'form': UserRegisterForm()

    }

    if request.method == 'POST':

        if request.POST['password'] != request.POST['confirm_password']:

            context['error'] = 'Passwords do not match'

            return render(request, 'register.html', context)

        else:

            form = UserRegisterForm(request.POST, request.FILES)

            if form.is_valid():

                user = form.save()

                user.set_password(user.password)

                user.save()

                return redirect('login')

    return render(request, 'register.html', context)

def login(request):

    context = {

        'title': 'Login',

        'form': UserLoginForm()



    }

    if request.method == 'POST':

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is not None:

            auth_login(request, user)

            return redirect('home')

        else:

            context['error'] = 'Username or password is incorrect'

    return render(request, 'login.html', context)



def logout(request):

    auth_logout(request)

    return redirect('home')