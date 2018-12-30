from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


#제네릭뷰 : 장고에서 제공하는 여러가지 뷰 기능을 수행하는 클래스
#뷰 클래스 구현 시 제네릭뷰를 상속받아 변수/메서드를 수정해 그 기능을 사용할 수 있음
#제네릭뷰를 사용할 때는 문서를 확인하여 어떤 변수/메서드를 수정할 수 있는지 파악해야함

#ListView: 특정 모델클래스의 객체의 목록을 다루는 기능을 수행하는 제네릭뷰
#게시물 목록(index)
class Index(ListView):
    template_name = 'blog/index.html' #HTML 파일의 경로를 저장하는 변수
    model = Post # 목록으로 보여질 model 클래스를 지정하는 변수
    context_object_name = 'post_list' #템플릿에게 객체리스트를 넘겨줄 때 사용할 키 값
    paginate_by = 5 #한 페이지당 보여지는 객체의 개수
    

#DetailView: 특정 모델클래스의 객체 한개를 템플릿에 전달할 때 사용하는 제네릭뷰
#상세페이지(detail)
class Detail(DetailView):
    template_name = 'blog/detail.html'
    model = Post
    context_object_name= 'obj'

#FormView:폼클래스를 객체로 생성해 템플릿으로 넘겨주는 뷰
#글 등록 페이지(postRegister)
from .forms import *
class PostRegister(LoginRequiredMixin ,FormView): #함수가 아니고 class이므로 decorator가 아닌 LoginRequiredMixin을 사용
    template_name = 'blog/postregister.html'
    form_class = PostForm
    context_object_name = 'form'

    #is_valid()함수가 True를 반환하였을 때에 대한 처리를 form_valid()함수를 오버라이딩해서 구현
    def form_valid(self, form):
        #사용자 입력에 대한 객체 생성 처리
        obj = form.save(commit=False) #author변수에 값이 x
        obj.author = self.request.user #뷰함수의 request 매개변수를 뷰클래스에서 사용할 때 self.request로 사용가능
        #request.user : 요청한 클라이언트의 로그인 정보(User 모델 클래스의 객체), #글쓴이 정보 채우기
        obj.save() #데이터베이스에 Post 객체 저장
        
        #사용자가 업로드한 이미지, 파일을 데이터베이스에 저장
        for f in self.request.FILES.getlist('images'): #request.FILES : 클라이언트가 서버로 보낸 파일정보를 관리하는 변수
            # f -> 이미지 정보, f를 이용하여 PostImage 객체를 생성, DB에 저장한다
            image = PostImage(post = obj, image = f) #객체 생성시 각 변수에 값을 채워서 생성할 수 있음
            #image = PostImage()
            #image.post = obj
            #imgae.image = f
            #위 3줄과 같은 의미
            image.save()
        
        for f in self.request.FILES.getlist('files'):
            file = PostFile(post = obj, file = f)
            file.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(obj.id,)) ) #만들어진 Post 객체의 id 값을 detail 뷰에 넘겨주면서 마무리
    
#검색 기능을 구현한 뷰클래스(searchP)
class SearchP(FormView):
    template_name = 'blog/searchP.html'
    form_class = SearchForm
    context_object_name = 'form'
    
    #유효성 검사를 통과한 요청들을 처리하기 위해 form_valid 함수 오버라이딩으로 구현
    def form_valid(self, form):
        #Post 객체중에 사용자가 입력한 텍스틀르 포함한 객체를 찾아 HTML 결과로 보여주기
        search_word = form.cleaned_data['search_word'] #사용자가 입력한 텍스트 추출
        #Post.object.filter(변수__필터링=값) -> 변수와 값을 필터링 조건에 맞춰서 비교 후 만족하는 객체를 추출하는 함수
        #contains -> 필터링, 해당 변수가 우변의 값을 포함한 경우를 추출
        
        post_list = Post.objects.filter(headline__contains=search_word)#추출된 텍스트를 포함한 Post 객체들을 추출(제목 검색)
        #추출된 결과를 HTML로 전달(검색결과 + 재 검색결과 + 검색어)
        return render(self.request, self.template_name, {'form':form, 'search_word':search_word, 'postlist':post_list})
    