'''
Created on 2018. 12. 23.

@author: user
'''

from django.forms import ModelForm
from django.contrib.auth.models import User #djagno.contrib.auth 어플리케이션의 models.py에서 User 모델 클래스를 임포트
#User 모델 클래스: django에서 제공하는 기본적인 회원 관리 클래스
from django import forms

#회원가입에 사용할 모델 폼 클래스
class SignupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password_check'].label = "패스워드 확인"
        
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())   #폼클래스에서 추가적인 input 태그를 만들 경우 forms.XXXField 객체를 변수에 저장
    
    field_order =['username','password','password_check','last_name','first_name','email'] #input 태그의 순서를 지정, 변수명으로 선언할 시 fields의 가장 마지막으로 간다. 그러나 password_check를 password 바로 뒤에 나오게하고 싶다.
    
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput()} #input 태그에 특정한 type을 지정할 때 사용하는 변수, 필드이름을 키값으로 쓰고 저장할 값을 forms.XXXInput클래스의 객체를 저장, password <input>태그에 비밀번호 type을 지정
        fields = ['username','password','last_name','first_name', 'email']
        
        
    
#로그인에 사용할 모델 폼 클래스
class SigninForm(ModelForm):
    class Meta:
        model=User
        widgets = {'password':forms.PasswordInput()}
        fields = ['username','password']