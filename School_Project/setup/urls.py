from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, ListEnrollmentStudent, ListEnrollmentCourse
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename = 'Students')
router.register('courses', CourseViewSet, basename = 'Courses')
router.register('enrollment', EnrollmentViewSet, basename = 'Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments', ListEnrollmentStudent.as_view()),
    path('course/<int:pk>/enrollments', ListEnrollmentCourse.as_view()),
]
