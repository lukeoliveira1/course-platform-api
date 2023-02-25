from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from school.views import StudentsViewSet, TeacherViewSet, CoursesViewSet, RegistrationViewSet, ListRegistrationsStudentViewSet, ListEnrolledStudentsViewSet

from rest_framework import routers
from rest_framework import permissions

#swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API-school",
      default_version='v1',
      description="A course platform management API",
      terms_of_service="#",
      contact=openapi.Contact(email="owner@apischool.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('teachers', TeacherViewSet, basename='Teachers')
router.register('courses', CoursesViewSet, basename='Registrations')
router.register('registrations', RegistrationViewSet, basename='Courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('students/<int:pk>/registrations/', ListRegistrationsStudentViewSet.as_view()),
    path('courses/<int:pk>/registrations/', ListEnrolledStudentsViewSet.as_view()),
    path('swagger/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
