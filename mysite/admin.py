from django.contrib import admin
from .models import ExpAccounts, ExpTransactions

admin.site.register(ExpAccounts)
admin.site.register(ExpTransactions)