# i have created this website
from django.http import HttpResponse
from django.shortcuts import render
# video6 code :
# def index(request):
#     return HttpResponse("<h1>This is you tube<h1> <a href ='https://www.youtube.com/'>Visit You tube.com !</a>")

def index(request):
    # variable={'name':'Django','place':'USA'}  this is the best way to add variable
    return render(request,'index.html')
def analyze(request):
    # get the text
    djtext=request.GET.get('text','default')
    print(djtext)
    # checkbox value
    removepunc=request.GET.get("removepunc","off")
    fullcaps=request.GET.get("fullcaps","off")
    newlineremover=request.GET.get("newlineremover","off")
    extraspaceremover=request.GET.get("extraspaceremover","off")
    print(removepunc)
    print(fullcaps)
    # print(djtext)
    # analyzed=djtext
    # check which chekckbox is on
    if removepunc=='on':
             punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
             analyzed=""
             for char in djtext:
                if char not in punctuations:
                 analyzed=analyzed+char
             params={'purpose':'Removed punctuations','analyzed_text':analyzed}
             djtext = analyzed

    # analyze the text
        # return HttpResponse("remove punc")
        #      return render(request,'analyze.html',params)
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
            params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
            djtext = analyzed

        # return render(request,'analyze.html',params)
    if newlineremover=='on':
        analyzed = ""
        for char in djtext:

            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose':'New line removed','analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)
    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate (djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Extra space rmoved', 'analyzed_text': analyzed}
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on') :
        return HttpResponse('Error')



    return render(request, 'analyze.html', params)

# def newlineremove(request):
#     return HttpResponse("remove new line")
# def charcount(request):
#     return HttpResponse("count char")
# def capitalizefirst(request):
#     return HttpResponse("capitalize first")
# def spaceremove(request):
#     return HttpResponse("space remover")