# ManyToManyApp
1. Получение всех объектов модели. 
    - `./manage.py shell`
    - `from ManyToManyApp.models import Student ,  Teacher`
    - `Student.objects.all()`
    - `Teacher.objects.all()`
#### Student - `<QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>]>`

#### Teacher - `<QuerySet [<Teacher: Teacher object (1)>, <Teacher: Teacher object (2)>]>`
---
2. Фильтрация объектов по определенным условиям.
    - `Student.objects.filter(name = 'student1')`
    - `Teacher.objects.filter(name = 'teacher1')`
#### Student - `<QuerySet [<Student: Student object (1)>]>`
#### Teacher - `<QuerySet [<Teacher: Teacher object (1)>]>`
--- 
3. Использование связанных моделей с помощью related_name и related_query_name.
    - `teacher1.students.set([student1 , student2])`
    - `teacher1.students.all()`
#### Teacher - `<QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>`
---
4. Создание новых объектов модели.

`
    student1 = Student.objects.create(name='student1',age=15)
    student2 = Student.objects.create(name='student2',age=16)
    student3 = Student.objects.create(name='student3',age=17)
    teacher1 = Teacher.objects.create(name='teacher1', subject='Math', experience= 10)
`

5. Обновление существующих объектов.
    -  `Student.objects.filter(pk=1).update(name = 'Alks')`
6. Удаление объектов.
    - `Student.objects.filter(pk=1).delete()`
7. Использование агрегирующих функций (например, count, sum, avg) для получения ста-
тистики данных.
    - `from django.db.models import Sum, Avg`
    - `Teacher.objects.aggregate(Sum('pk'))`
    #### `{'pk__sum': Decimal('3')}`
    - `Teacher.objects.aggregate(Sum('experience'))`
    #### `{'experience__sum': 15}`
8. Использование операторов сравнения (например, __gt, __lt, __contains) для фильтра-
ции данных.
    - `Student.objects.filter(age__gt = 15)`
    #### `<QuerySet [<Student: Student object (2)>, <Student: Student object (3)>]>`
    -  `Student.objects.filter(age__lt = 17)`
    #### `<QuerySet [<Student: Student object (2)>]>`
    - `Student.objects.filter(name__contains = 'Nur')`
    #### `<QuerySet [<Student: Student object (4)>]>`