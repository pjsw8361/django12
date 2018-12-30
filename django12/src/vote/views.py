from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login

#HTML 문서를 넘겨주는 것이 아닌 리다이렉트 주소를 넘겨줄 때 HttpResponseRedirect 클래스의 객체를 반환하면 됨
#HttpResponseRedirect(사용자가 넘겨줄 주소(문자열))

#reverse: 템플릿의 url 태그와 동일한 기능을 수행, 별칭을 기반으로 URL 검색
#reverse: 등록된 별칭(문자열), args=(매개변수에 넘겨줄 값,))
#HttpResponseRedirect( reverse() )

#index(질문 리스트)
def index(request):
    #Question 객체를 추출
    a=Question.objects.all()
    #HTML문서에 객체 리스트 전달 후 클라이언트에게 HTML 파일 전송
    return render(request, 'vote/index.html',{'a':a})

 
#detail(질문 선택 시 답변 항목 제공)
def detail(request, qid):
    #get_object_or_404(모델클래스, 조건) : 해당 모델 클래스에서 조건에 맞는 객체 한개를 출력
    #조건에 맞는 객체가 없을 경우 404에러를 띄우는 처리를 해줌
    b = get_object_or_404(Question, id=qid)
    return render(request, 'vote/detail.html',{'q':b})


#vote(웹 클라이언트 요청에 따라 투표 적용)
def vote(request):
    #POST방식으로 사용자가 요청했는지 확인
    #request.method : 사용자의 요청방식이 문자열 형태로 저장된 변수
    if request.method == "POST":
        #request.POST:post 방식으로 요청하면서 넘어온 데이터(사전형)
        #request.POST.get(키값):post방식으로 넘어온 데이터 중 입력한 키 값과 동일한 데이터를 추출
        c_id = request.POST.get('b') 
        c = get_object_or_404(Choice, id = c_id)
        c.votes += 1 #투표 수 증가
        c.save() #변동사항을 데이터베이스에 반영
        
        #vote application의 index뷰로 이동 가능,utl 주소를 넘겨줌 
        #c.q -> choice 객체 c에 저장된 q를 접근 , c와 연결된 Question 객체 자체를 의미
        #c.q.id -> choice 객체 c와 연결된 Question 객체 자체의 id 변수 값
        return HttpResponseRedirect( reverse('vote:result', args=(c.q.id ,) ) ) 



#result(투표 결과)
def result(request, q_id):
    
    return render(request, 'vote/result.html',{'q':get_object_or_404(Question,id = q_id)})


from .forms import QuestionForm, ChoiceForm
from _datetime import datetime #현재 날짜/시간을 불러오는 파이썬 내장 함수
from django.contrib.auth.decorators import login_required
#데코레이터: URL 요청에 따라 뷰함수를 호출할 때, 호출 전에 데코레이터가 먼저 실행되서 초기화작업, 로그인확인, 접근권한 확인을 수행하는 기능
#함수에 데코레이터 붙이기
#@데코레이터 함수 이름 ~~~~


#클래스에 데코레이터 붙이기
#class Class(사용할 데코레이터 클래스명):

#login_required : 뷰 함수 호출 전 요청을 한 클라이언트가 로그인을 했는지 여부를 파악하고 비 로그인 상태인 경우 로그인 페이지를 띄워주는 데코레이터 함수
#Question 객체를 사용자가 등록하는 뷰
@login_required
def qregister(request):
    #GET 방식
    if request.method == "GET":
        form = QuestionForm()  #모델 폼 클래스 객체 생성
        #모델 폼클래스 객체 생성 시 매개변수에 값을 전달하지 않는 경우, 입력 양식에 값이 비어있는 형태로 객체가 생성됨
        return render(request, 'vote/qregister.html', {'f' : form}) #HTML 파일 전달
    
    
         
    #사용자 요청 정보를 받아 데이터베이스에 저장
    #POST 방식
    elif request.method == "POST":
        #request.POST -> 사용자가 post 방식으로 요청했을 때 같이 넘어온 데이터 집합(사전형)
        print(request.POST)
        form = QuestionForm(request.POST) #사용자 입력을 해당 폼 객체 생성 시 넣어줌 
        if form.is_valid(): #사용자가 입력한 값이 유효한 값인지 확인 -> 글자수 초과, 중복 등등을 확인해줌
            #폼객체.cleaned_data : is_valid()함수로 유효한 값인지 확인 후 Trun 값을 반환했을때 사용자의 입력정보를 확인할 수 있는 사전형 변수
            #폼객체.save(): 모델 폼 클래스의 객체만 사용가능, 연동된 모델클래스의 객체로 변환 후 데이터베이스에 저장
            #폼객체.save(commit=False): 연동된 모델클래스의 객체로 변환만 해줌
            
            #Question 객체는 date 변수의 값이 비어있으면 안되므로 파이썬 코드로  date변수 값을 채운 후 db에 저장 해야함
            q = form.save(commit=False) #q: Form에 저장된 값을 바탕으로 생선된 Question 객체
            print('생성된 question 객체', q)
            q.date = datetime.now()#파이썬 모듈을 이용하여 현재 생성된 시간을 date변수에 저장
            q.save() # 해당 Question 객체를 데이터베이스에 저장함    
            
            return HttpResponseRedirect(reverse('vote:index'))
             
        
    
    
    
