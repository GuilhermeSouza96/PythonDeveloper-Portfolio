from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Student
from school.serializers import StudentSerializer

class StudentTestCase(APITestCase):
    fixtures = ['database_prototype.json']
    def setUp(self):

        self.user = User.objects.get(username = 'guilherme')
        self.url = reverse('Students-list')
        
        self.client.force_authenticate(user=self.user)

        self.student_01 = Student.objects.get(pk = 2)
        self.student_02 = Student.objects.get(pk = 3)

    def test_get_to_list_students(self):
        '''Test of GET requisition'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_to_list_one_student(self):
        '''Test of GET requisition one student'''
        response = self.client.get(self.url + '2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_student = Student.objects.get(pk=2)
        data_student_serialized = StudentSerializer(instance = data_student).data
        self.assertEqual(response.data, data_student_serialized)

    def test_post_to_create_one_student(self):
        '''Test of POST requisition one student'''
        datas = {
            'name': 'test',
            'email': 'test@email.com',
            'cpf': '82271917034',
            'birth_date': '2003-05-04',
            'phone': '21 99999-9999'
        }
        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_one_student(self):
        '''Test of DELETE requisition one student'''
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_to_update_one_student(self):
        '''Test of PUT requisition one student'''
        datas = {
            'name': 'teste',
            'email': 'teste@email.com',
            'cpf': '42370866071',
            'birth_date': '2003-05-09',
            'phone': '21 99999-9999'
        }
        response = self.client.put(f'{self.url}2/', datas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)