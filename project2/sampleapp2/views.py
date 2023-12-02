from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')
def addtwo(request):
    num1=int(request.POST['fno'])
    num2 = int(request.POST['sno'])
    s=num1+num2
    return render(request,'home.html',{'result':s,'msg':"done"})