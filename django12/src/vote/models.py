from django.db import models


#질문 저장
#질문 제목 생성일
class Question(models.Model):
    name = models.CharField('설문조사 제목',max_length=100)
    #날짜와 시간 데이터를 저장하는 클래스 -> DateTimeField 
    #날짜 정보만 저장 -> Date 필드
    date = models.DateTimeField('생성일')
    def __str__(self):
        return self.name        





#답변
#어떤 질문에 연결되었는가, 답변 내용 투표 수
class Choice(models.Model):
    name = models.CharField('답변항목',max_length=50)
    #IntegerFiedl: 정수 값을 저장하는 공간
    votes = models.IntegerField('투표수',default=0)
    
    #ForeignKey(연결할 모델클래스) : ForeginKey 객체를 만든 클래스의 객체들이 연결한 모델클래스의 객체와 연결할 수 있는 설정
    q = models.ForeignKey(Question, on_delete=models.CASCADE) #->Question 이 1 내가(Choice) n의 연결 -> 하나의 Question 객체에 여러개의 Choice 객체 연결
    #on_delete=models.CASCADE -> Question 객체를 지우면 연결된 모든 Choice 객체 삭제
    def __str__(self):
        return self.q.name + "/" + self.name # 객체가 보이는 형식을 질문 / 답변의 형태로 변경
    
    
    class Meta: #모델클래스에 정의된 변수들을 처리할 때 사용하는 클래스
        verbose_name = '답변항목' # admin 페이지의 Choice의 이름이 답변항목으로 바뀜
        ordering = ['q'] # -> Question 메소드와 연결된 것 끼리 집합