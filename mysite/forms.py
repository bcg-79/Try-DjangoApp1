from django import forms
from django.forms import widgets
from .models import ExpAccounts, ExpTransactions

class ExpAccountForm(forms.ModelForm):
    class Meta:
        model = ExpAccounts
        fields = ['acc_name', 'acc_type', 'initial_amount']

        widgets = {
            'acc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'acc_type': forms.Select(attrs={'class': 'form-control'}),
            'initial_amount': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
    def clean(self):
        data = self.cleaned_data

        return data

class ExpTransactionsForm(forms.ModelForm):
    class Meta:
        model = ExpTransactions
        fields = ['person_name', 'amount', 'category', 'add_spend', 'extra_note', ]

        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'amount': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'add_spend': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'extra_note': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': '3'} ),

        }
