from django.contrib import admin
from school.models import Student, Teacher, Course, Registration

class Students(admin.ModelAdmin):
    list_display = ('id','name', 'identifier', 'cpf', 'date_of_birth')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)

class Teachers(admin.ModelAdmin):
    list_display = ('id','name', 'identifier', 'cpf', 'date_of_birth', 'academic_education')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Teacher, Teachers)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description', 'level', 'teacher')
    list_display_links = ('id', 'course_code')
    search_fields = ('course_code',)

admin.site.register(Course, Courses)

class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'time_course')
    list_display_links = ('id', )

admin.site.register(Registration, Registrations)