from django.shortcuts import render,redirect 
from core.models import Student, Course
from .forms import StudentForms


def add_student(request):
    if request.method == "POST":
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForms()
    return render(request, 'management/add_student.html', {'form': form})

def list_students(request):
    students = Student.objects.select_related().prefetch_related('courses').all()
    return render(request, 'management/list_students.html', {'students': students})
