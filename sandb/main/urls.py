from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('account', HomePage.as_view(), name='home'), #write_note
]
