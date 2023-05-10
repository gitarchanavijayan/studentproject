from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from studentapps.models import add_course,add_student
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def logins(request):
    return render(request,'login.html')

@login_required(login_url='logins')
def addcourse(request):
    return render(request,'addco.html')

@login_required(login_url='logins')
def addstudent(request):
    return render(request,'addst.html')

@login_required(login_url='logins')
def showstudent(request):
    return render(request,'showst.html')

def signfun(request):
    if request .method=='POST':
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        u_name=request.POST['uname']
        e_mail=request.POST['mail']
        p_wd=request.POST['pwd']
        cnpwd=request.POST['cpwd']
        if p_wd==cnpwd:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,'This username is already exist')
                return redirect('signup')
            else:
                user_name=User.objects.create_user(
                    first_name=f_name,
                    last_name=l_name,
                    username=u_name,
                    email=e_mail,
                    password=p_wd
                )
                user_name.save()
        else:
             messages.info(request,'password does not match')
             return redirect('signup')
        return redirect('logins')
    else:
        return render(request,'signup.html')


        
def logfun(request):
    if request.method=='POST':
        luser=request.POST['luname']
        lpass=request.POST['lpwd']
        louser=auth.authenticate(username=luser,password=lpass)
        if louser is not None:
            auth.login(request,louser)
            messages.info(request,f'Hai {luser}')
            return redirect('addcourse')
        else:
            messages.info(request,'Invalid user or password')
            return redirect('logins')
    else:
        return redirect('logins')
    
def logoutfun(request):
    auth.logout(request)   
    return redirect('home') 

def addcfun(request):
    if request.method=='POST':
        ccode=request.POST['cd']
        csname=request.POST['cname']
        csdes=request.POST['cdes']
        cdu=request.POST['cdur']
        csf=request.POST['cfe']
        addc=add_course(c_code=ccode,c_name=csname,c_des=csdes,c_du=cdu,c_fee=csf)
        addc.save()
        return redirect('addcourse')
    
def stufun(request):
    if request.method=='POST':
        stcode=request.POST['stid'] 
        stname=request.POST['sname'] 
        stadd=request.POST['sadd']
        stage=request.POST['sage']
        stgen=request.POST['sgen']
        stmail=request.POST['smail']  
        addst=add_student(s_code=stcode,s_name=stname,s_add=stadd,s_age= stage,s_gen=stgen,s_mail=stmail)
        addst.save()
        return redirect('addstudent')

@login_required(login_url='logins')    
def showfun(request): 
    shst=add_student.objects.all()  
    return render (request,'showst.html',{'stkey':shst})
