

from .models import Post
from django.forms.models import ModelForm
from django import forms
#글 등록에 사용할 폼클래스 - 모델 form클래스 상속
class PostForm(ModelForm):
    #사용자의 첨부파일이나 이미지 업로드를 위한 <input>태그
    #required = False -> 해당 <input>태그를 사용자가 필수로 입력하지않아도 되는 공간 설정
    #ClearableFileInput -> <input type=file> 형태의 입력공간에 추가 설정을 할때 사용되는 위젯
    #{'multiple':True} -> 하나의 입력공간에 여러개의 파일을 업로드할 수 있도록 설정
    files = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple':True}))
    images = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple':True}))
    
    class Meta:
        model = Post
        fields = ['type','headline','content']
        


#검색에 사용할 폼클래스 - 폼클래스 상속
class SearchForm(forms.Form):
    search_word = forms.CharField(max_length=200, label='검색어')
    
    
    