from django.shortcuts import render
from .models import *
# Create your views here.



# with out models:
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contactus.html')
def adventure(request):
    return render(request,'adventure.html')


# with  models:
def carni(request):
    a=cat.objects.all()
    b=bird.objects.all()
    c=snake.objects.all()
    return render(request,'carni.html',context={'data1':a,'data2':b,'data3':c})


def omni(request):
    d=bear.objects.all()
    e=chicken.objects.all()
    f=turtle.objects.all()
    return render(request,'omni.html',context={'d':d,'e':e,'f':f})




