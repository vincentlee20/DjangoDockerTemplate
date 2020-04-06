from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'utilities/index.html')
#    return HttpResponse('This is a test')


def processed(request):
    return HttpResponse('This is processed function')

def process(request):
    if request.method == 'POST':
        Text=request.POST.get("text")
        Text= "Hello, " + Text.upper()
    return HttpResponse(Text)