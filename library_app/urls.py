from django.urls import path
from library_app.views import (
  CourseCreateView,
  CourseListView,
  BookListView,
  BookCreateView) 

urlpatterns = [
    path('', CourseListView.as_view()),
    path('create/', CourseCreateView.as_view()),
    path('book-list/', BookListView.as_view()),
    path('book-create/', BookCreateView.as_view()),
]