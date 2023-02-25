from django.contrib import admin
from school.models import Student, Teacher, Course, Registration

class Students(admin.ModelAdmin):
    list_display = ('id','name', 'identifier', 'cpf', 'date_of_birth', 'photo')
    list_display_links = ('id', 'name')
    ordering = ('name',)
    search_fields = ('name', 'cpf', 'identifier', 'date_of_birth',)
    list_per_page = 10

admin.site.register(Student, Students)

class Teachers(admin.ModelAdmin):
    list_display = ('id','name', 'identifier', 'cpf', 'date_of_birth', 'photo', 'academic_education')
    list_display_links = ('id', 'name')
    ordering = ('name',)
    search_fields = ('name', 'cpf', 'identifier', 'date_of_birth',)
    list_per_page = 10

admin.site.register(Teacher, Teachers)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description', 'level', 'teacher')
    list_display_links = ('id', 'course_code')
    ordering = ('course_code',)
    search_fields = ('course_code', 'description', 'level', 'teacher',)
    list_per_page = 10

admin.site.register(Course, Courses)

class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'time_course')
    list_display_links = ('id', )
    list_per_page = 10

admin.site.register(Registration, Registrations)