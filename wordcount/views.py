from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')


#def mypage(request):
 #   return HttpResponse('<h4>MyPage</h4>')


def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist)})

def aboutus(request):
    return render(request,'aboutus.html')
