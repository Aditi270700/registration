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
    print(request.method)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Student.objects.filter(email=email)
        print(user)
        if user:
            data=Student.objects.get(email=email)
            user_data={
                'name':data.name,
                'email':data.email,
                'detail':data.detail,
                'phone':data.phone,
                'password':data.password,
                'subscribe':data.subscribe,
                'dob':data.dob,
                'gender':data.gender,
                'profile_pic':data.profile_pic,
                'resume':data.resume
            }
            print(user_data)
            # print(data.name)
            # print(data.email)
            # print(data.detail)
            # print(data.phone)
            # print(data.password)
            # print(data.subscribe)
            # print(data.dob)
            # print(data.gender)
            # print(data.profile_pic)
            # print(data.resume)
            pass1 = data.password
            if pass1 == password:
                return render(request, 'dashboard.html',{'name':data.name,'email':data.email,'data':user_data})
            else:
                msg = "Email and password not match"
                return render(request, 'login.html',{'msg':msg,'oldemail':email})
        else:
            msg = "Email id not exist"
            return render(request,'login.html',{'msg':msg})  
    else:
        return render(request,'login.html')
    
    