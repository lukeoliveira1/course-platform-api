from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    identifier = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    photo = models.ImageField(blank=True)

    class Meta:
      abstract = True
      
class Student(Person):

  def __str__(self):
    return self.name 

class Teacher(Person):
  academic_education = models.CharField(max_length=30)

  def __str__(self):
    return self.name 

class Course(models.Model):
    NIVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced'),
    )
    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.description

class Registration(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_course = models.CharField(max_length=1, choices=PERIODO,  blank=False, null=False, default='M')
