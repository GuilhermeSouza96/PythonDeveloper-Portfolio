from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, ListEnrollmentsCourseSerializer, ListEnrollmentsStudentSerializer, StudentSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from school.throttles import EnrollmentAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    '''
    ViewSet Description:
    - Endpoint for student CRUD.
    Sort Fields:
    - Name: Allows you to sort results by name.

    Search Fields:
    - Name: Allows you to search results by name.
    - CPF: Allows you to search results by CPF.

    Allowed HTTP Methods:
    - GET, POST, PUT, PATCH, DELETE

    Serializer Class:
    - EstudanteSerializer: Used for data serialization and deserialization.
    - If the API version is 'v2', use EstudanteSerializerV2.
    '''
    queryset = Student.objects.all().order_by('id')
    # serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    '''
    ViewSet Description:
    - Endpoint for course CRUD.

    Allowed HTTP Methods:
    - GET, POST, PUT, PATCH, DELETE
    '''
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EnrollmentViewSet(viewsets.ModelViewSet):
    '''
    ViewSet Description:
    - Endpoint for enrollment CRUD.

    Allowed HTTP Methods:
    - GET, POST

    Throttle Classes:
    - EnrollmentAnonRateThrottle: Rate limit for anonymous users.
    - UserRateThrottle: Rate limit for authenticated users.
    '''
    queryset = Enrollment.objects.all().order_by('id')
    serializer_class = EnrollmentSerializer
    throttle_classes = [UserRateThrottle, EnrollmentAnonRateThrottle]
    http_method_names = ['get', 'post']

class ListEnrollmentStudent(generics.ListAPIView):
    '''
    View Description:
    - List Enrollments by Student id
    Params:
    - pk (int): Primary object identifyer. Must be integer
    '''
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id = self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListEnrollmentsStudentSerializer

class ListEnrollmentCourse(generics.ListAPIView):
    '''
    View Description:
    - List Enrollments by Student id
    Params:
    - pk (int): Primary object identifyer. Must be integer
    '''
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id = self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListEnrollmentsCourseSerializer