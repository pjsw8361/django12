from django.db import models

#카테고리
class PostType(models.Model):
    name = models.CharField('카테고리', max_length=20) #볗칭은 카테고리, 길이는 20
    def __str__(self):
        return self.name

from django.conf import settings
#글(제목, 글쓴이-외래키(User 클래스와 연동), 글내용, 작성일, 카테고리-외래키)
class Post(models.Model):
    type = models.ForeignKey(PostType, on_delete=models.PROTECT) 
    #models.PROTECT: 연결된 객체가 삭제되는 것을 막아주는 기능 -> PostType을 지우려면 연결된 Post를 먼저 삭제해야한다.!!
    #models.SET_NULL: 연결된 객체가 삭제되면 null값을 저장
    #models.SET_DEFAULT: 연결된 객체가 삭제되면 기본설정된 객체와 연결
    #models.SET(연결할 객체): 연결된 객체가 삭제되면 매개변수로 지정된 객체연결
    #models.CASCADE:연결된 객체가 삭제되면 같이 삭제됨
    headline = models.CharField('제목', max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.TextField('내용', null = True, blank=True) 
    #text field=글자 수 제한이 없는 문자열 공간
    #null -> 데이터 베이스에 객체를 저장할 때 해당 변수 값이 비어있어도 생성되도록 형성
    #blank -> 폼객체.is_valid, 폼객체.as+_p를 사용하였을 때 사용자가 입럭하지 않아도 되도록 허용
    pub_date = models.DateTimeField('작성일',auto_now_add = True) #auto_now_date: 객체가 생성될 때 현재 서버의 시간을 저장하도록 설정
    class Meta:
        ordering = ['-id']
#이미지(글-외래키, 이미지 파일)
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    image = models.ImageField('이미지 파일', upload_to = 'image/%Y/%m/%d')
    #ImageField: 이미지가 저장된 경로를 저장하는 공간
    #upload_to : 실제 이미지가 저장할 때 사용경로
    #% Y 현재 서버의 년도, %m 현재서버의 월, %d 현재 서버의 일
    
    def delete(self, using=None, keep_parents=False): #객체 삭제 시 호출되는 함수, 객체 삭제 전 실제 이미지 파일을 삭제하는 코드를 삽입
        #image 변수에 저장되어있는 경로의 파일을 지우는 과정
        self.image.delete()#첨부파일까지 삭제
        return models.Model.delete(self, using=using, keep_parents = keep_parents)

#파일(글-외래키, 파일)
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    file = models.FileField('첨부명',upload_to = 'files/%Y/%m/%d')
    #fileField 파일의 경로를 저장하는 겅간
    
    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        return models.Model.delete(self, using=using, keep_parents = keep_parents)
        
    
                    