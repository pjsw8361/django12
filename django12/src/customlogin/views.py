from django.shortcuts import render
from .forms import SigninForm, SignupForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

from django.contrib.auth.models import User

#회원가입
def signup(request):
    if request.method == "GET":
        return render(request, 'customlogin/signup.html',{'f':SignupForm()})
        
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid(): #id 중복, 형식, 비밀번호 형식 체크
            #form.save()는 비밀번호를 암호화하지 않은채로 데이터를 저장하기때문에 사용하면 안됨
            #User.object.create_user(아이디, 이메일, 비밀번호): 해당 비밀번호를 암호화한채로 회원생성, DB 저장 및 반환
           
            #비밀번호(password)와 비밀번호 확인(password_check)에 동일한 입력을 했는지 확ㅇ;ㄴ
            #form.cleaned_data['변수명'] -> 사용자가 입력한 데이터 추출
            if form.cleaned_data['password']  == form.cleaned_data['password_check']:            
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password']) #새로운 회원 생성 및 데이터 베이스에 저장
            #추가사항 입력 및 데이터베이스에 저장
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()
                
                return HttpResponseRedirect(reverse('vote:index'))
            
            else:
                return render(request, 'customlogin/signup.html',{'f':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})
            
        else:
            return render(request, 'customlogin/signup.html',{'f':form}) #is_valid()함수를 통과 못하면, User 모델 클래스에서 설정된 에러로 자동으로 넘겨짐
            

from django.contrib.auth import login, authenticate
#authenticate(아이디,비밀번호): 비밀번호를 암호화한 뒤, 아이디와 암호화된 비밀번호 모두 일치하는 user 객체를 추출
#login(request, User 객체): 해당 요청을 한 클라이언트가 User 정보를 기반으로 로그인 처리

#로그인
def signin(request):
    if request.method == "GET":
        return render(request, 'customlogin/signin.html', {'f':SigninForm(),'nexturl':request.GET.get('next','')})
    
    elif request.method == "POST":
        #아이디나 비밀번호가 일치하지않는 경우 사용자 입력을 넘겨줄 모뎀폼 객체를 미리 생성
        form = SigninForm(data=request.POST)
        
        #사용자 요청에 포함된 아이디와 비밀번호 값을 추출
        id = request.POST['username']
        pw = request.POST['password']
        #form.is_valid() -> username 중복체크를 해버려서 로그인을 수행할 수 없음(항상 FALSE)
        #아이디와 비밀번호가 동일한 User 객체 찾기
        #아이디와 비밀번호가 일치하지 않는 경우 none 값을 반환, 일치하는 경우 user 객체를 반환
        u = authenticate(username=id, password=pw) 
        #u 변수에 user 객체가 저장되어는지 확인
        if u: #아이디와 비밀번호가 일치하는 User 객체가 u 변수에 저장되어있는 경우
            #해당 요청을 한 클라이언트가 u에 저장된 User객체로 로그인
            login(request, user=u)
            nexturl = request.POST.get('nexturl')  #nexturl 데이터가 존재하는 경우 해당 url로 리다이렉트
            
            if nexturl:
                return HttpResponseRedirect( nexturl )
            else:
                return HttpResponseRedirect(reverse('vote:index'))
            
        else: #아이디와 비밀번호가 일치하지 않는 경우
            return render(request, 'customlogin/signin.html',{'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
        
        
        
        
from django.contrib.auth import logout        
#로그아웃
def signout(request):
    logout(request) #해당 요청을 한 클라이언트의 로그아웃(User 정보를 삭제)
    return HttpResponseRedirect(reverse("vote:index"))



