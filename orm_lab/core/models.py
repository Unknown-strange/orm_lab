from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    created_at = models.DateField(auto_now_add=True)
    
    #course = models.ForeignKey(Course , on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField('Course', blank=True)
    
    def __str__(self):
        return self.name
    

