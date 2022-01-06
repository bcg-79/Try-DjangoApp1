from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm, UserLoginForm

def login_views(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('mysite:home'))
        else:
            messages.add_message(request, messages.INFO, 'Username or Password is Incorrect...')

    data = {'form': form}
    return render(request, 'accounts/pages/login.html', data)

def register(request):
    form = UserRegisterForm(request.POST or None)
    data = {}

    if form.is_valid():
        u_name = form.cleaned_data['username']
        f_name = form.cleaned_data['first_name']
        l_name = form.cleaned_data['last_name']
        e_mail = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = User.objects.create_user(username=u_name, first_name=f_name, last_name=l_name, email=e_mail, password=password)
        user.save()

        messages.add_message(request, messages.INFO, 'User Created Successfully')
        form = UserRegisterForm()

    data['form'] = form
    return render(request, 'accounts/pages/register.html', data)


def logout_user(request):
    logout(request)

    return redirect(reverse('accounts:login'))



