from django.shortcuts import render,redirect, get_object_or_404
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
   student = Student.object.all()
   
   name = request.GET.get('name')
   course = request.GET.get('course')
   
   if name:
       student = student.filter(name_icontains=name)
       
   if course:
       student = student.filter(courses_tittle_icontains=course)
   
   return render(request, 'list_students.html', {'student': student})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    
    return render(request, "student_detail.html", {'student':student})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        form = StudentForms(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students.html')
    else:
        form = StudentForms(instance=student)
    
    return render(request, 'edit_student.html', {'form': form})
        
def delete_student(request, id):
    student = get_object_or_404(Student,id=id)
    
    if request.method == "POST":
        student.delete()
        return redirect('list_students')
    return render(request, "delete_student.html", {"student": student})