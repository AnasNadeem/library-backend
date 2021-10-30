from django.urls import path
from management_app.views import (
  ApplicationSubmit,
  ApplicationList, 
  ApproveApplication,
  DismissApplication,
  UnapprovedApplicationList,
  ApprovedApplicationList,
  BookApplicationList,
  UserAskForBook,
  UserBookList)

urlpatterns = [
  path('application/' , ApplicationSubmit.as_view()),
  path('pending-application-list/', UnapprovedApplicationList.as_view()),
  path('approved-application-list/', ApprovedApplicationList.as_view()),
  path('all-application-list/', ApplicationList.as_view()),
  path('approve-application/', ApproveApplication.as_view()),
  path('dismiss-application/', DismissApplication.as_view()),
  path('all-book-user-list/', BookApplicationList.as_view()),
  path('book-application/', UserAskForBook.as_view()),
  path('book-user-list/', UserBookList.as_view())
]