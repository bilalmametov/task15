from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=40) 
    expirience = models.IntegerField()
    students = models.ManyToManyField(
        Student, 
        related_name='teachers'
    ) 


# student1 = Student.objects.create(name='student1', age=15)
# student2 = Student.objects.create(name='student2', age=16)
# student3 = Student.objects.create(name='student3', age=17) 

# teacher1 = Teacher.objects.create(name='teacher1', subject='math', expirience=2)
# teacher1.students.set([student1, student2])
# teacher1.students.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (3)>]>
# teacher2 = Teacher.objects.create(name='teacher2', subject='bio', expirience=1)
# teacher2.students.set((student1, student3))
# student1.teachers.all()
# <QuerySet [<Teacher: Teacher object (1)>, <Teacher: Teacher object (2)>]>

# related_name | related_query_name  