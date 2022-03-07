from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.

def students_list(request):
    context = {'students_list':Student.objects.all()}
    return render(request, 'student/student_list.html',context)

def students_form(request, id=0):
    if request.method =='GET':
        if id==0:
            form = StudentForm()
        else :
            student=Student.objects.get(pk=id)
            form=StudentForm(instance=student)
        return render(request, 'student/student_form.html',{'form':form})

    else:
        if id==0:
         form = StudentForm(request.POST)
        else:
            student= Student.objects.get(pk=id)
            form=StudentForm(instance=student)
        if form.is_valid():
            form.save()
        redirect('/student/list')

def students_delete(request,id):
    student= Student.objects.get(pk=id)
    student.delete()
    redirect('/student/list')