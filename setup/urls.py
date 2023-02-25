from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from school.views import StudentsViewSet, TeacherViewSet, CoursesViewSet, RegistrationViewSet, ListRegistrationsStudentViewSet, ListEnrolledStudentsViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('teachers', TeacherViewSet, basename='Teachers')
router.register('courses', CoursesViewSet, basename='Registrations')
router.register('registrations', RegistrationViewSet, basename='Courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('students/<int:pk>/registrations/', ListRegistrationsStudentViewSet.as_view()),
    path('courses/<int:pk>/registrations/', ListEnrolledStudentsViewSet.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
