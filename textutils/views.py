from django.http import HttpResponse
from django.shortcuts import render
import string 

def remove_punctuations(input_string):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string

def index(request):
    return render(request,'index.html')
    # params={'name':'Bhavya',
    #         'city': 'Alwar'}
    # return HttpResponse("<h1>hello</h1>")

def analyze(request):
    djtext=request.POST.get('text','Nothing to show Input string was empty')
    removepunc=request.POST.get('removepunc')
    removespace=request.POST.get('removespace')
    countchar=request.POST.get('charcounter')
    upper=request.POST.get('uppercase')
    lower=request.POST.get('lowercase')
    if countchar:
        count=0
        for i in djtext:
            count=count+1
        return HttpResponse(f'''Number of characters are: {count}.
                            Click <a href="/">Here</a> to go back.''')
    if removepunc:
        djtext=remove_punctuations(djtext)
    if removespace:
        djtext=djtext.replace(" ","")
    if upper:
        djtext=djtext.upper()
    if lower:
        djtext=djtext.lower()

    return render (request,'analyze.html',{'analyzed_text':djtext})
    

def charcount(request):
    return HttpResponse("character counter <a href='/'>Click to Go back <a/>")

def removespace(request):
    return HttpResponse("space remover")