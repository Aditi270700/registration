from django.shortcuts import render

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
        
       
        pass
    else:
        return render(request, 'register.html')
def login(request):
    return render(request,'login.html')
    