from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CourseViewSet, EnrollmentViewSet, ListEnrollmentStudent, ListEnrollmentCourse
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="School's API Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename = 'Students')
router.register('courses', CourseViewSet, basename = 'Courses')
router.register('enrollment', EnrollmentViewSet, basename = 'Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments', ListEnrollmentStudent.as_view()),
    path('course/<int:pk>/enrollments', ListEnrollmentCourse.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
