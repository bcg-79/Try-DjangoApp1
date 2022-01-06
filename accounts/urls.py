from django.urls import path
from django.urls.resolvers import URLPattern
from .views import login_views, logout_user, register

app_name = 'accounts'

urlpatterns = [
    path('login/', login_views, name='login'),
    path('register/', register, name='register'),
    path('logout_user/', logout_user, name="logout_user"),

]