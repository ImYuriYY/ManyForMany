from django.shortcuts import render, redirect
from .models import *
from datetime import date

def index(request):
    students = Student.objects.all()
    return render(request, 'app/index.html', context={'students': students})



def create(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        course_ids = request.POST.getlist('courses')
        student.save()

        courses = Course.objects.filter(id__in=course_ids)
        student.course.set(courses, through_defaults={'date': date.today(), 'mark': 0})
        return redirect('homepage')
    courses = Course.objects.all()
    return render(request, 'app/create.html', context={'courses': courses})






