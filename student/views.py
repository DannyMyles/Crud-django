from django.shortcuts import render

# Create your views here.

def students_list(request):
    return render(request, 'student/student_list.html')

def students_form(request):
    return render(request, 'student/student_form.html')

def students_delete(request):
    return render(request, 'template_name')