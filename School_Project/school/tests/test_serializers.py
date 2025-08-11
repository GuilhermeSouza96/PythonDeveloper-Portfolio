from django.test import TestCase
from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer

class SerializerStudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name = 'Model Test',
            email = 'modeltest@gmail.com',
            cpf = '68195899056',
            birth_date = '2023-02-02',
            phone = '86 99999-9999'
        )
        self.serializer_student = StudentSerializer(instance=self.student)

    def test_check_serialized_fields_of_student(self):
        '''Test to verify fileds of Student beeing serialized '''
        datas = self.serializer_student.data
        self.assertEqual(set(datas.keys()), set(['id', 'name', 'email', 'cpf', 'birth_date', 'phone']))

    def test_check_content_of_serialized_fields_of_student(self):
        '''Test to verify content of Student fields beeing serialized '''
        datas = self.serializer_student.data
        self.assertEqual(datas['name'], self.student.name)
        self.assertEqual(datas['email'], self.student.email)
        self.assertEqual(datas['cpf'], self.student.cpf)
        self.assertEqual(datas['birth_date'], self.student.birth_date)
        self.assertEqual(datas['phone'], self.student.phone)


class SerializerCourseTestCase(TestCase):
    def setUp(self):
        self.course = Course(
            code = 'MTC',
            description = 'Model Test Course',
            level = 'B',
        )
        self.serializer_course = CourseSerializer(instance=self.course)

    def test_check_serialized_fields_of_course(self):
        """Test to verify fileds of Course beeing serialized"""
        datas = self.serializer_course.data
        self.assertEqual(set(datas.keys()),set(['id','code','description','level']))  
    
    def test_check_content_of_serialized_fields_of_course(self):
        """Test to verify content of Course fields beeing serialized"""
        datas = self.serializer_course.data
        self.assertEqual(datas['code'],self.course.code)
        self.assertEqual(datas['description'],self.course.description)
        self.assertEqual(datas['level'],self.course.level)

class SerializerEnrollmentTestCase(TestCase):
    def setUp(self):
        self.enrollment_student = Student.objects.create(
            name = 'Model Test',
            email = 'modeltest@gmail.com',
            cpf = '68195899056',
            birth_date = '2023-02-02',
            phone = '86 99999-9999'
        )
        self.enrollment_course = Course.objects.create(
            code='MTC',description='Model Test Course',level='B'
        )
        self.enrollment = Enrollment.objects.create(
            student=self.enrollment_student,
            course=self.enrollment_course,
            period='M'
        )
        self.serializer_enrollment = EnrollmentSerializer(instance=self.enrollment)

    def test_check_serialized_fields_of_enrollment(self):
        """Test to verify fileds of Enrollment beeing serialized"""
        datas = self.serializer_enrollment.data
        self.assertEqual(set(datas.keys()),set(['id','student','course','period']))  
    
    def test_check_content_of_serialized_fields_of_enrollment(self):
        """Test to verify content of Enrollment fields beeing serialized"""
        datas = self.serializer_enrollment.data
        self.assertEqual(datas['student'],self.enrollment.student.id)
        self.assertEqual(datas['course'],self.enrollment.course.id)
        self.assertEqual(datas['period'],self.enrollment.period)