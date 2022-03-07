from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def students_list(request):
    return render(request, 'student/student_list.html')

def students_form(request):
    form = StudentForm()
    return render(request, 'student/student_form.html',{'form':form})

def students_delete(request):
    return render(request, 'template_name')