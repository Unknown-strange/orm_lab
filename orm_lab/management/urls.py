from os import name
from django.urls import path 
from .import views

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('list/',views.list_students, name='list_students'),
    path('<int:id>/', views.student_detail, name='student_detail'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<init:id', views.delete_student, name='delete_student'),
]
