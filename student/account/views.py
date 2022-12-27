from django.shortcuts import render,redirect
from .models import Course,Contact,Staff
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method =="POST":
        email = request.POST["email"]
        password = request.POST["pass1"]
        try:
            check_user = Staff.objects.get(email=email,password=password)
            request.session['email'] =check_user.email
            request.session['name'] =check_user.name
            request.session['phno'] =check_user.phno
            return render(request,'home.html')
        except Staff.DoesNotExist:
            messages.error(request,'Invalid Username and Password')   
            return redirect('index') 
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                customer =Staff.objects.create(email=email,name=name,password=pass1,phno=phno)
                customer.save()
                messages.info(request,'User created')
                return redirect('login')
        else:
            messages.info(request,'Password is not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')

def forget(request):
    return render(request,'forget.html')


def mainhome(request):
    return render(request,'mainhome.html')

def course(request):
    courses={
        'course':Course.objects.all()
    }
    return render(request,'course.html',courses)

def Gallery(request):
    return render(request,'gallery.html')


def contact(request):
    if request.method=="POST":
        if request.POST['name']is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')