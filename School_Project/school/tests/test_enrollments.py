from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Student, Course, Enrollment
from school.serializers import EnrollmentSerializer

class EnrollmentTestCase(APITestCase):
    fixtures = ['database_prototype.json']
    def setUp(self):
        self.user = User.objects.get(username = 'guilherme')
        self.url = reverse('Enrollments-list')
        self.client.force_authenticate(user=self.user)

        self.student_01 = Student.objects.get(pk = 2)
        self.course_01 = Course.objects.get(pk = 1)

        self.enrollment = Enrollment.objects.get(pk = 1)

    def test_get_to_list_enrollment(self):
        '''Test of GET requisition'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_to_list_one_enrollment(self):
        '''Test of GET requisition one enrollment'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_post_to_create_one_enrollment(self):
        '''Test of POST requisition one enrollment'''
        datas = {
            'student': self.student_01.pk,
            'course': self.course_01.pk,
            'period': 'A'
        }
        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_one_enrollment(self):
        '''Test of DELETE requisition one enrollment'''
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_to_update_one_enrollment(self):
        '''Test of PUT requisition one enrollment'''
        datas = {
            'student': self.student_01.pk,
            'course': self.course_01.pk,
            'period': 'V'
        }
        response = self.client.put(f'{self.url}1/', datas)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)