#Choice 객체를 사용자가 등록하는 뷰
@login_required
def cregister(request):
    if request.method == "GET":
        return render(request, 'vote/cregister.html',{'f':ChoiceForm()}) #변수 저장 없이 바로 객체를 넘기는 것도 가능
    elif request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            c = form.save() #수정할 변수가 없기에 commit 사용을 안함, vote는 default가 0으로 되어있다.!!!
            print(c)
            return HttpResponseRedirect( reverse('vote:detail', args=(c.q.id, )))
        else: #사용자가 입력한 값이 유효한 값이 아닌 경우 
            return render(request, 'vote/cregister',{'f':form, 'error':'유요하지 않은 값입니다.'}) #사용자가 입력한 데이터를 바탕으로 생성된 form 객체와 error 변수를 HTML 파일에 전달
        
            
        
    




#Question 객체의 데이터를 사용자가 수정하는 뷰
@login_required
def qupdate(request, q_id):
    obj = get_object_or_404(Question, id=q_id)
    if request.method == "GET":
        #데이터 베이스에 저장된 Question 객체의 정보를 기반으로 모델폼 객체를 생성
        #HTML로 변환 시 빈칸이 아닌 값이 채워진 형태로 변환됨
        form = QuestionForm(instance = obj)
        return render(request, "vote/qupdate.html",{'f':form})
    
    elif request.method == "POST":  
        form = QuestionForm(data = request.POST, instance = obj) #기존 객체에 저장된 변수값을 사용자의 입력 데이터로 변경한 모델폼 객체를 생성
        if form.is_valid(): #수정한 값이 유효한 값인지 확인
            q = form.save() #사용자가 입력한 데이터를 바탕으로 데이터베이스에 수정사항을 반영
            print('obj: ', obj)
            print('q: ', q) 
            return HttpResponseRedirect(reverse('vote:index'))
        
            
            

#Choice 객체를 사용자가 수정하는 뷰
@login_required
def cupdate(request, c_id):
    c = get_object_or_404(Choice, id=c_id)
    if request.method == "GET":
        form = ChoiceForm(instance = c)
        return render(request, 'vote/cupdate.html', {'f':form})
    
    elif request.method == "POST":
        form = ChoiceForm(data = request.POST, instance = c)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vote:detail', args=(c.q.id, )))
        else:
            pass
        
    

#Question 객체 삭제요청 처리 뷰
@login_required
def qdelete(request, q_id):
    q = get_object_or_404(Question, id=q_id) #삭제할 객체를 찾기
    q.delete()#해당 객체를 데이터베이스에서 삭제함. 삭제한 객체에 저장된 변수값은 사용할 수 있음
    return HttpResponseRedirect(reverse('vote:index'))


#Choice 객체 삭제요청 처리 뷰
#매개변수를 추가(삭제하고자하는 Choice 객체의 id 값) -> 매개변수를 바탕으로 Choice 객체 찾기 -> 객체 삭제 ->index or detail의 url을 전달 -> urls.py에 등록
@login_required
def cdelete(request, c_id):
    c = get_object_or_404(Choice, id=c_id)
    c.delete()
    return HttpResponseRedirect(reverse('vote:detail', args=(c.q.id ,) ))

