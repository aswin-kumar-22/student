from django.shortcuts import render,redirect
from django.views import View
from account.models import Staff,Contact
from home.models import Student
from .form import StudentForm
from django.contrib import messages
# Create your views here.


class Home(View):
    def get(self,request):
        return render(request,'home.html')


class Showstaff(View):
    def get(self,request):
        return render(request,'showstaff.html')


class Showstudent(View):
    def get(self,request):
        student=Student.objects.all()
        return render(request,'showstudent.html',{'form':student})


class Enquery(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request,'enquery.html',{'form':customer})


class Form(View):
    def get(self,request):
        std1=StudentForm()
        return render(request,'form.html',{'form':std1})
    def post(self,request):
        if request.method == "POST":
            std1=StudentForm(request.POST)
            if std1.is_valid():
                std1.save()
                student=Student.objects.all()
                return render(request,'showstudent.html',{'form':student})
            else:
                print("Form not valid")
            return redirect("showstudent")

class Delete(View):
    def get(self,request):
        delete=request.GET['delete']
        Student.objects.filter(student_id=delete.delete())
        student=Student.object.all()
        return render(request,'showstudent.html',{'form':student})

class Edit(View):
    def get(self,request):
        edit1=request.GET['edit']
        edit=Student.objects.filter(Student_id=edit1)
        return render(request,'edit.html',{'forms':edit})
    def post(self,request):
        edit1=request.GET['edit']
        if request.method == 'POST':
            if Student.objects.filter(Student_id=edit1).exists():
                if request.POST['student_address']:
                    Student.objects.filter(Student_id=edit1).update(Student_address=request.POST['student_address'])
                if request.POST['student_place']:
                    Student.objects.filter(Student_id=edit1).update(Student_place=request.POST['student_place'])
                if request.POST['student_name']:
                    Student.objects.filter(Student_id=edit1).update(Student_name=request.POST['student_name'])
                if request.POST['student_email']:
                    Student.objects.filter(Student_id=edit1).update(Student_email=request.POST['student_email'])
                if request.POST['student_phone']:
                    Student.objects.filter(Student_id=edit1).update(Student_phone=request.POST['student_phone'])
                students=Student.objects.all()
                return render(request,'showstudent.html',{'form':students})



class Profile(View):
    def get(self,request):
        if request.session['email'] is not None:
            customer=Staff.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'customer':customer})


class Editprofile(View):
    def get(self, request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1) 
        return render(request, 'editprofile.html', {'forms' : edit})
    def post(self, request):
        edit1=request.session['email']
        if request.method =='POST':
            if Staff.objects.filter(email=edit1).exists():
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
            if request.POST['name']:
                Staff.objects.filter(email=edit1).update(name=request.POST['name'])
            if request.POST['email']:
                if Staff.objects.filter(email=request.POST['email']).exists(): 
                    edit=Staff.objects.filter(email=edit1) 
                    messages.error(request, "email id already exits") 
                    return render(request, 'editprofile.html', {'forms' :edit})
            else:
                Staff.objects.filter(email=edit1).update(email=request.POST['email']) 
                request.session['email']=request.POST['email']
            if request.POST['phno']:
                Staff.objects.filter(email=edit1).update(phno=request.POST['phno']) 
            customer=Staff.objects.filter(email=request.session['email']) 
            return render(request, 'profile.html', {'customer': customer})



