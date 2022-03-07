from django import forms
from .models import Student
#creating form model

class StudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields=('fullname','mobile','students_code','sd','stack')
        lebels={
            'fullname':'Full Name',
            'students_code':"Student,s Code",
            'mobile':'Mobile No.',
            'sd':'SD.'
        }