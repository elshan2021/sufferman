from django.shortcuts import render
from django.shortcuts import HttpResponse

# def about(request):
#     return HttpResponse('Hi There')
#
# def home(request):
#     return HttpResponse('Hi home')

def home(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'about.html')
