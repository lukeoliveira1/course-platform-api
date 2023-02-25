from django.test import TestCase
from school.models import Student, Teacher, Course, Registration

class TeacherModelTestCase(TestCase):

    def setUp(self):
        self.student = Student(
            name = 'Student Test',
            identifier = '123456789',
            cpf = '12345678901',
            date_of_birth = '2023-05-17',
        )
        self.teacher = Teacher(
            name = 'Teacher Test',
            identifier = '123456789',
            cpf = '12345678901',
            date_of_birth = '2023-05-17',
            academic_education = 'anyway'
        )
        self.course = Course(
            course_code = 'C1',
            description = 'Curso Test',
            level = 'B',
            teacher = self.teacher,
        )
        self.registration = Registration(
            student = self.student,
            course = self.course,
            time_course = 'M',
        )

    def test_check_attributes_of_student(self):
        self.assertEqual(self.student.name, 'Student Test')
        self.assertEqual(self.student.identifier, '123456789')
        self.assertEqual(self.student.cpf, '12345678901')
        self.assertEqual(self.student.date_of_birth, '2023-05-17')

    def test_check_attributes_of_teacher(self):
        self.assertEqual(self.teacher.name, 'Teacher Test')
        self.assertEqual(self.teacher.identifier, '123456789')
        self.assertEqual(self.teacher.cpf, '12345678901')
        self.assertEqual(self.teacher.date_of_birth, '2023-05-17')
        self.assertEqual(self.teacher.academic_education, 'anyway')

    def test_check_attributes_of_course(self):
        self.assertEqual(self.course.course_code, 'C1')
        self.assertEqual(self.course.description, 'Curso Test')
        self.assertEqual(self.course.level, 'B')
        self.assertEqual(self.course.teacher, self.teacher)
    
    def test_check_attributes_of_registration(self):
        self.assertEqual(self.registration.student, self.student)
        self.assertEqual(self.registration.course, self.course)
        self.assertEqual(self.registration.time_course, 'M')
