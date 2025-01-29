from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'post':
        pass
    else:
        return render(request, 'register.html')
def login(request):
    return render(request,'login.html')
    