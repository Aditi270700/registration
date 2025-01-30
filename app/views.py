from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        name=request.POST.get('username')
        email=request.POST.get('email')
        detail=request.POST.get('detail')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        subscribe=request.POST.getlist('subscribe')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        profile_pic=request.POST.get('profile-pic')
        resume=request.POST.get('resume')
        print(name,email,detail,phone,dob,subscribe,gender,password,cpassword,profile_pic,resume)
        user = Student.objects.filter(email=email)
        if user:
            x = "Email already exist"
            return render(request, 'register.html', {'msg': x})
        else:
            pass
        if password==cpassword:
            Student.objects.create(name=name,email=email,detail=detail,phone=phone,dob=dob,subscribe=subscribe,gender=gender,profile_pic=profile_pic,resume=resume,password=password)
            x = "Resgistration succesfully"
            return render(request,'login.html',{'msg':x})
        else:
            x = "password and cpassword not match"
            return render(request,'register.html',{'msg':x,'name':name,'email':email,'detail':detail,'phone':phone,'dob':dob,'subscribe':subscribe,'gender':gender,'profile_pic':profile_pic,'resume':resume,})
    else:
        return render(request, 'register.html')
def login(request):
    return render(request,'login.html')
    