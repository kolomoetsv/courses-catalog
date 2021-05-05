from django.urls import path

from .views import CourseListView, CourseDetailView, CourseDeleteView, course_create, CourseUpdateView

urlpatterns = [
    path('', CourseListView.as_view(), name='index'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add-course/', course_create, name='form_add_course'),
    path('<int:pk>/delete/', CourseDeleteView.as_view()),
    path('<int:pk>/edit/', CourseUpdateView.as_view()),
]