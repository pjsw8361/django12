'''
Created on 2018. 12. 23.

@author: user
'''



from django.urls import path
from .views import *

app_name = 'login'

urlpatterns =[
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    ]

