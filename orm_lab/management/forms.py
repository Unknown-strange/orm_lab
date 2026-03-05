from core.models import Student, Course
from django import forms

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'courses']