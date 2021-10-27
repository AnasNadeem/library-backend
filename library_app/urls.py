from django.urls import path
from library_app.views import (
  CourseCreateView,
  CourseListView) 

urlpatterns = [
    path('', CourseListView.as_view()),
    path('create', CourseCreateView.as_view()),
]