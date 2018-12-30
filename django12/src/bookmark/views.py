from django.shortcuts import render

#View : �궗�슜�옄�쓽 �슂泥��뿉 �뵲�씪 �뜲�씠�꽣瑜� 泥섎━�븯怨� HTML 臾몄꽌�굹 �깉濡쒖슫 URL 二쇱냼瑜� �쟾�넚�븯�뒗 �뿭�븷

#View : �겢�옒�뒪/�븿�닔 �삎�깭濡� �젙�쓽

#�븿�닔 �삎�깭濡� �젙�쓽 �떆 泥ル쾲吏� 留ㅺ컻蹂��닔瑜� request濡� �젙�쓽�빐�빞�븿
#request : �궗�슜�옄�쓽 �슂泥� �젙蹂�, <form>�쑝濡� �꽆寃⑥� �뜲�씠�꽣, 濡쒓렇�씤�젙蹂�, �꽭�뀡�젙蹂�, �슂泥�諛⑹떇(GET,POST)

#HTML �뙆�씪�쓣 �쟾�넚�븯�뒗 硫붿씤�럹�씠吏�
def index(request):
    #render(request, HTML臾몄꽌�쓽 寃쎈줈, HTML臾몄꽌�뿉 �쟾�떖�븷 媛�(�궗�쟾�삎) )
    return render(request, 'bookmark/index.html', {'a': 'Bye', 'b' : [1,2,3,4,'asdf'] } )

#紐⑤뜽�겢�옒�뒪�뿉 ���옣�맂 媛앹껜�뱾�쓣 異붿텧�븯湲� �쐞�빐�꽌 紐⑤뜽�겢�옒�뒪 �엫�룷�듃
from .models import Bookmark
#from bookmark.models import Bookmark 

#Bookmark 紐⑤뜽�겢�옒�뒪�쓽 媛앹껜瑜� 異붿텧�빐 HTML�뙆�씪�쓣 �닔�젙�븯�뒗 �럹�씠吏�
def booklist(request):
    #紐⑤뜽�겢�옒�뒪紐�.objects.all() : �뜲�씠�꽣踰좎씠�뒪�뿉 �빐�떦 紐⑤뜽�겢�옒�뒪濡� ���옣�맂 紐⑤뱺 媛앹껜瑜� 由ъ뒪�듃�삎�깭濡� 異붿텧
    #紐⑤뜽�겢�옒�뒪紐�.objects.get() : �뜲�씠�꽣踰좎씠�뒪�뿉 �빐�떦 紐⑤뜽�겢�옒�뒪濡� ���옣�맂 媛앹껜以� �븳媛쒕�� 異붿텧
    #紐⑤뜽�겢�옒�뒪紐�.objects.filter() : �뜲�씠�꽣踰좎씠�뒪�뿉 �듅�젙議곌굔�쓣 留뚯”�븯�뒗 媛앹껜�뱾�쓣 由ъ뒪�듃�삎�깭濡� 異붿텧
    #                 .exclude() : �뜲�씠�꽣踰좎씠�뒪�뿉 �듅�젙議곌굔�쓣 留뚯”�븯吏� �븡�뒗 媛쒖껜�뱾�쓣 由ъ뒪�듃�삎�깭濡� 異붿텧
    
    #�뜲�씠�꽣踰좎씠�뒪�뿉 ���옣�맂 Bookmark 媛앹껜�뱾�쓣 紐⑤몢 異붿텧�빐 由ъ뒪�듃�삎�깭濡� 諛섑솚
    objs = Bookmark.objects.all() 
    print(objs)
    
    return render(request, 'bookmark/booklist.html', {'objs' : objs })
#Bookmark 媛앹껜 以� �븯�굹�쓽 �뜲�씠�꽣留� 異붿텧�븯�뒗 �럹�씠吏�

#사용자가 선택한 객체를 구분하기위해서 새로운 매개변수 사용
#request를 제외한 매개변수는 URL등록 시 특정부분을 매개변수에 전달하는 처리를 해줘야함
def bookdetail(request, bookid):
    #데이터베이스에 저장된 bookmark 객체 중 사용자가 요청한 객체를 추출
    #추출한 객체와 HTML문서를 client에게 전달
    #get -> 조건에 맞는 객체 한개를 가져옴
    #조건에 맞는 객체가 여러개인 경우 -> 에러
    #조건에 맞는 객체가 없는 경우 -> 에러
    obj = Bookmark.objects.get(id=bookid)
    #추출한 객체와 HTML문서를 클라이언트에게 전달
    

    return render(request, 'bookmark/bookdetail.html',{'obj':obj})


