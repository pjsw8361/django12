from django.db import models
# 모델 : 만들고자하는 어플리케이션에서 사용하는 데이터들을 어떤식으로 저장할지 정의하는 부분
# 데이터베이스에 데이터를 저장할때, 저장할 데이터의 종류/이름을 클래스의 변수/객체로 정의할 수 있음

#1)모델 클래스 정의 시, models.Model 클래스 상속받아 모델클래스를 정의
#2)생성한 모델 클래스를 이용해 makemigrations 명령을 수행 (마이그레이션폴더에 파이썬파일이 생성)
#3)migrate 명령을 통해 데이터베이스에 실질적인 저장공간이 생성
#요약) 모델클래스 정의->makemigrations->migrate

#class 클래스이름(models.Model):

#북마크를 저장할 모델 클래스
#이름, URL주소 저장
class Bookmark(models.Model):
    #해당 모델클래스에 저장할 값을 정의할 때, 클래스 내의 변수를 정의
    #변수에 models.XXXField 클래스의 객체를 저장하는 것으로 정의할 수 있음
    #CharField : 글자수 제한이 있는 문자열을 저장하는 공간을 정의
    #max_length(필수) : 최대로 저장할수있는 글자수
    name = models.CharField(max_length=200)
    #URLField : 인터넷 주소(URL)를 정장하는 공간을 정의 
    url = models.URLField()
    #__str__ : 객체를 출력할 때 (print(객체)) 표현방식을 처리하는 파이썬 함수
    #Model 클래스에 구현된 __str__ 함수를 오버라이딩 해서 사용
    #함수를 추가/오버라이딩을 하는 작업은 makemigrations/migrate를 할 필요가 없음
    def __str__(self):
        return self.name










