app_name='blog'
from django.urls import path
from .views import *
urlpatterns = [
    path('', Index.as_view(), name = 'index'), #view에서 클래스 호출방법
    path('<int:pk>', Detail.as_view(), name ='detail'),
    path('postP/', PostRegister.as_view(), name='postP'),
    path('search', SearchP.as_view(), name = 'searchP')
    ]