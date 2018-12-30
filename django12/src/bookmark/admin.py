from django.contrib import admin
#같은 폴더에 있는 models.py 접근해 정의된 모델클래스를 사용할 수 있도록 설정
from .models import Bookmark #같은폴더에 있는 models.py에 정의된 Bookmark클래스 임포트
#bookmark 폴더에 있는 models.py에 정의된 Bookmark 클래스 임포트
#from bookmark.models import Bookmark 

#해당 어플리케이션에서 정의된 모델클래스를 관리자 사이트에서 추가/수정/삭제/조회 하고싶은 경우
#해당 파이썬 파일에서 모델클래스를 등록하면 됨
# Register your models here.
#admin.site.register(모델클래스명) : 해당 모델클래스를 관리자 사이트에 등록
admin.site.register(Bookmark)
