from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'utilities/index.html')
#    return HttpResponse('This is a test')

