from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        "number1" : 123,
        "number2" : 321
    }
    return render(request,"test.html",context=context)
