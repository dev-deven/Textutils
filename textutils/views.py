#This is Created By :- Devendra Patil
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')



def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunctuation = request.GET.get('removepunctuation', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    lineremover =request.GET.get('lineremover' , 'off')
    charcount = request.GET.get('charcount' , 'off')
    capsall = request.GET.get('capsall', 'off')
    print(removepunctuation)
    print(djtext)
    analyzed = ""
    if (removepunctuation=='on'):

     punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
     for char in djtext:
        if char not in punctuation:
            analyzed = analyzed + char
     params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
     return render(request, 'analyze.html', params)
    elif(capsall=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(spaceremover=='on'):
        analyzed = ""
        for char in djtext:
            if char!=" ":
                analyzed = analyzed + char
        params = {'purpose': 'Remove Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (lineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (charcount == 'on'):
        analyzed = ""
        count=0
        for char in djtext:
         count=count+1
        analyzed = count
        params = {'purpose': 'Remove Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        analyzed = "ERROR YOU HAVE NOT ENTERD ANY TEXT ;)"
        params = {'analyzed_text': analyzed}
        return render(request, 'analyze.html',params)


def goback(request):
    return render(request, 'index.html')