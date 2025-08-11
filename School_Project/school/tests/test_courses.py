from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Course
from school.serializers import CourseSerializer

class CourseTestCase(APITestCase):
    fixtures = ['database_prototype.json']
    def setUp(self):
        
        self.user = User.objects.get(username = 'guilherme')
        self.url = reverse('Courses-list')
        self.client.force_authenticate(user=self.user)

        self.course_01 = Course.objects.get(pk = 1)

        self.course_02 = Course.objects.get(pk = 2)

    def test_get_to_list_courses(self):
        '''Test of GET requisition'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_to_list_one_course(self):
        '''Test of GET requisition one course'''
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_course = Course.objects.get(pk=1)
        data_course_serialized = CourseSerializer(instance = data_course).data
        self.assertEqual(response.data, data_course_serialized)

    def test_post_to_create_one_course(self):
        '''Test of POST requisition one course'''
        datas = {
            'code': 'TC03',
            'description': 'Test Course 03',
            'level': 'A'
        }
        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_one_course(self):
        '''Test of DELETE requisition one course'''
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_to_update_one_course(self):
        '''Test of PUT requisition one course'''
        datas = {
            'code': 'TC01',
            'description': 'Test Course 01',
            'level': 'B',
        }
        response = self.client.put(f'{self.url}1/', datas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)