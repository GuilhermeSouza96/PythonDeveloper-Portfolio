from django.test import TestCase
from school.models import Student, Course

class FixtureTestCase(TestCase):
    fixtures = ['database_prototype.json']

    def test_load_fixture(self):
        '''Test to verify fixture load'''
        student = Student.objects.get(cpf = '15619819819')
        course = Course.objects.get(pk = 1)
        self.assertEqual(student.phone, '89119191981998')
        self.assertEqual(course.code, 'POO')