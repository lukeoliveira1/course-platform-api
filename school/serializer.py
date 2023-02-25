from rest_framework import serializers
from school.models import Student, Teacher, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = []

class ListRegistrationsStudentSerializer(serializers.ModelSerializer):
    """show time_course description instead of ('B','I','A')"""
    name_course = serializers.ReadOnlyField(source='course.description')
    time_course = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['name_course', 'time_course']

    def get_time_course(self, obj):
        return obj.get_time_course_display()

class ListEnrolledStudentsSerializer(serializers.ModelSerializer):
  """show student name instead of student ID""" 
  name_student = serializers.ReadOnlyField(source='student.name')

  class Meta:
    model = Registration
    fields = ['name_student']
