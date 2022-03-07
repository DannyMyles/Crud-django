from django import forms
from .models import Student
#creating form model

class StudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields='__all__'