from rest_framework import viewsets, generics

from school.models import Student, Teacher, Course, Registration
from school.serializer import StudentSerializer, TeacherSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationsStudentSerializer, ListEnrolledStudentsSerializer

#caching
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import cache_page

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ListRegistrationsStudentViewSet(generics.ListAPIView):
    """listing every student enrollment"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationsStudentSerializer

    #caching
    @method_decorator(cache_page(20)) 
    def dispatch(self, *args, **kwargs):
        return super(ListRegistrationsStudentViewSet, self).dispatch(*args, **kwargs)
    
class ListEnrolledStudentsViewSet(generics.ListAPIView):
    """listing all students enrolled in a course"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrolledStudentsSerializer

    #caching
    @method_decorator(cache_page(20)) 
    def dispatch(self, *args, **kwargs):
        return super(ListEnrolledStudentsViewSet, self).dispatch(*args, **kwargs)