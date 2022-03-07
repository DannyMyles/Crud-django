from django.shortcuts import render,redirect
from .forms import StudentForm
# Create your views here.

def students_list(request):
    return render(request, 'student/student_list.html')

def students_form(request):
    if request.method =='GET':
        form = StudentForm()
        return render(request, 'student/student_form.html',{'form':form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('/student/student_list')

def students_delete(request):
    return render(request, 'template_name')