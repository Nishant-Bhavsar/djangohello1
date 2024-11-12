from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello world. This is Home")

def about(request):
    return render(request, "pages/about.html")