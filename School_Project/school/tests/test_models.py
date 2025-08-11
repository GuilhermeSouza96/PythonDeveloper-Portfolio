from django.test import TestCase
from school.models import Student, Course, Enrollment

class ModelStudentTestCase(TestCase):
    # def fail_teste(self):
    #     self.fail('Test Fail :(')
    def setUp(self):
        self.student = Student.objects.create(
            name = 'Model Test',
            email = 'modeltest@gmail.com',
            cpf = '68195899056',
            birth_date = '2023-02-02',
            phone = '86 99999-9999'
        )

    def test_check_student_attributes(self):
        '''
        Test to verify attributes of Student Model
        '''
        self.assertEqual(self.student.name, 'Model Test')
        self.assertEqual(self.student.email, 'modeltest@gmail.com')
        self.assertEqual(self.student.cpf, '68195899056')
        self.assertEqual(self.student.birth_date, '2023-02-02')
        self.assertEqual(self.student.phone, '86 99999-9999')

class ModelCourseTestCase(TestCase):
    # def fail_teste(self):
    #     self.fail('Test Fail :(')
    def setUp(self):
        self.course = Course.objects.create(
            code = 'FE01',
            description = 'Curso de teste Front End 01',
            level = 'B'
        )

    def test_check_course_attributes(self):
        '''
        Test to verify attributes of Course Model
        '''
        self.assertEqual(self.course.code, 'FE01')
        self.assertEqual(self.course.description, 'Curso de teste Front End 01')
        self.assertEqual(self.course.level, 'B')

class ModelEnrollmentTestCase(TestCase):
    # def fail_teste(self):
    #     self.fail('Test Fail :(')
    def setUp(self):
        self.student = Student.objects.create(
            name = 'Model Test',
            email = 'modeltest@gmail.com',
            cpf = '68195899056',
            birth_date = '2023-02-02',
            phone = '86 99999-9999'
        )

        self.course = Course.objects.create(
            code = 'FE01',
            description = 'Curso de teste Front End 01',
            level = 'B'
        )

        self.enrollment = Enrollment.objects.create(
            student = self.student,
            course = self.course,
            period = 'M'
        )

    def test_check_enrollment_attributes(self):
        '''
        Test to verify attributes of Enrollment Model
        '''
        self.assertEqual(self.enrollment.student.name, 'Model Test')
        self.assertEqual(self.enrollment.course.code, 'FE01')
        self.assertEqual(self.enrollment.period, 'M')