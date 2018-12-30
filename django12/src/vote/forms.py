'''
Created on 2018. 12. 22.

@author: user
'''



#form : HTML 코드에서 사용할 입력양식 <form>,<input>을 모델클래스에 맞게 자동으로 만드는 기능
#class 클래스명(ModelForm 또는 Form):
#ModelForm : 모델클래스를 기반으로 입력양식을 자동 생성할 때 상속받는 클래스
#Form : 커스텀 입력양식을 생성할 때 상속받는 클래스

#폼 클래스의 객체를 함수를 통해 HTML문서의 입력양식으로 변화(<p>,<table>,<li>)

# 1) ModelForm 클래스 임포트 2) 사용하고자하는 모델 클래스 임포트 3) ModelForm을 상속받는 폼클래스를 정의

#어플리케이션을 제작하는 순서
#기존) 어플리케이션 생성 -> setting.py 등록 -> 모델 정의 -> 데이터베이스 반영(migrate) -> 뷰 정의 -> 템플릿 정의 -> url 정의
#변경) 어플리케이션 생성 -> setting.py 등록 -> 모델 정의 -> 폼 클래스 정의 -> 데이터베이스 반영(migrate) -> 뷰 정의 -> 템플릿 정의 -> url 정의

from django.forms.models import ModelForm
from .models import Question, Choice

#Question 모델 클래스와 연동된 모델폼 클래스 정의

class QuestionForm(ModelForm): #QuestionForm은 ModelForm 클래스를 상속받는다
    class Meta: #모델클래스에 대한 정보를 정의하는 클래스
        #model : 어떤 모델 클래스와 연동할지 저장하는 변수
        #fields :모델클래스에 정의된 변수 중 어떤 변수를 클라이언트가 작성할 수 있도록 입력양식으로 만들 것인지 지정하는 변수(iterable type) iterable type은 list나 튜플과 같은 타입 -> 객체의 변수 중 사용자가 직접 입력할 수 있는 부분
        #exclude :  모델클래스에 정의된 변수 중 입력양식으로 만들지 않을 것을 지정하는 변수
        #fields, exclude 변수 중 한개만 사용
        #ex) 게시판을 만들 시 사용자가 입력해야할 것 -> 제목, 내용, 첨부파일 -> fields
        #    실제로 보여지는 양식 -> 제목, 내용, 첨부파일, 글번호, 글쓴이 등등  -> 글번호와 글쓴이는 수정 xx -> excludes
        model = Question
        fields = ['name']
        # exclude = ['date']
        
#Choice 모델클래스와 연동된 모델폼 클래스 정의
class ChoiceForm(ModelForm):
    def __init__(self, *args, **kwarg):#'q'변수의 label 변경(변경 전 -> Q:)을 위한 생성자 호출
        super().__init__(*args, **kwarg)
        self.fields['q'].label = '질문지'
        
    class Meta:
        model = Choice
        fields = ['q','name']
        

