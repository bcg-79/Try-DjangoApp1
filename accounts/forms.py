from django.contrib.auth.models import User
from django import forms
from django.forms import widgets

class UserRegisterForm(forms.ModelForm):
    error_css_class = 'fw-lighter'
    required_css_class = 'required'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


    def clean(self):
        data = self.cleaned_data
        user = User.objects.filter(username__icontains=data.get("username"))

        if user:
            self.add_error('username', 'Username is already taken Please use different one..')

        return data

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            }

    def clean(self):
        data = self.cleaned_data
        # send a message to the user if anything is wrong
        return data


