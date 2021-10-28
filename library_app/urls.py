from django.urls import path
from library_app.views import (
  CourseCreateView,
  CourseListView,
  BookListView,
  BookCreateView,
  BranchListView,
  BranchCreateView) 

urlpatterns = [
    path('', CourseListView.as_view()),
    path('create/', CourseCreateView.as_view()),
    path('book-list/', BookListView.as_view()),
    path('book-create/', BookCreateView.as_view()),
    path('branch-list/', BranchListView.as_view()),
    path('branch-create/', BranchCreateView.as_view()),
]