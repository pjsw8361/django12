'''
Created on 2018. 12. 16.

@author: user
'''

from django.urls import path
from .views import  *



app_name =  'vote' # 하위#url 파일의 그룹이름
#path 함수를 이용하여 url1과 함수를 등록

#기본 주소가 
urlpatterns = [
    #127.0.0.1.:8000/vote 주소로 요청해야 vote의 인덱스 함수가 호출됨
     path('', index, name='index'),
     path('<int:qid>', detail, name='detail'),
     path('vote/', vote, name='vote'),
     path('result/<int:q_id>', result, name="result"),
     path('qr/',qregister, name='qregister'),
     path('qu/<int:q_id>', qupdate, name='qupdate'),
     path('qd/<int:q_id>', qdelete, name='qdelete'),
     path('cd/<int:c_id>', cdelete, name='cdelete'),
     path('cr/', cregister, name='cregister'),
     path('cu/<int:c_id>', cupdate, name='cupdate'),
    ]
                    