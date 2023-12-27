from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (f'{self.name}')

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField(Course, through='Enrollment')

    def __str__(self):
        return (f'{self.name}')
    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.IntegerField()

    def __str__(self):
        return(f'{self.student} - {self.course}')
    

