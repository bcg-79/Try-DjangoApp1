from django.urls import path
from .views import all_transactions, home, expaccounts, set_default_acc

app_name = 'mysite'
urlpatterns = [
    path('home/', home, name='home'),
    path('expaccounts/', expaccounts, name='expaccounts'),
    path('setDefaultAcc', set_default_acc, name='setDefaultAcc'),
    path('alltransaction/', all_transactions, name='alltransactions'),

]